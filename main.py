# coding=utf-8
import datetime
import locale
import os
import sys
import re

from PyQt4.QtCore import QDate, QTranslator, QLocale, QLibraryInfo, QCoreApplication
from PyQt4.QtGui import QWidget, QMessageBox, QLineEdit, QMainWindow, QApplication, QDialog, QTableWidgetItem
from interfaces.authorization import Ui_Authorization
from interfaces.pwdRecovery import Ui_PwdRecovery
from interfaces.mainScreen import Ui_MainScreen
from interfaces.registration import Ui_Registration
from interfaces.contactTemplate import Ui_ContactTemplate
from database import Database


class Login(QWidget, Ui_Authorization):
    def __init__(self, parent):
        super(Login, self).__init__()

        self.setupUi(self)
        self.parent = parent

        self.username.textEdited.connect(self.checkEnterButton)
        self.pwd.textEdited.connect(self.checkEnterButton)

        self.enterButton.clicked.connect(self.enterButtonClicked)

        self.regButton.clicked.connect(self.parent.regWindow)
        self.regButton.clicked.connect(self.close)

        self.showPwd.stateChanged.connect(self.changePwdShow)

        self.cancelButton.clicked.connect(sys.exit)

        self.forgotPwd.clicked.connect(self.forgot)

    def enterButtonClicked(self):
        username = str(self.username.text().toUtf8())
        password = str(self.pwd.text().toUtf8())
        if self.parent.isUserExists(username, password):
            self.parent.mainScreenWindow()
            self.close()
        else:
            msgbox = QMessageBox()
            msgbox.warning(self, u"Ошибка", u"Пользователь с такими данными не найден")

    def checkEnterButton(self):
        if self.username.text() != '' and self.pwd.text() != '':
            if not self.enterButton.isEnabled():
                self.enterButton.setEnabled(True)
        else:
            if self.enterButton.isEnabled():
                self.enterButton.setDisabled(True)

    def forgot(self):
        self.close()
        self.parent.pwdRecoveryWindow()

    def changePwdShow(self):
        if self.showPwd.isChecked():
            self.pwd.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.pwd.setEchoMode(QLineEdit.EchoMode.Password)


class Registration(QWidget, Ui_Registration):
    def __init__(self, parent):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.regButton.clicked.connect(self.regButtonClicked)

        self.username.textEdited.connect(self.checkRegButton)
        self.pwd.textEdited.connect(self.checkRegButton)
        self.repeat_pwd.textEdited.connect(self.checkRegButton)
        self.email.textEdited.connect(self.checkRegButton)

        self.cancelButton.clicked.connect(self.parent.loginWindow)
        self.cancelButton.clicked.connect(self.close)

    def regButtonClicked(self):
        msgbox = QMessageBox()
        regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

        username = str(self.username.text().toUtf8())
        password = str(self.pwd.text().toUtf8())
        r_password = str(self.repeat_pwd.text().toUtf8())
        email = str(self.email.text().toUtf8())

        if self.parent.isUserExists(username):
            msgbox.warning(self, u"Ошибка", u"Пользователь с таким именем уже зарегистрирован")
            return

        if password != r_password:
            msgbox.warning(self, u"Ошибка", u"Пароли не совпадают")
            return

        if not re.match(regex, email):
            msgbox.warning(self, u"Ошибка", u"Введите корректный адрес электронной почты")
            return

        self.parent.database.addUser(username, password, email)
        msgbox.information(self, u"Успех", u"Успешная регистрация")
        self.close()
        self.parent.mainScreenWindow()

    def checkRegButton(self):
        if self.username.text() != '' and self.pwd.text() != '' and self.repeat_pwd.text() != '' and self.email.text() != '':
            if not self.regButton.isEnabled():
                self.regButton.setEnabled(True)
        else:
            if self.regButton.isEnabled():
                self.regButton.setDisabled(True)


