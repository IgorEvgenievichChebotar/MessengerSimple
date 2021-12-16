import pickle  # importing lib
import socket  # importing lib
import sqlite3  # importing lib
import threading  # importing lib
import pathlib  # importing lib

from PyQt5 import QtCore, QtGui, QtWidgets  # importing lib
from PyQt5.Qt import *  # importing lib
from PyQt5.QtWidgets import *  # importing lib
from colorama import init, Fore  # importing lib

init(autoreset=True)  # set colorama lib condition

from chat_window import Ui_chatWindow  # importing ui class


class messenger_(QMainWindow):  # main class
    def __init__(self, username, parent=None):  # constructor
        super(messenger_, self).__init__(parent)  # connecting parent class

        self.ui = Ui_chatWindow()  # connecting class
        self.ui.setupUi(self)  # ui initialization
        self.con = sqlite3.connect("messages.db", check_same_thread=False, timeout=1)  # connecting db1
        self.con2 = sqlite3.connect(pathlib.Path.cwd().joinpath('servers').joinpath('data.db'),
                                    check_same_thread=False, timeout=1)  # connecting db2
        self.con.execute("PRAGMA journal_mode=WAL")  # condition for db1
        self.con2.execute("PRAGMA journal_mode=WAL")  # condition for db2
        self.c = self.con.cursor()  # creating cursor for db1
        self.c2 = self.con2.cursor()  # creating cursor for db2
        self.username = username  # assignment
        self.host = '127.0.0.1'  # creating host
        self.port = 60005  # creating port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a TCP/IP socket
        self.s.connect((self.host, self.port))  # connecting socket to the server
        self.s.send(("name: " + self.username).encode('utf-8'))
        self.ui.my_image.setMaximumSize(100, 100)
        self.ui.my_login_label.setText(self.username)
        self.thread = threading.Thread(target=self.find)  # creating thread
        self.thread.start()  # starting thread
        self.handler()
        self.thread_1 = threading.Thread(target=self.receive_messages)  # creating thread
        self.thread_1.start()  # starting thread
        self.ui.msg_lineEdit.returnPressed.connect(self.send_message)
        self.ui.my_image.clicked.connect(self.change_image)

        path_file = open("path_avatarka.log", 'r')
        image_dir = path_file.read()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.my_image.setIcon(icon)
        self.ui.my_image.setIconSize(QtCore.QSize(100, 100))

        self.update_friends_list()

    def set_image(self, user_name):
        print("the _set_image_ function has now started working")
        

    def change_image(self):  # method for changing avatar
        print("the _change_image_ function has now started working")
        image_dir = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print(image_dir)
        if image_dir:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.my_image.setIcon(icon)
            self.ui.my_image.setIconSize(QtCore.QSize(100, 100))
            f = open("path_avatarka.log", 'w')
            f.write(image_dir)
            f.close()
        else:
            f = open("path_avatarka.log", 'r')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(f.read()), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.my_image.setIcon(icon)
            self.ui.my_image.setIconSize(QtCore.QSize(100, 100))

    def handler(self):  # method for handle click
        print("the _handler_ function has now started working")
        self.ui.send_msg_btn.clicked.connect(self.send_message)       

    def send_message(self):  # method for save message to database
        print("the _send_message_ function has now started working")
        self.msg = self.ui.msg_lineEdit.text().split()
        if self.msg:
            print(self.msg)
            self.message = self.msg[0:]
            self.message = ' '.join(self.message)
            add_msg = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.username + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            add_msg.setIcon(icon)
            add_msg.setText(self.message)
            self.ui.msg_list.addItem(add_msg)
            # self.item = self.ui.friends_list.currentItem()
            if self.item:
                self.c.execute("""INSERT INTO""" + '"' + self.item + '"' + """VALUES (?,?)""",
                               (self.username, self.message,))
                self.con.commit()
                self.s.send(
                    ("sender: " + self.username + " receiver: " + self.item + " message: " + self.message).encode(
                        'utf-8'))
                self.ui.msg_lineEdit.clear()
            else:
                print("no receiver")
        else:
            print("empty field")

    def find(self):  # method for send data to server
        print("the _find_ function has now started working")
        host = '127.0.0.1'
        port = 8888
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.send(("name: " + self.username).encode('utf-8'))
        self.new_thread = threading.Thread(target=self.receive_friend)
        self.new_thread.start()
        self.line = self.ui.friends_comboBox.lineEdit()

        self.ui.friends_list.itemClicked.connect(self.update_messages_list)

        self.line.returnPressed.connect(self.combobox_process)

    def combobox_process(self):  # method for processing friends_comboBox button
        print("the _combobox_process_ function has now started working")
        self.sock.send((self.line.text()).encode('utf-8'))
        self.ui.friends_comboBox.hidePopup()
        self.ui.friends_comboBox.clear()
        # self.ui.friends_list.takeItem(self.ui.friends_list.selectedItems()[0])
        self.ui.friends_comboBox.activated.connect(self.pressed_keys)
        self.ui.find_friends_btn.clicked.connect(self.pressed_keys)

    def get_key(self, d):  # method for catching click
        print("the _get_key_ function has now started working")
        for item in d.items():
            f = open(item[0] + ".png", 'wb')
            f.write(item[1])
            f.close()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(item[0] + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.friends_comboBox.addItem(icon, item[0])
            
    def receive_messages(self):  # method for waiting response from the server
        print("the _receive_messages_ function has now started working")
        while True:
            self.data = self.s.recv(40960000)
            data = pickle.loads(self.data)
            print("receive_messages_data = ", data)
            sender = data["sender:"]
            message_ = data['message:']
            image_data = data["image:"]
            self.c.execute("""CREATE TABLE IF NOT EXISTS """ + '"' + sender + '"' + """(sender TEXT, message TEXT)""")
            self.c.execute("""INSERT INTO""" + '"' + sender + '"' + """VALUES (?,?)""", (sender, message_,))
            self.con.commit()
            print("sender", sender, message_)
            # self.ui.friends_list.setIconSize(QtCore.QSize(60, 60))
            # _translate = QtCore.QCoreApplication.translate
            if self.ui.friends_list.count() > 0:
                for x in range(0, self.ui.friends_list.count()):
                    cur_item = (self.ui.friends_list.item(x))
                    print(str(cur_item.text()), str(sender))
                    if cur_item.text() == sender:
                        brush = QtGui.QBrush(QtGui.QColor(32, 178, 170))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        cur_item.setBackground(brush)
                        print(sender, cur_item.text())
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
                    self.ui.friends_list.addItem(item)
                    brush = QtGui.QBrush(QtGui.QColor(166, 226, 43))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    print(str(self.ui.friends_list.count()))
                    itemm = self.ui.friends_list.item(self.ui.friends_list.count() - 1)
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
                self.ui.friends_list.addItem(item)
                brush = QtGui.QBrush(QtGui.QColor(166, 226, 43))
                brush.setStyle(QtCore.Qt.SolidPattern)
                itemm = self.ui.friends_list.item(0)
                itemm.setBackground(brush)
                print(itemm.text())
            # self.guest_message = str('received from ' + sender +': '+ message_)
            # self.ui.plainTextEdit.appendPlainText(self.guest_message)

    def receive_friend(self):  # method for waiting response from the server
        print("the _receive_friend_ function has now started working")
        while True:
            self.data2 = self.sock.recv(40960000)  # .decode('utf-8').split(",")
            data = pickle.loads(self.data2)
            if data:
                print("receive_friend_data = ", data)
                self.get_key((data))

    def pressed_keys(self):  # method for processing click
        print("the _pressed_keys_ function has now started working")

        friend_name = self.ui.friends_comboBox.currentText()

        self.add_friend(friend_name)

        self.ui.friends_comboBox.activated.disconnect(self.pressed_keys)
        self.ui.find_friends_btn.clicked.disconnect(self.pressed_keys)

    def update_messages_list(self):  # method for show list of messages
        print("the _update_messages_list_ function has now started working")
        self.ui.msg_list.clear()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        itemm = self.ui.friends_list.currentItem()
        itemm.setBackground(brush)
        self.item = self.ui.friends_list.currentItem().text()
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
                self.ui.msg_list.addItem(add_msg)
        self.update_profile_info()

    def update_profile_info(self):  # method for show profile information
        print("the _update_profile_info_ function has now started working")

        # avatar
        self.ui.friend_image.setEnabled(True)
        path_file = open("path_avatarka.log", 'r')
        image_dir = path_file.read()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(image_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.friend_image.setIcon(icon)
        self.ui.friend_image.setIconSize(QtCore.QSize(100, 100))

        # status and name
        self.c2.execute("SELECT name FROM base_connection WHERE name = ?", (self.item,))
        name = self.c2.fetchone()
        if name is not None:
            self.ui.friend_login_label.setText(self.item)
            print(self.item, "online")
            self.ui.friend_activity.setText("online")
            self.ui.friend_activity.setStyleSheet('color: green')
        else:
            self.ui.friend_login_label.setText(self.item)
            print(self.item, "offline")
            self.ui.friend_activity.setText("offline")
            self.ui.friend_activity.setStyleSheet('color: red')

    def clear_profile_info(self):
        print("the _clear_profile_info_ function has now started working")
        self.ui.friend_login_label.setText("")
        self.ui.friend_activity.setText("")
        self.ui.friend_image.setIcon(QIcon())
        self.ui.friend_image.setEnabled(False)

    def clear_messages_list(self):
        print("the _clear_messages_list_ function has now started working")
        self.ui.msg_list.clear()
        
    def clear_friends_list(self):
        print("the _clear_friends_list_ function has now started working")
        self.ui.friends_list.clear()

    def update_friends_list(self):  # method for showing friends list
        print("the _update_friends_list_ function has now started working")
        self.clear_friends_list()
        self.c2.execute("""CREATE TABLE IF NOT EXISTS friends(
                      user TEXT,
                      his_friend TEXT);
                   """)
        self.con2.commit()
        self.c2.execute("SELECT user FROM friends Where user = ? ", (self.username,))
        entry = self.c2.fetchone()
        if entry is None:
            print(Fore.BLUE + "the string in friends is empty")
        else:
            print(Fore.GREEN + "the string in friends were founded")
            self.c2.execute("SELECT user, his_friend FROM friends Where user = ? ", (self.username,))
            lines = self.c2.fetchall()
            print("number of friends : ", len(lines))
            for line in lines:
                friend_name = line[1]
                self.add_friend(friend_name)

    def add_friend(self, friend_name):  # method for adding friend to database
        print("the _add_friend_ function has now started working")
        self.add_friend_item(friend_name)
        self.c2.execute("SELECT user FROM friends Where user = ? ", (self.username,))
        entry = self.c2.fetchone()
        if entry is None:
            self.c2.execute("INSERT INTO friends VALUES(?, ?);", (self.username, friend_name))
            self.con2.commit()
            print(Fore.BLUE + "the string in friends WAS CREATED")
        else:
            self.c2.execute("SELECT user, his_friend FROM friends")
            lines = self.c2.fetchall()
            if (self.username, friend_name) in lines:
                print(Fore.GREEN + "the string in friends were founded")
            else:
                print(Fore.BLUE + "the string in friends WAS CREATED")
                self.c2.execute("INSERT INTO friends VALUES(?, ?);", (self.username, friend_name))
                self.con2.commit()

    def add_friend_item(self, friend_name):  # method for adding friend item
        print("the _add_friend_item_ function has now started working")
        self.ui.friends_list.setIconSize(QtCore.QSize(40, 40))
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(friend_name + ".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        item.setText(friend_name)
        self.ui.friends_list.addItem(item)

    def delete_friend(self, friend_name):  # method for deleting friend from database
        print("the _delete_friend_ function has now started working")
        print("delete ", friend_name)
        self.c2.execute("DELETE FROM friends Where his_friend = ? ", (friend_name,))
        self.con2.commit()

        self.update_friends_list()
        self.clear_profile_info()
        self.clear_messages_list()

    def contextMenuEvent(self, event):  # method is called when mouse right click was caught
        print("the _contextMenuEvent_ function has now started working")
        menu = QMenu(self)
        del_friend = menu.addAction("Delete friend")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == del_friend:
            try:
                friend_name = self.ui.friends_list.currentItem().text()
                self.delete_friend(friend_name)
                self.clear_profile_info()
            except:
                print("friend not selected")

    def closeEvent(self, event):  # method is called when the program closing
        print("the _closeEvent_ function has now started working")
        self.hide()
        sys.exit(0)


if __name__ == "__main__":  # that protects users from accidentally invoking the script
    import sys

    app = QApplication(sys.argv)
    w = messenger_()
    w.show()
    sys.exit(app.exec_())