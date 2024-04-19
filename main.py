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

# carrega o fomulario que lista as tarefas do dia
def showFormListarHoje():
    form_listagem_hoje.show()
    data = form_pricipal.txtDt.text()
    dados = db.select_total_datas(data)
    form_listagem_hoje.dgvDadosHoje.setRowCount(len(dados))
    form_listagem_hoje.dgvDadosHoje.setColumnCount(5)
    for linha in range(0, len(dados)):
        for coluna in range(0, 5):
            try:
                form_listagem_hoje.dgvDadosHoje.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados[linha][coluna])))
            except Exception as error:
                print(f"Error ao tentar listar : {error}")


# carrega o fomulario que lista as tarefas programadas
def showFormListaProgramados():
    form_listagem_programados.show()
    dados = db.select_total_programadas()
    form_listagem_programados.dgvDadosProgramados.setRowCount(len(dados))
    form_listagem_programados.dgvDadosProgramados.setColumnCount(5)
    for linha in range(0, len(dados)):
        for coluna in range(0, 5):
            try:
                form_listagem_programados.dgvDadosProgramados.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados[linha][coluna])))
            except Exception as error:
                print(f"Error ao tentar listar : {error}")


# salvar um novo lembrete
def inserir():
    try:
        titulo = form_lancamento.txtTitulo.text()
        nota = form_lancamento.txtNotas.text()
        data = form_lancamento.txtDt.text()
        status = form_lancamento.comboBox.currentText()

        if titulo != "" and nota != "" and data != "":
            db.insert(titulo, nota, data, status)
            todos_os_registro = db.select_count()
            for registro in todos_os_registro:
                form_pricipal.lblTotalTodos.setText(str(registro[0]))

            data = form_pricipal.txtDt.text()
            registro_datas = db.select_data(data)
            for registro_data in registro_datas:
                form_pricipal.lblTotalHoje.setText(str(registro_data[0]))

            msgInfo("Lancamento concluido!!")
        else:
            msgWarning(f"O preenchimento dos campos são obrigatorio")
    except Exception as error:
        msgWarning(f"Error ao tentar salvar o lembrete : {error}")


# criar o app ( janela )
app = QtWidgets.QApplication([])

# cria os formulario
form_pricipal = uic.loadUi("./views/formPrincipal.ui")
form_lancamento = uic.loadUi("./views/formLancamento.ui")
form_listagem_hoje = uic.loadUi("./views/formListarHoje.ui")
form_listagem_programados = uic.loadUi("./views/formListarProgramados.ui")
form_listagem_concluidos = uic.loadUi("./views/formListarConcluidos.ui")
form_listagem_todos = uic.loadUi("./views/formListarTodos.ui")

# botao novo chamando a funcao para carregr o form
form_pricipal.btnNovo.clicked.connect(
    showFormLancamento
)

# botoes do formulario principal
form_pricipal.btnVisualizarHoje.clicked.connect(showFormListarHoje)
form_pricipal.btnVisualizarProgramados.clicked.connect(showFormListaProgramados)
form_pricipal.btnVisualizarConcluido.clicked.connect(showFormListarHoje)
form_pricipal.btnVisualizarTodos.clicked.connect(showFormListarHoje)

form_lancamento.btnNovo.clicked.connect(
    inserir
)

form_lancamento.btnCancelar.clicked.connect(
    closeFormLancamento
)

# inicia o form principal
form_pricipal.show()

# recebo todos os lancamntos e faco uma contagem
todos_os_registro = db.select_count()
for registro in todos_os_registro:
    form_pricipal.lblTotalTodos.setText(str(registro[0]))


# recebo a lista com dados conforme a data do formulario e faco uma ontagem por data
data = form_pricipal.txtDt.text()
registro_datas = db.select_data(data)
for registro_data in registro_datas:
    form_pricipal.lblTotalHoje.setText(str(registro_data[0]))


# executa o app
app.exec()