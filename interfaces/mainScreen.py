# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainScreen.ui'
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

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName(_fromUtf8("MainScreen"))
        MainScreen.resize(785, 661)
        self.gridLayout = QtGui.QGridLayout(MainScreen)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(MainScreen)
        self.listWidget.setMinimumSize(QtCore.QSize(58, 355))
        self.listWidget.setMaximumSize(QtCore.QSize(58, 355))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(7)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(_fromUtf8("QListWidget::Item { \n"
"    selection-background-color: darkblue;\n"
"    background-color:lightgrey;\n"
"    border: 1px solid grey;\n"
"    height: 25;\n"
"}\n"
"\n"
"QListWidget::Item:selected {\n"
"    background-color: #EAEAEA;\n"
"}\n"
"\n"
"\n"
""))
        self.listWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.frame = QtGui.QFrame(MainScreen)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setMinimumSize(QtCore.QSize(512, 522))
        self.tableWidget.setStyleSheet(_fromUtf8("QHeaderView::section { \n"
"    background-color: #ccc;\n"
"    height: 40px;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #919191;\n"
"    alternate-background-color: #e4e4e4;\n"
"    background-color: white;\n"
"    selection-background-color: #818181;\n"
"    selection-color: white;\n"
"}\n"
""))
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.gridLayout_2.addWidget(self.tableWidget, 3, 1, 1, 6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.username = QtGui.QPushButton(self.frame)
        self.username.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.username.setFont(font)
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.username.setStyleSheet(_fromUtf8("QPushButton {\n"
"    text-align: left;\n"
"    border: None;\n"
"    color: blue;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: None;\n"
"}"))
        self.username.setFlat(False)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout_2.addWidget(self.username, 2, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 7, 1, 1)
        self.addContactButton = QtGui.QPushButton(self.frame)
        self.addContactButton.setObjectName(_fromUtf8("addContactButton"))
        self.gridLayout_2.addWidget(self.addContactButton, 2, 1, 1, 1)
        self.editContactButton = QtGui.QPushButton(self.frame)
        self.editContactButton.setEnabled(False)
        self.editContactButton.setObjectName(_fromUtf8("editContactButton"))
        self.gridLayout_2.addWidget(self.editContactButton, 2, 2, 1, 1)
        self.deleteContactButton = QtGui.QPushButton(self.frame)
        self.deleteContactButton.setEnabled(False)
        self.deleteContactButton.setObjectName(_fromUtf8("deleteContactButton"))
        self.gridLayout_2.addWidget(self.deleteContactButton, 2, 3, 1, 1)
        self.enterAs = QtGui.QLabel(self.frame)
        self.enterAs.setMinimumSize(QtCore.QSize(65, 40))
        self.enterAs.setMaximumSize(QtCore.QSize(65, 40))
        self.enterAs.setObjectName(_fromUtf8("enterAs"))
        self.gridLayout_2.addWidget(self.enterAs, 2, 5, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 3, 1)

        self.retranslateUi(MainScreen)
        self.listWidget.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(_translate("MainScreen", "Телефонная книга", None))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainScreen", "АБ", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainScreen", "ВГ", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainScreen", "ДЕ", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainScreen", "ЖЗИЙ", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainScreen", "КЛ", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainScreen", "МН", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainScreen", "ОП", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainScreen", "РС", None))
        item = self.listWidget.item(8)
        item.setText(_translate("MainScreen", "ТУ", None))
        item = self.listWidget.item(9)
        item.setText(_translate("MainScreen", "ФХ", None))
        item = self.listWidget.item(10)
        item.setText(_translate("MainScreen", "ЦЧШЩ", None))
        item = self.listWidget.item(11)
        item.setText(_translate("MainScreen", "ЪЫЬЭ", None))
        item = self.listWidget.item(12)
        item.setText(_translate("MainScreen", "ЮЯ", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Имя", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Телефон", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainScreen", "Дата рождения", None))
        self.username.setText(_translate("MainScreen", "Админ", None))
        self.addContactButton.setText(_translate("MainScreen", "Добавить", None))
        self.editContactButton.setText(_translate("MainScreen", "Изменить", None))
        self.deleteContactButton.setText(_translate("MainScreen", "Удалить", None))
        self.enterAs.setText(_translate("MainScreen", "Зашли как", None))

