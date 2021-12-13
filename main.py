import socket  # importing lib
import sys  # importing lib

from PyQt5.QtCore import *  # importing lib
from PyQt5.QtWidgets import *  # importing lib

from auth_window import Ui_authWindow  # importing ui class
from reg_window import Dialog  # importing ui+func class
from chat_functions import messenger_  # importing ui+func class


class MainDialog(QMainWindow):  # main class
    def __init__(self, parent=None):  # constructor
        super(MainDialog, self).__init__(parent)  # connecting parent class
        self.ui = Ui_authWindow()  # connecting class
        self.ui.setupUi(self)  # ui initialization
        self.host = '127.0.0.1'  # creating host
        self.port = 8080  # creating port
        self.message = b'no'  # signal message
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a TCP/IP socket
        self.s.connect((self.host, self.port))  # connecting socket to the server
        self.ui.Button_login.clicked.connect(self.login_check)  # signIn button click processing
        self.ui.Button_registr.clicked.connect(self.sign_up_check)  # signUp button click processing

    def show_message_box(self, arg):  # notification in red text about incorrect input
        print("the _show_message_box_ function has now started working")
        _translate = QCoreApplication.translate
        self.ui.label_4.setText(_translate("MainWindow", arg))
        self.ui.label_4.setStyleSheet('color: red')

    def chat_window_show(self, username):  # opening the chat window
        print("the _chat_window_show_ function has now started working")
        self.main_window = messenger_(self.username)
        self.main_window.show()

    def reg_window_show(self):  # opening the auth window
        print("the _reg_window_show_ function has now started working")
        self.sign_up_window = Dialog(self.s)
        self.sign_up_window.show()

    def sign_up_check(self):  # processing the signUp button
        print("the _sign_up_check_ function has now started working")
        self.reg_window_show()

    def login_check(self):  # input validation and input processing (processing the signIn button)
        print("the _login_check_ function has now started working")
        self.username = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        if (not self.username) or (not self.password):
            self.show_message_box("Not all fields are filled in")
            return
        else:
            print(self.username + " " + self.password)
        self.s.send(("log" + " login: " + self.username + " password: " + self.password).encode('utf-8'))
        self.data = self.s.recv(1024).decode('utf-8').split()
        if "выполнен" in self.data:
            print("signed in")
            self.chat_window_show(self.username)
            self.hide()
            self.s.close()
        elif "существует" in self.data:
            self.show_message_box('There is no such user')
        elif "неверен" in self.data:
            self.show_message_box('Incorrect password')
        else:
            self.show_message_box('Unknown error')


def main():  # main function
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    app.exec_()


if __name__ == '__main__':  # starts main() if the file in which it is located is active
    main()
