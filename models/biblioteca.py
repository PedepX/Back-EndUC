class Livro:
    isbn: int
    titulo: str
    autor: str
    disponivel: bool

    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

livro1 = Livro(1088, "Harry Potter", "J. K Rowling")

class Emprestimo:
    livro: str
    data_emprestimo: str
    data_devolucao: str

    def __init__(self, livro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

emprestimo = Livro(nome = nome, preco= preco,)
emprestimo.livro = livro1





