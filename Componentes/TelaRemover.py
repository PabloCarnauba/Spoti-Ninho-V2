# Form implementation generated from reading ui file 'Designs\TelaRemover.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TelaRemover(object):
    def setupUi(self, TelaRemover):
        TelaRemover.setObjectName("TelaRemover")
        TelaRemover.resize(400, 300)
        TelaRemover.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:black ;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:grey;\n"
"\n"
"}")
        self.Email = QtWidgets.QLabel(parent=TelaRemover)
        self.Email.setGeometry(QtCore.QRect(80, 140, 49, 21))
        self.Email.setObjectName("Email")
        self.BotaoRemover = QtWidgets.QPushButton(parent=TelaRemover)
        self.BotaoRemover.setGeometry(QtCore.QRect(70, 240, 131, 31))
        self.BotaoRemover.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"}\n"
"")
        self.BotaoRemover.setObjectName("BotaoRemover")
        self.inputEmail = QtWidgets.QLineEdit(parent=TelaRemover)
        self.inputEmail.setGeometry(QtCore.QRect(140, 140, 171, 22))
        self.inputEmail.setText("")
        self.inputEmail.setObjectName("inputEmail")
        self.rotuloMenuInicial_3 = QtWidgets.QLabel(parent=TelaRemover)
        self.rotuloMenuInicial_3.setGeometry(QtCore.QRect(120, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        self.rotuloMenuInicial_3.setFont(font)
        self.rotuloMenuInicial_3.setStyleSheet("Color rgb(255, 255, 255)")
        self.rotuloMenuInicial_3.setObjectName("rotuloMenuInicial_3")
        self.backButton_2 = QtWidgets.QPushButton(parent=TelaRemover)
        self.backButton_2.setGeometry(QtCore.QRect(210, 240, 131, 31))
        self.backButton_2.setStyleSheet("color: white")
        self.backButton_2.setObjectName("backButton_2")
        self.frame = QtWidgets.QFrame(parent=TelaRemover)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setMinimumSize(QtCore.QSize(400, 300))
        self.frame.setMaximumSize(QtCore.QSize(400, 300))
        self.frame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.Email.raise_()
        self.BotaoRemover.raise_()
        self.inputEmail.raise_()
        self.rotuloMenuInicial_3.raise_()
        self.backButton_2.raise_()

        self.retranslateUi(TelaRemover)
        QtCore.QMetaObject.connectSlotsByName(TelaRemover)

    def retranslateUi(self, TelaRemover):
        _translate = QtCore.QCoreApplication.translate
        TelaRemover.setWindowTitle(_translate("TelaRemover", "Form"))
        self.Email.setText(_translate("TelaRemover", "<html><head/><body><p><span style=\" font-weight:700;\">Email :</span></p></body></html>"))
        self.BotaoRemover.setText(_translate("TelaRemover", "REMOVER"))
        self.rotuloMenuInicial_3.setText(_translate("TelaRemover", "REMOVER USUÁRIO"))
        self.backButton_2.setWhatsThis(_translate("TelaRemover", "<html><head/><body><p><span style=\" font-weight:700;\">Voltar</span></p></body></html>"))
        self.backButton_2.setText(_translate("TelaRemover", "VOLTAR"))
