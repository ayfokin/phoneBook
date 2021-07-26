# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pwdRecovery.ui'
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

class Ui_PwdRecovery(object):
    def setupUi(self, PwdRecovery):
        PwdRecovery.setObjectName(_fromUtf8("PwdRecovery"))
        PwdRecovery.resize(440, 360)
        PwdRecovery.setMinimumSize(QtCore.QSize(440, 360))
        PwdRecovery.setMaximumSize(QtCore.QSize(440, 360))
        self.verticalLayout = QtGui.QVBoxLayout(PwdRecovery)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title = QtGui.QLabel(PwdRecovery)
        self.title.setMinimumSize(QtCore.QSize(332, 80))
        self.title.setMaximumSize(QtCore.QSize(332, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.email = QtGui.QLineEdit(PwdRecovery)
        self.email.setMinimumSize(QtCore.QSize(200, 30))
        self.email.setMaximumSize(QtCore.QSize(200, 30))
        self.email.setObjectName(_fromUtf8("email"))
        self.horizontalLayout_2.addWidget(self.email)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.changePwd = QtGui.QPushButton(PwdRecovery)
        self.changePwd.setEnabled(False)
        self.changePwd.setMinimumSize(QtCore.QSize(130, 0))
        self.changePwd.setMaximumSize(QtCore.QSize(130, 16777215))
        self.changePwd.setDefault(True)
        self.changePwd.setObjectName(_fromUtf8("changePwd"))
        self.horizontalLayout_3.addWidget(self.changePwd)
        self.cancelButton = QtGui.QPushButton(PwdRecovery)
        self.cancelButton.setMinimumSize(QtCore.QSize(130, 0))
        self.cancelButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(PwdRecovery)
        QtCore.QMetaObject.connectSlotsByName(PwdRecovery)
        PwdRecovery.setTabOrder(self.email, self.changePwd)
        PwdRecovery.setTabOrder(self.changePwd, self.cancelButton)

    def retranslateUi(self, PwdRecovery):
        PwdRecovery.setWindowTitle(_translate("PwdRecovery", "Восстановление", None))
        self.title.setText(_translate("PwdRecovery", "Восстановление пароля", None))
        self.email.setPlaceholderText(_translate("PwdRecovery", "Адрес электронной почты", None))
        self.changePwd.setText(_translate("PwdRecovery", "Сменить пароль", None))
        self.cancelButton.setText(_translate("PwdRecovery", "Отмена", None))

