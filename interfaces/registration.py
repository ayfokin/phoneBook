# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/registration.ui'
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

class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName(_fromUtf8("Registration"))
        Registration.resize(440, 360)
        Registration.setMinimumSize(QtCore.QSize(440, 360))
        Registration.setMaximumSize(QtCore.QSize(440, 360))
        self.verticalLayout = QtGui.QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title = QtGui.QLabel(Registration)
        self.title.setMinimumSize(QtCore.QSize(175, 80))
        self.title.setMaximumSize(QtCore.QSize(175, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.email = QtGui.QLineEdit(Registration)
        self.email.setMinimumSize(QtCore.QSize(200, 30))
        self.email.setMaximumSize(QtCore.QSize(200, 30))
        self.email.setMaxLength(20)
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout.addWidget(self.email, 1, 0, 1, 1)
        self.username = QtGui.QLineEdit(Registration)
        self.username.setMinimumSize(QtCore.QSize(200, 30))
        self.username.setMaximumSize(QtCore.QSize(200, 30))
        self.username.setMaxLength(20)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 0, 0, 1, 1)
        self.pwd = QtGui.QLineEdit(Registration)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd.sizePolicy().hasHeightForWidth())
        self.pwd.setSizePolicy(sizePolicy)
        self.pwd.setMinimumSize(QtCore.QSize(200, 30))
        self.pwd.setMaximumSize(QtCore.QSize(200, 30))
        self.pwd.setMaxLength(15)
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.gridLayout.addWidget(self.pwd, 2, 0, 1, 1)
        self.repeat_pwd = QtGui.QLineEdit(Registration)
        self.repeat_pwd.setMinimumSize(QtCore.QSize(200, 30))
        self.repeat_pwd.setMaximumSize(QtCore.QSize(200, 30))
        self.repeat_pwd.setMaxLength(15)
        self.repeat_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.repeat_pwd.setObjectName(_fromUtf8("repeat_pwd"))
        self.gridLayout.addWidget(self.repeat_pwd, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.regButton = QtGui.QPushButton(Registration)
        self.regButton.setEnabled(False)
        self.regButton.setMinimumSize(QtCore.QSize(100, 0))
        self.regButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.regButton.setDefault(True)
        self.regButton.setObjectName(_fromUtf8("regButton"))
        self.horizontalLayout_2.addWidget(self.regButton)
        self.cancelButton = QtGui.QPushButton(Registration)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 0))
        self.cancelButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)
        Registration.setTabOrder(self.username, self.email)
        Registration.setTabOrder(self.email, self.pwd)
        Registration.setTabOrder(self.pwd, self.repeat_pwd)
        Registration.setTabOrder(self.repeat_pwd, self.regButton)
        Registration.setTabOrder(self.regButton, self.cancelButton)

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(_translate("Registration", "Регистрация", None))
        self.title.setText(_translate("Registration", "Регистрация", None))
        self.email.setPlaceholderText(_translate("Registration", "Электронная почта", None))
        self.username.setPlaceholderText(_translate("Registration", "Имя пользователя", None))
        self.pwd.setPlaceholderText(_translate("Registration", "Пароль", None))
        self.repeat_pwd.setPlaceholderText(_translate("Registration", "Повторите пароль", None))
        self.regButton.setText(_translate("Registration", "Ок", None))
        self.cancelButton.setText(_translate("Registration", "Отмена", None))

