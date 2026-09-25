import sqlite3
from banco import db


# Pega os aliens que estão no TinyDB
aliens = db.all()


# Cria/conecta ao banco SQLite
banco = sqlite3.connect("ominitrix.db")
cursor = banco.cursor()


# Cria a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS aliens (
        idomnitrix INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        raca TEXT NOT NULL,
        planeta_natal TEXT NOT NULL,
        habilidade TEXT NOT NULL
    )
""")


# Transfere os aliens para o SQLite
for alien in aliens:

    cursor.execute("""
        INSERT OR REPLACE INTO aliens
        (idomnitrix, nome, raca, planeta_natal, habilidade)
        VALUES (?, ?, ?, ?, ?)
    """, (
        alien["idomnitrix"],
        alien["nome"],
        alien["raca"],
        alien["planeta_natal"],
        alien["habilidade"]
    ))


# Salva as alterações
banco.commit()

# Fecha o banco
banco.close()


print("Migração concluída!")
print(f"{len(aliens)} aliens foram transferidos para o SQLite.")