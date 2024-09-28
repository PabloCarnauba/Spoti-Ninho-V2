import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Conexao import Conexao
from Componentes.CadastrarUser import Ui_CadastrarUsuario
from Componentes.menuPYQT import Ui_MenuInicial
from Componentes.telalogin import Ui_TelaLogin
from Componentes.TelaRemover import Ui_TelaRemover

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
        self.construtorTelaMenuInicial.botaoEntrar.clicked.connect(self.exibirTelaLogin)
        self.construtorTelaMenuInicial.botaoRemover.clicked.connect(self.exibirTelaRemover)

        self.layoutContentPane.addWidget(self.telaMenuInicial)
        
        self.telaCadastrar = QWidget()
        self.construtorTelaCadastrar = Ui_CadastrarUsuario()
        self.construtorTelaCadastrar.setupUi(self.telaCadastrar)
        self.construtorTelaCadastrar.BotaoCadastrar.clicked.connect(self.cadastrarUsuario)
        self.layoutContentPane.addWidget(self.telaCadastrar)

        self.TelaLogin = QWidget()
        self.construtorTelaLogin = Ui_TelaLogin()
        self.construtorTelaLogin.setupUi(self.TelaLogin)
        self.construtorTelaLogin.BotaoLogin.clicked.connect(self.LogarUsuario)
        self.layoutContentPane.addWidget(self.TelaLogin)

        self.TelaRemover = QWidget()
        self.construtorTelaRemover = Ui_TelaRemover()
        self.construtorTelaRemover.setupUi(self.TelaRemover)
        self.construtorTelaRemover.BotaoRemover.clicked.connect(self.RemoverUsuario)
        self.layoutContentPane.addWidget(self.TelaRemover)
    

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

    def mostrarPopup(self, mensagem):
        popup = QMessageBox(self)
        popup.setText(mensagem)
        popup.exec()

    def validarCampos(self, *campos):
        return all(campo != "" for campo in campos)

    def exibirTelaCadastrar(self):
        
        self.layoutContentPane.setCurrentIndex(1)

    def cadastrarUsuario(self):
        nomeUsuario = self.construtorTelaCadastrar.inputUsuario.text()
        EmailUsuario = self.construtorTelaCadastrar.inputEmail.text()
        senhaUsuario = self.construtorTelaCadastrar.inputSenha.text()

        if not self.validarCampos(nomeUsuario, EmailUsuario, senhaUsuario):
            self.mostrarPopup("Preencha todos os campos")
            return
        else:
            self.conexaoBD.manipularComParametros("INSERT INTO usuario (nome,senha,email) VALUES(%s, %s, %s)",  (nomeUsuario, senhaUsuario, EmailUsuario))

            resultado = self.conexaoBD.consultar("SELECT * FROM usuario")
            print(resultado)

    def exibirTelaLogin(self):
        
        self.layoutContentPane.setCurrentIndex(2)   
    
    def LogarUsuario(self):
        nomeUsuario = self.construtorTelaLogin.inputUsuario.text()
        senhaUsuario = self.construtorTelaLogin.inputSenha.text()

        if not self.validarCampos(nomeUsuario, senhaUsuario):
            self.mostrarPopup("Preencha todos os campos")
            return
        else:
            resultado = self.conexaoBD.consultarComParametros("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (nomeUsuario, senhaUsuario))
            print(resultado)

    
    def exibirTelaRemover(self):
        
        self.layoutContentPane.setCurrentIndex(3)   
    
    def RemoverUsuario(self):
        EmailUsuario = self.construtorTelaRemover.inputEmail.text()
        
        if not self.validarCampos(EmailUsuario):
            self.mostrarPopup("Preencha todos os campos")
            return
        else:
            usuario_existente = self.conexaoBD.consultarComParametros("SELECT * FROM usuario WHERE email = %s", (EmailUsuario,))

        if usuario_existente:
            id_usuario = usuario_existente[0][0]
        playlist = self.conexaoBD.consultarComParametros("SELECT * FROM playlist WHERE id_usuario  = %s", (id_usuario,))
        
        lista_id_play = []
        
        for ID in playlist:
            lista_id_play.append(ID[0])
            
        self.conexaoBD.manipularComParametros("DELETE FROM historico WHERE nome = %s", (usuario_existente[0][1],))
        
        for i in range(len(lista_id_play)):
            self.conexaoBD.manipularComParametros("DELETE FROM lista WHERE id_playlist = %s", (lista_id_play[i],))
            
        self.conexaoBD.manipularComParametros("DELETE FROM playlist WHERE id_usuario = %s", (id_usuario,))
        self.conexaoBD.manipularComParametros("DELETE FROM usuario WHERE email = %s", ( EmailUsuario,))
        
        popup = QMessageBox(self)
        popup.setText("USUÁRIO REMOVIDO!")
        popup.exec()
        
        

def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()