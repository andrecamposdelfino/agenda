# imports das bibliotecas
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import database as db

# mensagens do sistema
def msgInfo(msg):
    QMessageBox.information(
        None,
        "Sucesso",
        msg
    )

def msgWarning(msg):
    QMessageBox.warning(
        None,
        "Error",
        msg
    )


# funcao para carregar o formulario de lancamnto
def showFormLancamento():
    form_lancamento.show()

# funcao para carregar o formulario de lancamnto
def closeFormLancamento():
    form_lancamento.close()

# salvar um novo lembrete
def inserir():
    try:
        titulo = form_lancamento.txtTitulo.text()
        nota = form_lancamento.txtNotas.text()
        data = form_lancamento.txtDt.text()

        if titulo != "" and nota != "" and data != "":
            db.insert(titulo, nota, data)
            msgInfo("Lancamento concluido!!")
        else:
            msgWarning(f"O preenchimento dos campos são obrigatorio : {error}")
    except Exception as error:
        msgWarning(f"Error ao tentar salvar o lembrete : {error}")


# criar o app ( janela )
app = QtWidgets.QApplication([])

# cria os formulario
form_pricipal = uic.loadUi("./views/formPrincipal.ui")
form_lancamento = uic.loadUi("./views/formLancamento.ui")

# botao novo chamando a funcao para carregr o form
form_pricipal.btnNovo.clicked.connect(
    showFormLancamento
)

form_lancamento.btnNovo.clicked.connect(inserir)
form_lancamento.btnCancelar.clicked.connect(closeFormLancamento)

# inicia o form principal
form_pricipal.show()

# executa o app
app.exec()