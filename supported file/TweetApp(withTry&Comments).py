import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import gettweet

from tweetmodule import *


class TweetGUI(gettweet.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(TweetGUI, self).__init__()
        self.setupUi(self)

        self.btn.clicked.connect(lambda :self.DisplayonScreen())

    def DisplayonScreen(self):
        mytext = self.entername.toPlainText()    #entername is name of textedit in Qt

        print(mytext)
        #print(type(mytext))
        #demo2 = demo()  # this is demo to test that i can access class n method of imported module like this
        #print(type(demo2.demofun()))

        #z=main()
        #print(z)

        self.displaytweet.setPlainText(myfun(mytext))  #displaytweet is name of another textedit in Qt






if __name__ == '__main__':

    tweetapp = QtWidgets.QApplication(sys.argv)
    Tweet = TweetGUI()
    Tweet.show()
    tweetapp.exec()






