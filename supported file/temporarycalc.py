import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import calc



class Calculator(calc.Ui_MainWindow, QtWidgets.QMainWindow):
        def __init__(self):
            super(Calculator,self).__init__()
            self.setupUi(self)
            #self.DisplayOnScreen('sdfdsf')
            self.bt_0.clicked.connect(lambda :self.DisplayOnScreen('0'))  # lambda should be used, boz u r giving argument '0' in function which is also being passed in some other function
            self.bt_1.clicked.connect(lambda: self.DisplayOnScreen('1'))
            self.bt_2.clicked.connect(lambda: self.DisplayOnScreen('2'))
            self.bt_3.clicked.connect(lambda: self.DisplayOnScreen('3'))
            self.bt_4.clicked.connect(lambda: self.DisplayOnScreen('4'))
            self.bt_5.clicked.connect(lambda: self.DisplayOnScreen('5'))
            self.bt_6.clicked.connect(lambda: self.DisplayOnScreen('6'))
            self.bt_7.clicked.connect(lambda: self.DisplayOnScreen('7'))
            self.bt_8.clicked.connect(lambda: self.DisplayOnScreen('8'))
            self.bt_9.clicked.connect(lambda: self.DisplayOnScreen('9'))
            self.bt_dot.clicked.connect(lambda: self.DisplayOnScreen('.'))
            self.bt_clear.clicked.connect(lambda :self.screen.clear())
            self.bt_back.clicked.connect(lambda :self.screen.backspace())

            self.bt_plus.clicked.connect(lambda: self.DisplayOnScreen(' + '))
            self.bt_minus.clicked.connect(lambda: self.DisplayOnScreen(' - '))
            self.bt_mul.clicked.connect(lambda: self.DisplayOnScreen(' * '))
            self.bt_div.clicked.connect(lambda: self.DisplayOnScreen(' / '))

            self.bt_eq.clicked.connect( lambda :self.calculations())  # when u press eq btn then it will go to func calculations
            self.screen.setReadOnly(True)  # will not allow user to enter value from keyboard, it helps to prevent app from invalid entries from user


        def DisplayOnScreen(self,value):   # this func adds value to line edit
            self.screen.insert(value)   # screen is name given to Line Edit in QtDesigner



        def  calculations(self):   # this func gets vlaue from screen n get it for calculation to mathoperations function n finally disply o/p on screen
            screen_value=str(self.screen.text()).split(' ')  # getting screen value for calculations
            #converting screen input into string elements with list n split by space
            #print(screen_value)
            #x=screen_value.split(' ')

            a=float(screen_value[0])
            operator=screen_value[1]
            b=float(screen_value[2])

            result=self.mathoperations(a,b,operator) #To print result after operations
            #print(result)
            self.screen.setText(str(result))
            # while displaying result into screen insert method doesnt work so i have to use setText method which take string input only that is  why i cant  here use DisplayOnScreen func


        def mathoperations(self,a,b,operator):

            if operator=='+':
                return a+b
            elif operator=='-':
                return a-b
            elif operator=='*':
                return a*b
            elif operator=='/':
                if b==0:
                    return 'Invalid Operation:DivideByZero Error'
                else:
                    return a/b


if __name__ == '__main__':
        calcapp= QtWidgets.QApplication(sys.argv)
        calc= Calculator()
        calc.show()
        calcapp.exec()








