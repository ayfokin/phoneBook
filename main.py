# coding=utf-8
import sys
import re

from PyQt4.QtGui import QWidget, QMessageBox, QLineEdit, QMainWindow, QApplication, QDialog
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
            msgbox.critical(self, u"Ошибка", u"Пользователь с такими данными не найден")

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
            msgbox.critical(self, u"Ошибка", u"Пользователь с таким именем уже зарегистрирован")
            return

        if password != r_password:
            msgbox.critical(self, u"Ошибка", u"Пароли не совпадают")
            return

        if not re.match(regex, email):
            msgbox.critical(self, u"Ошибка", u"Введите корректный адрес электронной почты")
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
            msgbox.critical(self, u"Ошибка", u"Введите корректный адрес электронной почты")
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
        # self.tableWidget.horizontalHeader().setFixedHeight(40)

    def changeTable(self):
        index = self.listWidget.currentRow()
        # self.stackedWidget.setCurrentIndex(index)


class ContactTemplate(QDialog, Ui_ContactTemplate):
    def __init__(self, parent):
        super(ContactTemplate, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.informationText = ''

    def addContact(self):
        name = str(self.username.text().toUtf8())
        phone = str(self.phoneNumber.text().toUtf8())
        birth = self.birthDate.dateTime()
        msgbox = QMessageBox()

        regex = r'(^[\+\d]{1}\d{9}$)'

        if not re.match(regex, phone):
            msgbox.critical(self, u"Ошибка", u"Введите корректный номер телефона в формате +12345678900")
            return

        self.parent.database.addContact(name, phone, birth)
        msgbox.information(self, u"Успех", self.informationText)


class InsertContact(ContactTemplate):
    def __init__(self, parent):
        super(InsertContact, self).__init__(parent)
        self.informationText = u"Контакт успешно добавлен"
        self.title.setText(u"Добавить контакт")
        self.setWindowTitle(u"Добавление контакта")


class EditContact(ContactTemplate):
    def __init__(self, parent):
        super(EditContact, self).__init__(parent)
        self.informationText = u"Контакт успешно изменен"
        self.title.setText(u"Измененить контакта")
        self.setWindowTitle(u"Изменение контакта")
        # TODO: add autofill for editText


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
window = PhoneBook()
window.loginWindow()
sys.exit(app.exec_())
