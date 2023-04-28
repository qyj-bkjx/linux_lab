# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'train.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 684)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 57, 14))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 57, 14))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 240, 81, 16))
        self.inquire = QPushButton(Form)
        self.inquire.setObjectName(u"inquire")
        self.inquire.setGeometry(QRect(410, 80, 80, 22))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 80, 57, 14))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 150, 57, 16))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 150, 57, 14))
        self.Ttype_LineEdit = QLineEdit(Form)
        self.Ttype_LineEdit.setObjectName(u"Ttype_LineEdit")
        self.Ttype_LineEdit.setGeometry(QRect(150, 150, 113, 22))
        self.Tid_LineEdit = QLineEdit(Form)
        self.Tid_LineEdit.setObjectName(u"Tid_LineEdit")
        self.Tid_LineEdit.setGeometry(QRect(420, 150, 113, 22))
        self.Tra_Num_Line = QLineEdit(Form)
        self.Tra_Num_Line.setObjectName(u"Tra_Num_Line")
        self.Tra_Num_Line.setGeometry(QRect(160, 80, 211, 22))
        self.detail = QPushButton(Form)
        self.detail.setObjectName(u"detail")
        self.detail.setGeometry(QRect(10, 410, 80, 22))
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 270, 471, 111))
        self.tw = QTableWidget(Form)
        self.tw.setObjectName(u"tw")
        self.tw.setGeometry(QRect(30, 440, 491, 151))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 190, 511, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.first = QPushButton(self.widget)
        self.first.setObjectName(u"first")

        self.horizontalLayout_2.addWidget(self.first)

        self.front = QPushButton(self.widget)
        self.front.setObjectName(u"front")

        self.horizontalLayout_2.addWidget(self.front)

        self.next = QPushButton(self.widget)
        self.next.setObjectName(u"next")

        self.horizontalLayout_2.addWidget(self.next)

        self.last = QPushButton(self.widget)
        self.last.setObjectName(u"last")

        self.horizontalLayout_2.addWidget(self.last)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"info_input", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"train_info", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"inquire_res", None))
        self.inquire.setText(QCoreApplication.translate("Form", u"inquire", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"num", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"train_class", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"train_num", None))
        self.detail.setText(QCoreApplication.translate("Form", u"details", None))
        self.first.setText(QCoreApplication.translate("Form", u"first", None))
        self.front.setText(QCoreApplication.translate("Form", u"front", None))
        self.next.setText(QCoreApplication.translate("Form", u"next", None))
        self.last.setText(QCoreApplication.translate("Form", u"last", None))
    # retranslateUi

