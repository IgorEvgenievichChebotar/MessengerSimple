from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import socket
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

class Ui_signUp(object):
    def setupUi(self, signUp):
        signUp.setObjectName("signUp")
        signUp.setFixedSize(400, 300)
        signUp.setWindowIcon(QIcon('chat.ico'))
        self.label_3 = QtWidgets.QLabel(signUp)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 55, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(signUp)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 55, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.password_lineEdit = QtWidgets.QLineEdit(signUp)
        self.password_lineEdit.setGeometry(QtCore.QRect(110, 150, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.label = QtWidgets.QLabel(signUp)
        self.label.setGeometry(QtCore.QRect(120, 30, 161, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.uname_lineEdit = QtWidgets.QLineEdit(signUp)
        self.uname_lineEdit.setGeometry(QtCore.QRect(110, 100, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.uname_lineEdit.setFont(font)
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.label_4 = QtWidgets.QLabel(signUp)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setLineWidth(-1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.signup_btn = QtWidgets.QPushButton(signUp)
        self.signup_btn.setGeometry(QtCore.QRect(110, 220, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")

        self.retranslateUi(signUp)
        QtCore.QMetaObject.connectSlotsByName(signUp)

    def retranslateUi(self, signUp):
        _translate = QtCore.QCoreApplication.translate
        signUp.setWindowTitle(_translate("signUp", "regWindow"))
        self.label_3.setText(_translate("signUp", "password"))
        self.label_2.setText(_translate("signUp", "login"))
        self.label.setText(_translate("signUp", "Create account"))
        self.signup_btn.setText(_translate("signUp", "SignUp"))

class Dialog(QDialog):
    def __init__(self, s, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        self.parent = parent
        self.host = '127.0.0.1'
        self.port = 8080
        self.message = b'no'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.ui.signup_btn.clicked.connect(self.insert_data)
    def show_message_box(self,arg):
        _translate = QCoreApplication.translate
        self.ui.label_4.setText(_translate("MainWindow", arg))
        self.ui.label_4.setStyleSheet('color: red')
    def insert_data(self):
        username = self.ui.uname_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        if (not username) or (not password):
            self.ui.label_4.setGeometry(QRect(10, 70, 381, 20))
            self.show_message_box('Not all fields are filled in')
            return
        self.s.send(("reg " + " name: " + username + " password: " + password).encode('utf-8'))
        if "Зарегистрирован" in self.s.recv(1024).decode('utf-8').split():
            self.hide()
        else:
            self.ui.label_4.setGeometry(QRect(10, 70, 381, 20))
            self.show_message_box('This user already exists')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signUp = QtWidgets.QDialog()
    ui = Ui_signUp()
    ui.setupUi(signUp)
    signUp.show()
    sys.exit(app.exec_())
