# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Numan/Desktop/SatisKayit/alimTable.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_showAlimTable(object):
    def setupUi(self, showAlimTable):
        showAlimTable.setObjectName("showAlimTable")
        showAlimTable.resize(854, 398)
        self.btn_anamenu = QtWidgets.QPushButton(showAlimTable)
        self.btn_anamenu.setGeometry(QtCore.QRect(390, 360, 75, 23))
        self.btn_anamenu.setObjectName("btn_anamenu")
        self.tbl_alim = QtWidgets.QTableWidget(showAlimTable)
        self.tbl_alim.setGeometry(QtCore.QRect(30, 20, 630, 321))
        self.tbl_alim.setObjectName("tbl_alim")
        self.tbl_alim.setColumnCount(6)
        self.tbl_alim.setHorizontalHeaderLabels(["Urun No","IMEI","Model","AlimTarihi","AlimFiyati","AlimYeri"])
        self.tbl_alim.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.txt_ara = QtWidgets.QLineEdit(showAlimTable)
        self.txt_ara.setGeometry(QtCore.QRect(680, 30, 150, 30))
        self.txt_ara.setObjectName("txt_ara")
        self.btn_ara = QtWidgets.QPushButton(showAlimTable)
        self.btn_ara.setGeometry(QtCore.QRect(710, 70, 75, 23))
        self.btn_ara.setObjectName("btn_ara")

        self.retranslateUi(showAlimTable)
        QtCore.QMetaObject.connectSlotsByName(showAlimTable)

    def retranslateUi(self, showAlimTable):
        _translate = QtCore.QCoreApplication.translate
        showAlimTable.setWindowTitle(_translate("showAlimTable", "Alım Tablosu"))
        self.btn_anamenu.setText(_translate("showAlimTable", "AnaMenü"))
        self.txt_ara.setText(_translate("showAlimTable", ""))
        self.btn_ara.setText(_translate("showAlimTable", "Ara"))

