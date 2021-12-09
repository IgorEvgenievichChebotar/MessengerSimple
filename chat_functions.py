import pickle
import socket
import sqlite3
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import *

from chat_window import Ui_MainWindow


class messenger_(QMainWindow):
    def __init__(self, username, parent=None):
        super(messenger_, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = sqlite3.connect("messages.db", check_same_thread=False)
        self.c = self.con.cursor()
        self.username = username
        self.host = '127.0.0.1'
        self.port = 60005
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.s.send(("name: " + self.username).encode('utf-8'))
        self.ui.pushButton_2.setMaximumSize(100, 100)
        self.ui.label_2.setText(self.username)
        self.thread = threading.Thread(target=self.find)
        self.thread.start()
        self.handler()
        self.thread_1 = threading.Thread(target=self.receive, args=(self.s, "a"))
        self.thread_1.start()
        self.ui.lineEdit.returnPressed.connect(self.clicked_but)
        self.ui.pushButton_2.clicked.connect(self.changeImage)

        f = open("path_avatarka.log", 'r')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f.read()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.pushButton_2.setIcon(icon)
        self.ui.pushButton_2.setIconSize(QtCore.QSize(100, 100))


    def changeImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print(fname)
        if fname:
            self.ui.pushButton_2.setStyleSheet("QPushButton{\n"
                                               "  display: block;\n"
                                               "  box-sizing: border-box;\n"
                                               "  margin: 0 auto;\n"
                                               "  padding: 8px;\n"
                                               "  width: 80%;\n"
                                               "  max-width: 200px;\n"
                                               "  background: #fff; /* запасной цвет для старых браузеров */\n"
                                               "  background: rgba(255, 255, 255,0);\n"
                                               "  border-radius: 8px;\n"
                                               "  color: #fff;\n"
                                               "  text-align: center;\n"
                                               "  text-decoration: none;\n"
                                               "  letter-spacing: 1px;\n"
                                               "  transition: all 0.3s ease-out;\n"
                                               "}")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(fname), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_2.setIcon(icon)
            self.ui.pushButton_2.setIconSize(QtCore.QSize(100, 100))
            f = open("path_avatarka.log", 'w')
            f.write(fname)
            f.close()
        else:
            f = open("path_avatarka.log", 'r')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f.read()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pushButton_2.setIcon(icon)
            self.ui.pushButton_2.setIconSize(QtCore.QSize(100, 100))

    def handler(self):
        self.ui.pushButton.clicked.connect(self.clicked_but)

    def receive(self, s, a):
        while True:
            self.data = self.s.recv(40960000)
            data = pickle.loads(self.data)
            print(data)
            sender = data["sender:"]
            message_ = data['message:']
            image_data = data["image:"]
            self.c.execute("""CREATE TABLE IF NOT EXISTS """ + '"' + sender + '"' + """(sender TEXT, message TEXT)""")
            self.c.execute("""INSERT INTO""" + '"' + sender + '"' + """VALUES (?,?)""", (sender, message_,))
            self.con.commit()
            print("sender", sender, message_)
            # self.ui.listWidget.setIconSize(QtCore.QSize(60, 60))
            # _translate = QtCore.QCoreApplication.translate
            if self.ui.listWidget.count() > 0:
                for x in range(0, self.ui.listWidget.count()):
                    cur_item = (self.ui.listWidget.item(x))
                    print(str(cur_item.text()), str(sender))
                    if cur_item.text() == sender:
                        brush = QtGui.QBrush(QtGui.QColor(166, 226, 43))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        cur_item.setBackground(brush)
                        print(cur_item.text())
                        break
                else:
                    print("No")
                    f = open(sender + ".png", 'wb')
                    f.write(image_data)
                    f.close()
                    item = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(sender + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item.setIcon(icon)
                    item.setText(sender)
                    self.ui.listWidget.addItem(item)
                    brush = QtGui.QBrush(QtGui.QColor(166, 226, 43))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    print(str(self.ui.listWidget.count()))
                    itemm = self.ui.listWidget.item(self.ui.listWidget.count() - 1)
                    print(str(itemm))
                    if itemm:
                        itemm.setBackground(brush)
                        print(str(itemm.text()))

            else:
                print("No")
                f = open(sender + ".png", 'wb')
                f.write(image_data)
                f.close()
                item = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(sender + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                item.setText(sender)
                self.ui.listWidget.addItem(item)
                brush = QtGui.QBrush(QtGui.QColor(166, 226, 43))
                brush.setStyle(QtCore.Qt.SolidPattern)
                itemm = self.ui.listWidget.item(0)
                itemm.setBackground(brush)
                print(itemm.text())
            # self.guest_message = str('Received from ' + sender +': '+ message_)
            # self.ui.plainTextEdit.appendPlainText(self.guest_message)

    def clicked_but(self):
        self.msg = self.ui.lineEdit.text().split()
        if self.msg:
            print(self.msg)
            self.message = self.msg[0:]
            self.message = ' '.join(self.message)
            add_msg = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.username + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            add_msg.setIcon(icon)
            add_msg.setText(self.message)
            self.ui.ListWidget.addItem(add_msg)
            #self.item = self.ui.listWidget.currentItem()
            if self.item:
                self.c.execute("""INSERT INTO""" + '"' + self.item + '"' + """VALUES (?,?)""",
                               (self.username, self.message,))
                self.con.commit()
                self.s.send(
                    ("sender: " + self.username + " receiver: " + self.item + " message: " + self.message).encode(
                        'utf-8'))
                self.ui.lineEdit.clear()
            else:
                print("нет получателя!")
        else:
            print("Пустое")

    def find(self):
        host = '127.0.0.1'
        port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.send(("name: " + self.username).encode('utf-8'))
        self.new_thread = threading.Thread(target=self.receiv)
        self.new_thread.start()
        self.line = self.ui.comboBox.lineEdit()
        self.ui.listWidget.itemClicked.connect(self.listview)
        self.line.returnPressed.connect(self.nado)

    def addInGroup(self, event):
        self.menu_1 = QMenu(self)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        for x in range(0, self.ui.listWidget.count()):
            action = self.menu_1.addAction(self.ui.listWidget.item(x).text())
        result = self.menu_1.exec_(self.mapToGlobal(event.pos()))

    def contextMenuEvent(self, event):
        self.menu = QMenu(self)
        action = self.menu.addAction("Add to friends")
        action_1 = self.menu.addAction("*Unassigned action*")
        result = self.menu.exec_(self.mapToGlobal(event.pos()))
        if action == result:
            self.addInGroup(event)
        elif action_1 == result:
            print("press")

    def nado(self):
        self.sock.send((self.line.text()).encode('utf-8'))
        print("send")
        self.ui.comboBox.hidePopup()
        self.ui.comboBox.clear()
        # self.ui.listWidget.takeItem(self.ui.listWidget.selectedItems()[0])
        self.ui.comboBox.activated.connect(self.pressedKeys)

    def get_key(self, d):
        for item in d.items():
            print(item[0], item[1])
            f = open(item[0] + ".png", 'wb')
            f.write(item[1])
            f.close()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(item[0] + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.comboBox.addItem(icon, item[0])

    def receiv(self):
        while True:
            self.dataa = self.sock.recv(40960000)  # .decode('utf-8').split(",")
            self.dataa = pickle.loads(self.dataa)
            print(self.dataa)
            if self.dataa:
                self.get_key((self.dataa))

    def pressedKeys(self):
        self.ui.listWidget.setIconSize(QtCore.QSize(40, 40))
        self.current_item = self.ui.comboBox.currentText()
        print(self.current_item)
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.current_item + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        item.setText(self.current_item)
        self.ui.listWidget.addItem(item)
        self.ui.comboBox.activated.disconnect(self.pressedKeys)

    def listview(self):
        self.ui.ListWidget.clear()
        brush = QtGui.QBrush(QtGui.QColor(255, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        itemm = self.ui.listWidget.currentItem()
        itemm.setBackground(brush)
        self.item = self.ui.listWidget.currentItem().text()
        self.c.execute("""CREATE TABLE IF NOT EXISTS """ + '"' + self.item + '"' + """(sender TEXT, message TEXT)""")
        self.c.execute("""SELECT * FROM """'"' + self.item + '"')
        f = self.c.fetchall()
        if f is not None:
            for x in range(0, len(f)):
                mess = f[x][1:]
                mess = ".".join(mess)
                add_msg = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f[x][0] + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                add_msg.setIcon(icon)
                add_msg.setText(mess)
                self.ui.ListWidget.setIconSize(QtCore.QSize(40, 40))
                self.ui.ListWidget.addItem(add_msg)
        print(self.item)

    def closeEvent(self, event):
        self.hide()
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = messenger_()
    w.show()
    sys.exit(app.exec_())