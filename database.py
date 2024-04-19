import sqlite3

conexao = sqlite3.connect("lembrete.db")
cursor = conexao.cursor()

def criar_tabela():
    query = """
        CREATE TABLE IF NOT EXISTS lembrete(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(60) NOT NULL,
            nota VARCHAR(155) NOT NULL,
            data VARCHAR(60) NOT NULL,
            status VRCHAR(60) NOT NULL
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

def select_count():
    query = """
        SELECT count(*) FROM lembrete
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_data(data):
    query = f"""
        SELECT count(*) FROM lembrete WHERE data = "{data}"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_total_datas(data):
    query = f"""
        SELECT * FROM lembrete WHERE data = "{data}"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_total_programadas():
    query = """
        SELECT * FROM lembrete WHERE status = "Programados"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_programados():
    query = """
        SELECT count(*) FROM lembrete WHERE status = "Programados"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_concluidos():
    query = """
        SELECT count(*) FROM lembrete WHERE status = "Concluidos"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult

def select_all_concluidos():
    query = """
        SELECT * FROM lembrete WHERE status = "Concluidos"
    """
    cursor.execute(query)
    dados_rsult = cursor.fetchall()
    return dados_rsult


def insert(titulo, nota, data, status):
    query = """
        INSERT INTO lembrete(titulo, nota, data, status)VALUES(?,?,?, ?)
    """
    cursor.execute(query, (titulo, nota, data, status))
    conexao.commit()

def update(titulo, nota, data, status, id):
    query = """
        UPDATE lembrete SET titulo = ?, nota = ?, data = ?, status = ? WHERE id = ?
    """
    cursor.execute(query, (titulo, nota, data, status, id))
    conexao.commit()
