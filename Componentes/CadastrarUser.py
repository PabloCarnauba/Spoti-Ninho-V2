# Form implementation generated from reading ui file 'Designs\CadastrarUser.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.rotuloMenuInicial = QtWidgets.QLabel(parent=Form)
        self.rotuloMenuInicial.setGeometry(QtCore.QRect(90, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        self.rotuloMenuInicial.setFont(font)
        self.rotuloMenuInicial.setStyleSheet("Color rgb(255, 255, 255)")
        self.rotuloMenuInicial.setObjectName("rotuloMenuInicial")
        self.inputUsuario = QtWidgets.QLineEdit(parent=Form)
        self.inputUsuario.setGeometry(QtCore.QRect(150, 80, 171, 22))
        self.inputUsuario.setText("")
        self.inputUsuario.setObjectName("inputUsuario")
        self.Usuario = QtWidgets.QLabel(parent=Form)
        self.Usuario.setGeometry(QtCore.QRect(80, 80, 49, 21))
        self.Usuario.setObjectName("Usuario")
        self.Email = QtWidgets.QLabel(parent=Form)
        self.Email.setGeometry(QtCore.QRect(80, 140, 49, 21))
        self.Email.setObjectName("Email")
        self.inputEmail = QtWidgets.QLineEdit(parent=Form)
        self.inputEmail.setGeometry(QtCore.QRect(150, 140, 171, 22))
        self.inputEmail.setText("")
        self.inputEmail.setObjectName("inputEmail")
        self.Senha = QtWidgets.QLabel(parent=Form)
        self.Senha.setGeometry(QtCore.QRect(80, 200, 49, 21))
        self.Senha.setObjectName("Senha")
        self.inputSenha = QtWidgets.QLineEdit(parent=Form)
        self.inputSenha.setGeometry(QtCore.QRect(150, 200, 171, 22))
        self.inputSenha.setText("")
        self.inputSenha.setObjectName("inputSenha")
        self.BotaoCadastrar = QtWidgets.QPushButton(parent=Form)
        self.BotaoCadastrar.setEnabled(True)
        self.BotaoCadastrar.setGeometry(QtCore.QRect(110, 250, 181, 31))
        self.BotaoCadastrar.setStyleSheet("background-color: black;\n"
"color:  white;\n"
"border-radius: 10px\n"
"")
        self.BotaoCadastrar.setObjectName("BotaoCadastrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rotuloMenuInicial.setText(_translate("Form", "CADASTRAR USUÁRIO"))
        self.Usuario.setText(_translate("Form", "Usuário :"))
        self.Email.setText(_translate("Form", "Email :"))
        self.Senha.setText(_translate("Form", "Senha : "))
        self.BotaoCadastrar.setText(_translate("Form", "CADASTRAR"))