class PwdRecovery(QWidget, Ui_PwdRecovery):
    def __init__(self, parent):
        super(PwdRecovery, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.changePwd.clicked.connect(self.sendEmail)
        self.cancelButton.clicked.connect(self.parent.loginWindow)
        self.email.textEdited.connect(self.checkChangePwd)
        self.cancelButton.clicked.connect(self.close)

    def sendEmail(self):
        regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        msgbox = QMessageBox()
        email = str(self.email.text().toUtf8())

        if not re.match(regex, email):
            msgbox.warning(self, u"Ошибка", u"Введите корректный адрес электронной почты")
            return
        # sending email...

        msgbox.information(self, u"Успех", u"Что-то сделано")
        self.close()
        self.parent.loginWindow()

    def checkChangePwd(self):
        if self.email.text() != '':
            if not self.changePwd.isEnabled():
                self.changePwd.setEnabled(True)
        else:
            if self.changePwd.isEnabled():
                self.changePwd.setDisabled(True)


class MainScreen(QWidget, Ui_MainScreen):
    def __init__(self, parent):
        super(MainScreen, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.tabsort = [u'Б', u'Г', u'Е', u'Й', u'Л', u'Н', u'П', u'С', u'У', u'Х', u'Щ', u'Э', u'Я']
        self.contacts = [[] for _ in range(len(self.tabsort))]

        self.addContactButton.clicked.connect(self.insert)
        self.editContactButton.clicked.connect(self.edit)
        self.deleteContactButton.clicked.connect(self.delete)
        self.listWidget.currentRowChanged.connect(self.updateTable)

        self.tableWidget.horizontalHeader().setClickable(False)

        contacts = self.parent.database.selectContacts()
        index = 0
        for contact in contacts:
            self.insertContact(contact, index=index)
        self.listWidget.setCurrentRow(0)
        self.updateTable()

    def insertContact(self, contact, sort=True, index=0):
        letter = contact[0][0].upper()
        while letter > self.tabsort[index]:
            index += 1
        if sort:
            self.contacts[index].append(contact)
        else:
            left, right = 0, len(self.contacts[index])
            while right - left > 0:
                middle = (left + right) // 2
                if self.contacts[index][middle][0].upper() > contact[0].upper():
                    right = middle
                else:
                    left = middle + 1
            self.contacts[index].insert(right, contact)

    def editContact(self, contact):
        self.deleteContact()
        self.insertContact(contact, sort=False)

    def deleteContact(self):
        tab = self.listWidget.currentRow()
        row = self.tableWidget.currentRow()
        contact = self.contacts[tab][row]
        self.parent.database.deleteContact(contact[0], contact[1], contact[2])
        del self.contacts[tab][row]

    def updateTable(self):
        index = self.listWidget.currentRow()
        self.tableWidget.clearContents()
        for i, contact in enumerate(self.contacts[index]):
            for j, field in enumerate(contact):
                if isinstance(field, datetime.date):
                    field = QDate(field)
                    field = field.toString("d MMMM yyyy")
                self.tableWidget.setItem(i, j, QTableWidgetItem(field))

    def insert(self):
        self.insertContactDialog = InsertContact(self)
        self.insertContactDialog.show()

    def edit(self):
        self.editContactDialog = EditContact(self)
        self.editContactDialog.show()

    def delete(self):
        msgbox = QMessageBox()
        reply = msgbox.question(self, u"Удаление", u"Вы действительно хотите удалить выбранный контакт?",
                                msgbox.Yes, msgbox.No)
        if reply == QMessageBox.Yes:

            self.deleteContact()
            self.updateTable()



class ContactTemplate(QDialog, Ui_ContactTemplate):
    def __init__(self, parent):
        super(ContactTemplate, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.okButton.clicked.connect(self.okButtonClicked)
        self.cancelButton.clicked.connect(self.reject)

    def okButtonClicked(self):
        name = str(self.username.text().toUtf8()).decode("utf-8")
        phone = str(self.phoneNumber.text().toUtf8()).decode("utf-8")
        birth = self.birthDate.date()
        msgbox = QMessageBox()

        regex = ur'(^[А-Яа-я\s]+$)'
        if not re.match(regex, name):
            msgbox.warning(self, u"Ошибка", u"Имя может состоять только из символов кириллицы")
            return
        name = name.split()
        name = ' '.join(name)

        regex = r'(^\+?\d{11}$)'
        if not re.match(regex, phone):
            msgbox.warning(self, u"Ошибка", u"Введите корректный номер телефона в формате +12345678900")
            return


        # TODO: edit after creating array of contacts
        # if self.parent.database.checkContact(name, phone, birth):
        #     msgbox.warning(self, u"Ошибка", u"Контакт с такими данными уже существует")
        #     return

        self.applyChanges(name, phone, birth)
        msgbox.information(self, u"Успех", self.informationText)
        self.close()
        self.parent.updateTable()

    def applyChanges(self, name, phone, birth):
        pass


class InsertContact(ContactTemplate):
    def __init__(self, parent):
        super(InsertContact, self).__init__(parent)
        self.informationText = u"Контакт успешно добавлен"
        self.title.setText(u"Добавить контакт")
        self.setWindowTitle(u"Добавление контакта")

    def applyChanges(self, name, phone, birth):
        self.parent.parent.database.addContact(name, phone, str(QDate(birth).toString("yyyy-MM-dd").toUtf8()).decode("utf-8"))
        self.parent.insertContact((name, phone, birth.toPyDate()), sort=False)


class EditContact(ContactTemplate):
    def __init__(self, parent):
        super(EditContact, self).__init__(parent)
        self.informationText = u"Контакт успешно изменен"
        self.title.setText(u"Изменить контакт")
        self.setWindowTitle(u"Изменение контакта")
        self.username.setText(self.parent.tableWidget.selectedItems()[0].text())
        self.phoneNumber.setText(self.parent.tableWidget.selectedItems()[1].text())
        self.birthDate.setDate(QDate.fromString(self.parent.tableWidget.selectedItems()[2].text(), "d MMMM yyyy"))

    def applyChanges(self, name, phone, birth):
        self.parent.parent.database.editContact(name, phone, str(QDate(birth).toString("yyyy-MM-dd").toUtf8()).decode("utf-8"))
        self.parent.editContact((name, phone, birth.toPyDate()))


class PhoneBook(QMainWindow):
    def __init__(self):
        super(PhoneBook, self).__init__()
        self.database = Database()

    def loginWindow(self):
        self.login = Login(self)
        self.login.show()

    def regWindow(self):
        self.registration = Registration(self)
        self.registration.show()

    def pwdRecoveryWindow(self):
        self.recovery = PwdRecovery(self)
        self.recovery.show()

    def mainScreenWindow(self):
        self.mainScreen = MainScreen(self)
        self.mainScreen.show()

    def isUserExists(self, username, password=None):
        return self.database.checkUser(username, password)


app = QApplication(sys.argv)

qt_translator = QTranslator(app)
qt_translator.load("qt_" + QLocale().system().name(), QLibraryInfo.location(QLibraryInfo.TranslationsPath))
app.installTranslator(qt_translator)


window = PhoneBook()
window.loginWindow()
sys.exit(app.exec_())
