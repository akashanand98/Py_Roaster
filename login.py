# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'login.ui'
# Created by: PyQt5 UI code generator 5.9.2
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cal_employee import Ui_EmployeeUI

class Ui_MyRoaster(object):
    
        
    def setupUi(self, MyRoaster):
        MyRoaster.setObjectName("MyRoaster")
        MyRoaster.resize(450, 500)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        MyRoaster.setFont(font)
        MyRoaster.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MyRoaster.setMouseTracking(True)
        MyRoaster.setTabletTracking(False)
        MyRoaster.setFocusPolicy(QtCore.Qt.ClickFocus)
        MyRoaster.setAutoFillBackground(False)
        MyRoaster.setStyleSheet("background-color: rgb(35, 35, 35);")
        MyRoaster.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MyRoaster)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 200, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setMouseTracking(False)
        #self.lineEdit_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_5.setStyleSheet("QLineEdit{color:#FFF;border-radius: 15px;border:1px solid rgb(255,255,255);}QLineEdit:hover{border:2px solid rgb(255,255,255);background-color: rgb(50, 50, 50);}\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 240, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setMouseTracking(False)
        #self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setStyleSheet("QLineEdit{color:#FFF;border-radius: 15px;border:1px solid rgb(255,255,255);}QLineEdit:hover{border:2px solid rgb(255,255,255);background-color: rgb(50, 50, 50);}\n"
"")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 99, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(33)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FFF;background-color: rgb(255, 34, 93);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);border-radius: 8px;}QPushButton:hover{border:2px solid rgb(255,255,0);}\n"
"    ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 350, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);border-radius: 8px;}QPushButton:hover{border:2px solid rgb(255,255,0);}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MyRoaster.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyRoaster)
        QtCore.QMetaObject.connectSlotsByName(MyRoaster)
        
    def validate(self):
        username=self.lineEdit_5.text().strip()
        password=self.lineEdit_4.text().strip()
        flag=0
        value =''
        try:
            f = open("Employee_det.csv", "r",encoding = 'utf-8')
            next(f)             #skip header row
            for line in f:
                line_split=line.split(",")
                
                if((line_split[1] == username) or line_split[3] == username and line_split[2] == password):
                    if(line_split[4] == "Manager"):
                        flag=1
                    elif(line_split[4] == "Teammate"):
                        flag=-1
                    value = line_split
                    
                    break
            
            if(flag==-1):
                print("Team Mate")
                self.value=value
                MyRoaster.close()
                self.EmployeeUI = QtWidgets.QMainWindow()
                self.ui = Ui_EmployeeUI(self.value)
                self.ui.setupUi(self.EmployeeUI)
                self.EmployeeUI.show()
            elif(flag==1):    
                print("Manager")
            else:
                print("Invalid User")
            
        except (IOError, ValueError, EOFError) as e:
            print(e)
        finally:
            f.close()
    
       
    
    def retranslateUi(self, MyRoaster):
        _translate = QtCore.QCoreApplication.translate
        MyRoaster.setWindowTitle(_translate("MyRoaster", "MainWindow"))
        self.lineEdit_5.setPlaceholderText(_translate("MyRoaster", "Username"))
        self.lineEdit_4.setPlaceholderText(_translate("MyRoaster", "Password"))
        self.label.setText(_translate("MyRoaster", "My Roaster"))
        self.pushButton.setText(_translate("MyRoaster", "Login"))
        self.pushButton.clicked.connect(self.validate)
        self.pushButton_2.setText(_translate("MyRoaster", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyRoaster = QtWidgets.QMainWindow()
    ui = Ui_MyRoaster()
    ui.setupUi(MyRoaster)
    MyRoaster.show()
    

    sys.exit(app.exec_())

