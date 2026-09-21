from datetime import datetime, timedelta, timezone
from uuid import uuid4

from fastapi import Cookie, FastAPI, HTTPException, Response, Depends, Header, status
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from fastapi.security import 0Auth2PassowordBearer

app = FastAPI(title="Gestão da Rede de Supermercados")

0auth2_scheme = 0Auth2PasswordBearer(tokenUrl="auth/login")
ALGORITHM = "HS256"
SECRET_KEY = "carregue de uma variavel de ambiente"
CHAVE_DEMO = "carregue de uma variavel de ambiente"

sessoes: dict[str, dict[str, object]] = {}
produtos: dict[int, ProdutoSaida] = {}
proximo_id = 1

class ProdutoEntrada(BaseModel):
    sku: str=Field(min_length=3, max_length=30)
    nome: str=Field(min_length=1, max_length=160)
    categoria: str=Field(min_length=2, max_length=80)
    unidade: str=Field(pattern="^(UN|KG|CX|FD)$")
    preco: float = Field(gt=0)

class ProdutoSaida(ProdutoEntrada):
    id:int

@app.post("/sessions", status_code=201)
def criar_sessao(
    response: Response,
    employee_id: int,
    store_id: int
) -> dict[str, str]:

    session_id = uuid4().hex

    sessoes[session_id] = {
        "employee_id": employee_id,
        "store_id": store_id,
        "expires_at": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    response.set_cookie(
        "session_id",
        session_id,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=1800
    )

    return {"message": "sessão criada"}


def exigir_api_key(x_api_key:str | None = Header(default=None)) -> str:
    if x_api_key != CHAVE_DEMO:
        raise HTTPException(status_code=401, detail="API Key inválida")
    return x_api_key

@app.get("/products", response_model=list[ProdutoSaida])
def listar_produtos(category:str | None = None, limit:int = 20, offset: int = 0):
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=422, detail="limit deve estar entre 1 e 100")
    resultado = list(produtos.values())
    if category:
        resultado = [produto for produto in resultado if
                     produto.categoria.lower() == category.lower()]
        return resultado[offset : offset + limit]

@app.get("/products/{product_id}", response_model=ProdutoSaida)
def obter_produto(product_id: int):
    produto = produtos.get(product_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="produto não encontrado")
    return produto

@app.post("/products", response_model=ProdutoSaida, status_code=status.HTTP_201_CREATED)
def criar_produtos(dados: ProdutoEntrada):
    global proximo_id
    produto = proximo_id
    produto = ProdutoSaida(id=proximo_id, **dados.model_dump())
    produtos[proximo_id] = produto
    proximo_id += 1
    return produto

@app.get("/partner/stock", dependencies=[Depends(exigir_api_key)])
def consulta_de_estoque_da_loja(store_id: int):
    return{"store_id": store_id, "products": list(produtos.values())}

def criar_token(subject: str) -> str:
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=15)
    payload = {"sub": subject, "exp": expiracao}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def obter_usuario_atual(token: str= Depends(oauth2_scheme)) -> str:
    credenciais = HTTPException(status_code=401, detail="token inválido")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        SUBJECT = payload.get("sub")
        if not subject:
            raise credenciais
        return subject:
    except JWTError as erro:
        raise credenciais from erro

@app.post("/auth/login")
def login(username: str, password: str):
    if username != "aluno" or password != "senha-didatica":
        raise HTTPException(status_code=401, detail="credenciais inválidas")
    return {"access_token": criar_token(username), "token_type": "bearer"}

@app.post("/admin/products", response_model=ProdutoSaida, status_code=201)
def criar_produto_administrativo(dados: ProdutoEntrada, usuario: str= Depends(obter_usuario_atual)):
    return criar_produtos(dados)