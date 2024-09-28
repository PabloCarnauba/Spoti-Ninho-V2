import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from conexao import Conexao
from Componentes.CadastrarUser import Ui_Form
from Componentes.menuInicial import Ui_MenuInicial

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conexaoBD = Conexao("localhost", "root", "mysql", "spotninho")
        self.setWindowTitle("Janela Principal")
        self.setFixedSize(400,300)

        self.contentPane = QWidget()
        self.layoutContentPane = QStackedLayout()
        self.contentPane.setLayout(self.layoutContentPane)
        
        self.telaMenuInicial = QWidget()
        self.construtorTelaMenuInicial = Ui_MenuInicial()
        self.construtorTelaMenuInicial.setupUi(self.telaMenuInicial)

        self.construtorTelaMenuInicial.botaoSair.clicked.connect(lambda:self.close())
        self.construtorTelaMenuInicial.botaoCadastrar.clicked.connect(self.exibirTelaCadastrar)

        self.layoutContentPane.addWidget(self.telaMenuInicial)

        self.telaCadastrar = QWidget()
        self.construtorTelaCadastrar = Ui_Form()
        self.construtorTelaCadastrar.setupUi(self.telaCadastrar)
        self.construtorTelaCadastrar.BotaoCadastrar.clicked.connect(self.cadastrarUsuario)
        self.layoutContentPane.addWidget(self.telaCadastrar)
    

        #Lógica de adição e troca de telas

        # self.tela1 = QWidget()
        # self.tela1.setStyleSheet("background-color:red")

        # self.layoutContentPane.addWidget(self.tela1)

        # self.tela2 = QWidget()
        # self.tela2.setStyleSheet("background-color:blue")

        # self.layoutContentPane.addWidget(self.tela2)

        # self.layoutContentPane.setCurrentIndex(0)

        #caminho do arquivo ui 
        #pyuic6 Trabalho\Designs\menuPYQT.ui -o menuInicial.py

        self.setCentralWidget(self.contentPane)

    def exibirTelaCadastrar(self):
        
        self.layoutContentPane.setCurrentIndex(1)

    def cadastrarUsuario(self):
        nomeUsuario = self.construtorTelaCadastrar.inputUsuario.text()
        emailUsuario = self.construtorTelaCadastrar.inputEmail.text()
        senhaUsuario = self.construtorTelaCadastrar.inputSenha.text()

        if (nomeUsuario == "" or  emailUsuario == "" or  senhaUsuario == ""):
            popup = QMessageBox(self)
            popup.setText("Preencha todos os campos")
            popup.exec()
        else:

            self.conexaoBD.manipularComParametros("INSERT INTO usuario (nome,senha,email) VALUES(%s, %s, %s)",  (nomeUsuario, senhaUsuario, emailUsuario))

            resultado = self.conexaoBD.consultar("SELECT * FROM usuario")
            print(resultado)
               
def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()