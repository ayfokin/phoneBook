# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/phoneBook.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PhoneBook(object):
    def setupUi(self, PhoneBook):
        PhoneBook.setObjectName(_fromUtf8("PhoneBook"))
        PhoneBook.resize(661, 453)
        self.centralwidget = QtGui.QWidget(PhoneBook)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 200, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        PhoneBook.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhoneBook)
        QtCore.QMetaObject.connectSlotsByName(PhoneBook)

    def retranslateUi(self, PhoneBook):
        PhoneBook.setWindowTitle(_translate("PhoneBook", "Phone Book", None))
        self.label.setText(_translate("PhoneBook", "Мы внутри", None))

