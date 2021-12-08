from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setWindowIcon(QIcon('chat.ico'))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.label_2.setFont(font)
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.listWidget.setFont(font)
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.comboBox.setFont(font)
        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.ListWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gridLayout_4.addWidget(self.ListWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable")
        self.pushButton.setFont(font)
        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "chatWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

        self.pushButton.setText(_translate("MainWindow", "Send message"))