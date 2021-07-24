# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/authorization.ui'
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

class Ui_Authorization(object):
    def setupUi(self, Authorization):
        Authorization.setObjectName(_fromUtf8("Authorization"))
        Authorization.resize(440, 360)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Authorization.sizePolicy().hasHeightForWidth())
        Authorization.setSizePolicy(sizePolicy)
        Authorization.setMinimumSize(QtCore.QSize(440, 360))
        Authorization.setMaximumSize(QtCore.QSize(440, 360))
        self.verticalLayout = QtGui.QVBoxLayout(Authorization)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title = QtGui.QLabel(Authorization)
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
        self.pwd = QtGui.QLineEdit(Authorization)
        self.pwd.setMinimumSize(QtCore.QSize(200, 30))
        self.pwd.setMaximumSize(QtCore.QSize(200, 30))
        self.pwd.setMaxLength(15)
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.gridLayout.addWidget(self.pwd, 2, 0, 1, 1)
        self.username = QtGui.QLineEdit(Authorization)
        self.username.setMinimumSize(QtCore.QSize(200, 30))
        self.username.setMaximumSize(QtCore.QSize(200, 30))
        self.username.setMaxLength(20)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.enterButton = QtGui.QPushButton(Authorization)
        self.enterButton.setEnabled(False)
        self.enterButton.setMinimumSize(QtCore.QSize(100, 0))
        self.enterButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.enterButton.setDefault(True)
        self.enterButton.setObjectName(_fromUtf8("enterButton"))
        self.horizontalLayout_3.addWidget(self.enterButton)
        self.regButton = QtGui.QPushButton(Authorization)
        self.regButton.setMinimumSize(QtCore.QSize(100, 0))
        self.regButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.regButton.setObjectName(_fromUtf8("regButton"))
        self.horizontalLayout_3.addWidget(self.regButton)
        self.cancelButton = QtGui.QPushButton(Authorization)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 0))
        self.cancelButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.showPwd = QtGui.QCheckBox(Authorization)
        self.showPwd.setMinimumSize(QtCore.QSize(180, 0))
        self.showPwd.setMaximumSize(QtCore.QSize(180, 16777215))
        self.showPwd.setObjectName(_fromUtf8("showPwd"))
        self.gridLayout_2.addWidget(self.showPwd, 1, 0, 1, 1)
        self.rememberMe = QtGui.QCheckBox(Authorization)
        self.rememberMe.setMinimumSize(QtCore.QSize(180, 0))
        self.rememberMe.setMaximumSize(QtCore.QSize(180, 16777215))
        self.rememberMe.setObjectName(_fromUtf8("rememberMe"))
        self.gridLayout_2.addWidget(self.rememberMe, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.forgotPwd = QtGui.QPushButton(Authorization)
        self.forgotPwd.setMinimumSize(QtCore.QSize(110, 0))
        self.forgotPwd.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.forgotPwd.setFont(font)
        self.forgotPwd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgotPwd.setDefault(False)
        self.forgotPwd.setFlat(True)
        self.forgotPwd.setObjectName(_fromUtf8("forgotPwd"))
        self.gridLayout_3.addWidget(self.forgotPwd, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(Authorization)
        QtCore.QMetaObject.connectSlotsByName(Authorization)
        Authorization.setTabOrder(self.username, self.pwd)
        Authorization.setTabOrder(self.pwd, self.enterButton)
        Authorization.setTabOrder(self.enterButton, self.regButton)
        Authorization.setTabOrder(self.regButton, self.cancelButton)
        Authorization.setTabOrder(self.cancelButton, self.rememberMe)
        Authorization.setTabOrder(self.rememberMe, self.showPwd)
        Authorization.setTabOrder(self.showPwd, self.forgotPwd)

    def retranslateUi(self, Authorization):
        Authorization.setWindowTitle(_translate("Authorization", "Form", None))
        self.title.setText(_translate("Authorization", "Окно авторизации", None))
        self.pwd.setPlaceholderText(_translate("Authorization", "Пароль", None))
        self.username.setPlaceholderText(_translate("Authorization", "Имя пользователя", None))
        self.enterButton.setText(_translate("Authorization", "Войти", None))
        self.regButton.setText(_translate("Authorization", "Регистрация", None))
        self.cancelButton.setText(_translate("Authorization", "Отмена", None))
        self.showPwd.setText(_translate("Authorization", "Показать пароль", None))
        self.rememberMe.setText(_translate("Authorization", "Запомнить меня", None))
        self.forgotPwd.setText(_translate("Authorization", "Забыли пароль?", None))

