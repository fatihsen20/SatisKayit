# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/Otomasyon/alim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Ui_AlimTable(object):
    def setupUi(self, AlimTable):
        AlimTable.setObjectName("AlimTable")
        AlimTable.resize(453, 408)
        self.label = QtWidgets.QLabel(AlimTable)
        self.label.setGeometry(QtCore.QRect(50, 60, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AlimTable)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AlimTable)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AlimTable)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AlimTable)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.txt_Imei = QtWidgets.QLineEdit(AlimTable)
        self.txt_Imei.setGeometry(QtCore.QRect(130, 70, 301, 31))
        self.txt_Imei.setObjectName("txt_Imei")
        self.txt_Model = QtWidgets.QLineEdit(AlimTable)
        self.txt_Model.setGeometry(QtCore.QRect(130, 120, 301, 31))
        self.txt_Model.setObjectName("txt_Model")
        self.txt_Tarih = QtWidgets.QLineEdit(AlimTable)
        self.txt_Tarih.setGeometry(QtCore.QRect(130, 170, 301, 31))
        self.txt_Tarih.setObjectName("txt_Tarih")
        self.txt_Fiyat = QtWidgets.QLineEdit(AlimTable)
        self.txt_Fiyat.setGeometry(QtCore.QRect(130, 220, 301, 31))
        self.txt_Fiyat.setObjectName("txt_Fiyat")
        self.txt_Alimyeri = QtWidgets.QLineEdit(AlimTable)
        self.txt_Alimyeri.setGeometry(QtCore.QRect(130, 270, 301, 31))
        self.txt_Alimyeri.setObjectName("txt_Alimyeri")
        self.btn_kayit = QtWidgets.QPushButton(AlimTable)
        self.btn_kayit.setGeometry(QtCore.QRect(120, 360, 75, 23))
        self.btn_kayit.setObjectName("btn_kayit")
        self.btn_anamenu = QtWidgets.QPushButton(AlimTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(240, 360, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")

        self.retranslateUi(AlimTable)
        QtCore.QMetaObject.connectSlotsByName(AlimTable)

    def retranslateUi(self, AlimTable):
        _translate = QtCore.QCoreApplication.translate
        AlimTable.setWindowTitle(_translate("AlimTable", "Alım Formu"))
        self.label.setText(_translate("AlimTable", "Imei:"))
        self.label_2.setText(_translate("AlimTable", "Model:"))
        self.label_3.setText(_translate("AlimTable", "Alım Tarihi:"))
        self.label_4.setText(_translate("AlimTable", "Alım Fiyatı:"))
        self.label_5.setText(_translate("AlimTable", "Alım Yeri:"))
        self.btn_kayit.setText(_translate("AlimTable", "Kaydet"))
        self.btn_anamenu.setText(_translate("AlimTable", "Ana Menü"))

