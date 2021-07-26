# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/contactTemplate.ui'
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

class Ui_ContactTemplate(object):
    def setupUi(self, ContactTemplate):
        ContactTemplate.setObjectName(_fromUtf8("ContactTemplate"))
        ContactTemplate.setWindowModality(QtCore.Qt.ApplicationModal)
        ContactTemplate.resize(440, 360)
        ContactTemplate.setMinimumSize(QtCore.QSize(440, 360))
        ContactTemplate.setMaximumSize(QtCore.QSize(440, 360))
        self.verticalLayout = QtGui.QVBoxLayout(ContactTemplate)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title = QtGui.QLabel(ContactTemplate)
        self.title.setMinimumSize(QtCore.QSize(260, 80))
        self.title.setMaximumSize(QtCore.QSize(260, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.phoneNumber = QtGui.QLineEdit(ContactTemplate)
        self.phoneNumber.setMinimumSize(QtCore.QSize(200, 30))
        self.phoneNumber.setMaximumSize(QtCore.QSize(200, 30))
        self.phoneNumber.setMaxLength(12)
        self.phoneNumber.setObjectName(_fromUtf8("phoneNumber"))
        self.gridLayout.addWidget(self.phoneNumber, 1, 0, 1, 1)
        self.username = QtGui.QLineEdit(ContactTemplate)
        self.username.setMinimumSize(QtCore.QSize(200, 30))
        self.username.setMaximumSize(QtCore.QSize(200, 30))
        self.username.setMaxLength(25)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 0, 0, 1, 1)
        self.birthDate = QtGui.QDateEdit(ContactTemplate)
        self.birthDate.setMinimumSize(QtCore.QSize(200, 30))
        self.birthDate.setMaximumSize(QtCore.QSize(200, 30))
        self.birthDate.setCalendarPopup(True)
        self.birthDate.setObjectName(_fromUtf8("birthDate"))
        self.gridLayout.addWidget(self.birthDate, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(ContactTemplate)
        self.okButton.setMinimumSize(QtCore.QSize(130, 0))
        self.okButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(ContactTemplate)
        self.cancelButton.setMinimumSize(QtCore.QSize(130, 0))
        self.cancelButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(ContactTemplate)
        QtCore.QMetaObject.connectSlotsByName(ContactTemplate)
        ContactTemplate.setTabOrder(self.username, self.phoneNumber)
        ContactTemplate.setTabOrder(self.phoneNumber, self.birthDate)
        ContactTemplate.setTabOrder(self.birthDate, self.okButton)
        ContactTemplate.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, ContactTemplate):
        ContactTemplate.setWindowTitle(_translate("ContactTemplate", "Шаблон", None))
        self.title.setText(_translate("ContactTemplate", "Шаблон", None))
        self.phoneNumber.setPlaceholderText(_translate("ContactTemplate", "Телефон", None))
        self.username.setPlaceholderText(_translate("ContactTemplate", "Имя", None))
        self.okButton.setText(_translate("ContactTemplate", "Ок", None))
        self.cancelButton.setText(_translate("ContactTemplate", "Отмена", None))

