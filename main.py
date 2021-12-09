import socket
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from auth_window import Ui_authWindow
from reg_window import Dialog
from chat_functions import messenger_


class MainDialog(QMainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.ui = Ui_authWindow()
        self.ui.setupUi(self)
        self.host = '127.0.0.1'
        self.port = 8080
        self.message = b'no'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a TCP/IP socket
        self.s.connect((self.host, self.port))  # connecting socket to the server
        self.ui.Button_login.clicked.connect(self.loginCheck)
        self.ui.Button_registr.clicked.connect(self.signUpCheck)

    def showMessageBox(self, arg):  # notification in red text about incorrect input
        _translate = QCoreApplication.translate
        self.ui.label_4.setText(_translate("MainWindow", arg))
        self.ui.label_4.setStyleSheet('color: red')

    def welcomeWindowShow(self, username):  # opening the chat window
        self.main_window = messenger_(self.username)
        self.main_window.show()

    def signUpShow(self):  # opening the auth window
        self.signUpWindow = Dialog(self.s)
        self.signUpWindow.show()

    def signUpCheck(self):  # processing the signUp button
        print("signed up")
        self.signUpShow()

    def loginCheck(self):  # input validation and input processing (processing the signIn button)
        print("signed in")
        self.username = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()

        if (not self.username) or (not self.password):
            self.showMessageBox("Not all fields are filled in")
            return
        else:
            print(self.username + " " + self.password)
        self.s.send(("log" + " login: " + self.username + " password: " + self.password).encode('utf-8'))
        self.data = self.s.recv(1024).decode('utf-8').split()
        print(self.data)
        if "выполнен" in self.data:
            self.welcomeWindowShow(self.username)
            self.hide()
            self.s.close()
        elif "существует" in self.data:
            self.showMessageBox('There is no such user')
        elif "неверен" in self.data:
            self.showMessageBox('Incorrect password')
        else:
            self.showMessageBox('Unknown error')


def main():
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
