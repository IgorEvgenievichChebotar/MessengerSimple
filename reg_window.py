from PyQt5 import QtCore, QtGui, QtWidgets  # importing lib
from PyQt5.Qt import *  # importing lib
from PyQt5.QtCore import *  # importing lib
from PyQt5.QtGui import QIcon  # importing lib


class Ui_signUp(object):  # ui class
    def setupUi(self, signUp):  # ui class method
        signUp.setObjectName("signUp")
        signUp.setFixedSize(400, 300)
        signUp.setWindowIcon(QIcon('chat.ico'))
        self.signUp_password_label = QtWidgets.QLabel(signUp)
        self.signUp_password_label.setGeometry(QtCore.QRect(40, 160, 55, 20))
        self.signUp_password_label.setFont(QtGui.QFont("Segoe UI Variable"))
        self.signUp_password_label.setObjectName("label_3")
        self.signUp_login_label = QtWidgets.QLabel(signUp)
        self.signUp_login_label.setGeometry(QtCore.QRect(50, 110, 55, 20))
        self.signUp_login_label.setFont(QtGui.QFont("Segoe UI Variable"))
        self.signUp_login_label.setObjectName("label_2")
        self.signUp_password_lineEdit = QtWidgets.QLineEdit(signUp)
        self.signUp_password_lineEdit.setGeometry(QtCore.QRect(110, 150, 181, 35))
        self.signUp_password_lineEdit.setFont(QtGui.QFont("Segoe UI Variable"))
        self.signUp_password_lineEdit.setObjectName("password_lineEdit")
        self.signUp_label_creatAcc = QtWidgets.QLabel(signUp)
        self.signUp_label_creatAcc.setGeometry(QtCore.QRect(120, 30, 161, 35))
        self.signUp_label_creatAcc.setFont(QtGui.QFont("Segoe UI Variable",14))
        self.signUp_label_creatAcc.setObjectName("label")
        self.signUp_login_lineEdit = QtWidgets.QLineEdit(signUp)
        self.signUp_login_lineEdit.setGeometry(QtCore.QRect(110, 100, 181, 35))
        self.signUp_login_lineEdit.setFont(QtGui.QFont("Segoe UI Variable"))
        self.signUp_login_lineEdit.setObjectName("uname_lineEdit")
        self.message_box_label = QtWidgets.QLabel(signUp)
        self.message_box_label.setGeometry(QtCore.QRect(10, 70, 381, 20))
        self.message_box_label.setFont(QtGui.QFont("Segoe UI Variable"))
        self.message_box_label.setAutoFillBackground(False)
        self.message_box_label.setLineWidth(-1)
        self.message_box_label.setMidLineWidth(0)
        self.message_box_label.setText("")
        self.message_box_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_box_label.setObjectName("label_4")
        self.signUp_btn_reg = QtWidgets.QPushButton(signUp)
        self.signUp_btn_reg.setGeometry(QtCore.QRect(110, 220, 181, 50))
        self.signUp_btn_reg.setFont(QtGui.QFont("Segoe UI Variable"))
        self.signUp_btn_reg.setObjectName("signup_btn")

        self.retranslateUi(signUp)
        QtCore.QMetaObject.connectSlotsByName(signUp)

    def retranslateUi(self, signUp):  # ui class method
        _translate = QtCore.QCoreApplication.translate
        signUp.setWindowTitle(_translate("signUp", "regWindow"))
        self.signUp_password_label.setText(_translate("signUp", "password"))
        self.signUp_login_label.setText(_translate("signUp", "login"))
        self.signUp_label_creatAcc.setText(_translate("signUp", "Create account"))
        self.signUp_btn_reg.setText(_translate("signUp", "SignUp"))

class Dialog(QDialog):  # this class works with ui
    def __init__(self, s, parent=None):  # constructor
        super(Dialog, self).__init__(parent)
        self.ui = Ui_signUp()
        self.ui.setupUi(self)
        self.parent = parent
        self.message = b'no'
        self.s = s
        self.ui.signUp_btn_reg.clicked.connect(self.insert_data)
    def show_message_box(self,arg):  # shows a message when incorrect input
        _translate = QCoreApplication.translate
        self.ui.message_box_label.setText(_translate("MainWindow", arg))
        self.ui.message_box_label.setStyleSheet('color: red')
    def insert_data(self):  # works with user's input
        username = self.ui.signUp_login_lineEdit.text()
        password = self.ui.signUp_password_lineEdit.text()
        if (not username) or (not password):
            self.ui.message_box_label.setGeometry(QRect(10, 70, 381, 20))
            self.show_message_box('Not all fields are filled in')
            return
        self.s.send(("reg " + " name: " + username + " password: " + password).encode('utf-8'))
        if "Зарегистрирован" in self.s.recv(1024).decode('utf-8').split():
            self.hide()
        else:
            self.ui.message_box_label.setGeometry(QRect(10, 70, 381, 20))
            self.show_message_box('This user already exists')

if __name__ == "__main__":  # that protects users from accidentally invoking the script
    import sys  # importing lib
    app = QtWidgets.QApplication(sys.argv)
    signUp = QtWidgets.QDialog()
    ui = Ui_signUp()
    ui.setupUi(signUp)
    signUp.show()
    sys.exit(app.exec_())
