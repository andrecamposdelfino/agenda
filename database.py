import sqlite3

conexao = sqlite3.connect("lembrete.db")
cursor = conexao.cursor()

def criar_tabela():
    query = """
        CREATE TABLE IF NOT EXISTS lembrete(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(60) NOT NULL,
            nota VARCHAR(155) NOT NULL,
            data VARCHAR(60) NOT NULL
        )
    """
    cursor.execute(query)
    conexao.commit()


def select():
    query = """
        SELECT * FROM lembrete
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    print(dados_rsult)

def insert(titulo, nota, data):
    query = """
        INSERT INTO lembrete(titulo, nota, data)VALUES(?,?,?)
    """
    cursor.execute(query, (titulo, nota, data))
    conexao.commit()


