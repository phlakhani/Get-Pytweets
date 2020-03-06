# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gettweet2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(450, 350))
        MainWindow.setBaseSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setStyleSheet("background-color: rgb(204, 225, 222);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.btn_frame = QtWidgets.QFrame(self.MainFrame)
        self.btn_frame.setGeometry(QtCore.QRect(20, 50, 391, 80))
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.entername = QtWidgets.QTextEdit(self.btn_frame)
        self.entername.setGeometry(QtCore.QRect(13, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.entername.setFont(font)
        self.entername.setStyleSheet("background-color: rgb(236, 255, 19);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.entername.setObjectName("entername")
        self.btn = QtWidgets.QPushButton(self.btn_frame)
        self.btn.setGeometry(QtCore.QRect(300, 10, 81, 61))
        self.btn.setStyleSheet("background-color: rgb(255, 196, 255);")
        self.btn.setObjectName("btn")
        self.frame_3 = QtWidgets.QFrame(self.MainFrame)
        self.frame_3.setGeometry(QtCore.QRect(20, 130, 391, 171))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.displaytweet = QtWidgets.QTextEdit(self.frame_3)
        self.displaytweet.setGeometry(QtCore.QRect(10, 10, 371, 151))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.displaytweet.setFont(font)
        self.displaytweet.setStyleSheet("background-color: rgb(155, 245, 255);\n"
"background-color: rgb(69, 181, 241);")
        self.displaytweet.setObjectName("displaytweet")
        self.horizontalLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GetTweets"))
        self.btn.setText(_translate("MainWindow", "GetTweets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
