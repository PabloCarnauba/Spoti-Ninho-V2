import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Conexao import Conexao
import interface
from Componentes.CadastrarUser import Ui_CadastrarUsuario
from Componentes.menuPYQT import Ui_MenuInicial
from Componentes.TelaLogin import Ui_TelaLogin
from Componentes.TelaRemover import Ui_TelaRemover
from Componentes.menu_usuario import Ui_menu_user
from Componentes.criarPlaylist import Ui_criarPlay
from Componentes.musicas import Ui_musicas

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
        self.construtorTelaCadastrar.backButton_3.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(0))   

        self.layoutContentPane.addWidget(self.telaCadastrar)

        self.TelaLogin = QWidget()
        self.construtorTelaLogin = Ui_TelaLogin()
        self.construtorTelaLogin.setupUi(self.TelaLogin)
        self.construtorTelaLogin.BotaoLogin.clicked.connect(self.LogarUsuario)
        self.construtorTelaLogin.backButton_3.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(0))
        self.layoutContentPane.addWidget(self.TelaLogin)

        self.TelaRemover = QWidget()
        self.construtorTelaRemover = Ui_TelaRemover()
        self.construtorTelaRemover.setupUi(self.TelaRemover)
        self.construtorTelaRemover.BotaoRemover.clicked.connect(self.RemoverUsuario)
        self.construtorTelaRemover.backButton_2.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(0))
        self.layoutContentPane.addWidget(self.TelaRemover)
        
        self.TelaMenuUser = QWidget()
        self.construtorTelaMenuUser = Ui_menu_user()
        self.construtorTelaMenuUser.setupUi(self.TelaMenuUser)
        self.construtorTelaMenuUser.button_sair.clicked.connect(lambda:self.close())
        #self.construtorTelaMenuUser.button_verPlay.clicked.connect()
        self.construtorTelaMenuUser.button_escutarPlay.clicked.connect(lambda:self.close())
        self.construtorTelaMenuUser.button_escutarPlay.clicked.connect(self.exibirPlayList)
        #self.construtorTelaMenuUser.button_historico.clicked.connect()
        self.construtorTelaMenuUser.button_criarPlay.clicked.connect(self.exibirCriarPlay)
        self.layoutContentPane.addWidget(self.TelaMenuUser)
        self.construtorTelaMenuUser.backButton_4.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(0))
        
        self.TelaCriarPlay = QWidget()
        self.construtorTelaCriarPlay = Ui_criarPlay()
        self.construtorTelaCriarPlay.setupUi(self.TelaCriarPlay)
        self.construtorTelaCriarPlay.button_escutarPlay.clicked.connect(self.criarPlaylist)
        self.construtorTelaCriarPlay.button_escutarPlay.clicked.connect(self.exibirTelaMusicas)
        self.layoutContentPane.addWidget(self.TelaCriarPlay)
        self.construtorTelaCriarPlay.backButton_4.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(4))
        
        self.TelaMusicas = QWidget()
        self.construtorTelaMusicas = Ui_musicas()
        self.construtorTelaMusicas.setupUi(self.TelaMusicas)
        self.construtorTelaMusicas.backButton_4.clicked.connect(lambda: self.layoutContentPane.setCurrentIndex(5))

        
        lista_musicas = [self.construtorTelaMusicas.Medobobo,self.construtorTelaMusicas.Dancin, self.construtorTelaMusicas.beggin, self.construtorTelaMusicas.AnjoAzul, self.construtorTelaMusicas.Troco, self.construtorTelaMusicas.blue, self.construtorTelaMusicas.Eduard, self.construtorTelaMusicas.Intheend, self.construtorTelaMusicas.Sunshine,self.construtorTelaMusicas.Icarly]
            
        for musica in lista_musicas:
            
            musica.clicked.connect(self.adicionar_musica)
    
        self.layoutContentPane.addWidget(self.TelaMusicas)
    

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
        
        global resultado
        
        nomeUsuario = self.construtorTelaLogin.inputUsuario.text()
        
        senhaUsuario = self.construtorTelaLogin.inputSenha.text()
        
        resultado = self.conexaoBD.consultarComParametros("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (nomeUsuario, senhaUsuario))
        
        if not self.validarCampos(nomeUsuario, senhaUsuario):
            
            self.mostrarPopup("Preencha todos os campos")
            
            return
        
        else:
            
            if resultado != []:
                
                self.construtorTelaMenuUser.rotuloMenuInicial.setText(f"Menu - {nomeUsuario}")
                
                self.layoutContentPane.setCurrentIndex(4)
                
                print(resultado)
                
            else:
                 self.mostrarPopup("Usuário não encontrado!")
                
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
        
        else:
            
            popup.setText("USUÁRIO NÃO ENCONTRADO!")
            
        
    def exibirCriarPlay(self):
        
        self.layoutContentPane.setCurrentIndex(5)
        
    def criarPlaylist (self):
        
        nome_playlist = self.construtorTelaCriarPlay.lineEdit.text()
        
        id_usuario = resultado[0][0]
        
        self.conexaoBD.manipularComParametros(
        "INSERT INTO playlist (nome_playlist, id_usuario) VALUES (%s, %s)",
        (nome_playlist, id_usuario)
    )
        
        global id_playlist
        
        id_playlist = self.conexaoBD.consultarComParametros(
        "SELECT id_playlist FROM playlist WHERE nome_playlist = %s AND id_usuario = %s ORDER BY id_playlist DESC LIMIT 1", 
        (nome_playlist, id_usuario)
    )[0][0]
        
    def exibirTelaMusicas (self):
        
        self.layoutContentPane.setCurrentIndex(6)
        
    def adicionar_musica(self):
        
        button = self.sender()
        
        print(f"{button.text()}")
        
        nome_musica = button.text()
        
        id_musica = self.conexaoBD.consultarComParametros("SELECT * FROM musicas WHERE nome = %s", (nome_musica,))[0][0]
        
        self.conexaoBD.manipularComParametros(
                
                "INSERT INTO lista (id_playlist, id_musica) VALUES (%s, %s)",
                (id_playlist, id_musica)
                
            )
        
    def exibirPlayList(self):
        
        nome_user = resultado[0][1]
        
        interface.rodar(nome_user)
        

def main():
    
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()