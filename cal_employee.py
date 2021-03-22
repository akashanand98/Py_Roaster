# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dell\Desktop\UI\cal_employee.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import pandas as pd
from datetime import date, timedelta,datetime
#from login import Ui_MyRoaster


class Ui_EmployeeUI(object):
    
    def __init__(self,value):
        if value=="":
            print ("empty")
        else:
            self.uname=value[0]
            print ("user name is :"+value[0])
        
        
        
        
        
    def setupUi(self, EmployeeUI):
        EmployeeUI.setObjectName("EmployeeUI")
        EmployeeUI.resize(800, 600)
        EmployeeUI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(EmployeeUI)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(150, 40, 631, 401))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.calendarWidget.setFont(font)

        
        

        
        format = QTextCharFormat() 
        format.setBackground(QtGui.QColor("yellow"))

        format_l = QTextCharFormat() 
        format_l.setBackground(QtGui.QColor("#52bdff"))
        
        df = pd.read_csv('holiday.csv')
        linfo=pd.read_csv('leave_info.csv')
        s_date=datetime.strptime(linfo.iloc[0]['start_date'], '%d-%m-%Y').strftime('%Y-%m-%d')
        e_date=datetime.strptime(linfo.iloc[0]['end_date'], '%d-%m-%Y').strftime('%Y-%m-%d')
        leave_dates=pd.date_range(s_date,e_date,freq='d')
        

        for d in leave_dates:
            myPythonicDate=d.strftime("%d-%m-%Y")
            qtDate = QtCore.QDate.fromString(myPythonicDate, 'dd-MM-yyyy')
            self.calendarWidget.setDateTextFormat(qtDate, format_l)
        
        h_dates=df['Holiday_date']
        h_des=df['Holiday_description']
        
        for i in h_dates:
            myPythonicDate=i
            qtDate = QtCore.QDate.fromString(myPythonicDate, 'dd-MM-yyyy')
            self.calendarWidget.setDateTextFormat(qtDate, format)
        
        self.calendarWidget.setStyleSheet("background-color: rgb(210, 246, 255);\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(25, 10, 500, 20))
        #label_info --> display login info
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 101, 581))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 71, 51))
        self.pushButton.setStyleSheet("QPushButton{image: url(:/newPrefix/home.png);\n"
"background-color:rgb(0,0,0);}\n"
"\n"
"QPushButton:hover{\n"
"border:1px solid rgb(85, 255, 0);\n"
"border-radius:10px\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 71, 51))
        self.pushButton_2.setStyleSheet("QPushButton{image: url(:/newPrefix/leave.png);\n"
"background-color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border:1px solid rgb(85, 255, 0);\n"
"border-radius:10px\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 370, 71, 51))
        self.pushButton_3.setStyleSheet("QPushButton{image: url(:/newPrefix/emp_det.png);\n"
"background-color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border:1px solid rgb(85, 255, 0);\n"
"border-radius:10px\n"
"}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 470, 31, 31))
        self.label_3.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(0, 255, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 470, 31, 31))
        self.label_4.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 0);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 470, 31, 31))
        self.label_5.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(64, 182, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 480, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_info.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 480, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 480, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        EmployeeUI.setCentralWidget(self.centralwidget)
        self.actionres = QtWidgets.QAction(EmployeeUI)
        self.actionres.setObjectName("actionres")

        self.retranslateUi(EmployeeUI)
        QtCore.QMetaObject.connectSlotsByName(EmployeeUI)

    def retranslateUi(self, EmployeeUI):
        #get name
        name ="NAME"
        today=date.today()
        res="Hi "+ self.uname +" Date :"+str(today)
        
        _translate = QtCore.QCoreApplication.translate
        EmployeeUI.setWindowTitle(_translate("EmployeeUI", "MainWindow"))
        self.label_info.setText(_translate("EmployeeUI", res))
        self.label_6.setText(_translate("EmployeeUI", "Leave Balance"))
        self.label_7.setText(_translate("EmployeeUI", "Holiday"))
        self.label_8.setText(_translate("EmployeeUI", "Upcoming"))
        self.actionres.setText(_translate("EmployeeUI", "res"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeUI = QtWidgets.QMainWindow()
    ui = Ui_EmployeeUI()
    ui.setupUi(EmployeeUI)
    EmployeeUI.show()
    sys.exit(app.exec_())

