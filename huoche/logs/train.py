# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 684)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 57, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 57, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 81, 16))
        self.label_3.setObjectName("label_3")
        self.inquire = QtWidgets.QPushButton(Form)
        self.inquire.setGeometry(QtCore.QRect(410, 80, 80, 22))
        self.inquire.setObjectName("inquire")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 57, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 150, 57, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(310, 150, 57, 14))
        self.label_7.setObjectName("label_7")
        self.Ttype_LineEdit = QtWidgets.QLineEdit(Form)
        self.Ttype_LineEdit.setGeometry(QtCore.QRect(150, 150, 113, 22))
        self.Ttype_LineEdit.setObjectName("Ttype_LineEdit")
        self.Tid_LineEdit = QtWidgets.QLineEdit(Form)
        self.Tid_LineEdit.setGeometry(QtCore.QRect(420, 150, 113, 22))
        self.Tid_LineEdit.setObjectName("Tid_LineEdit")
        self.Tra_Num_Line = QtWidgets.QLineEdit(Form)
        self.Tra_Num_Line.setGeometry(QtCore.QRect(160, 80, 211, 22))
        self.Tra_Num_Line.setObjectName("Tra_Num_Line")
        self.detail = QtWidgets.QPushButton(Form)
        self.detail.setGeometry(QtCore.QRect(10, 410, 80, 22))
        self.detail.setObjectName("detail")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 270, 471, 111))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tw = QtWidgets.QTableWidget(Form)
        self.tw.setGeometry(QtCore.QRect(30, 440, 491, 151))
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(0)
        self.tw.setRowCount(0)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 190, 511, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.first = QtWidgets.QPushButton(self.widget)
        self.first.setObjectName("first")
        self.horizontalLayout_2.addWidget(self.first)
        self.front = QtWidgets.QPushButton(self.widget)
        self.front.setObjectName("front")
        self.horizontalLayout_2.addWidget(self.front)
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setObjectName("next")
        self.horizontalLayout_2.addWidget(self.next)
        self.last = QtWidgets.QPushButton(self.widget)
        self.last.setObjectName("last")
        self.horizontalLayout_2.addWidget(self.last)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "info_input"))
        self.label_2.setText(_translate("Form", "train_info"))
        self.label_3.setText(_translate("Form", "inquire_res"))
        self.inquire.setText(_translate("Form", "inquire"))
        self.label_5.setText(_translate("Form", "num"))
        self.label_6.setText(_translate("Form", "train_class"))
        self.label_7.setText(_translate("Form", "train_num"))
        self.detail.setText(_translate("Form", "details"))
        self.first.setText(_translate("Form", "first"))
        self.front.setText(_translate("Form", "front"))
        self.next.setText(_translate("Form", "next"))
        self.last.setText(_translate("Form", "last"))
