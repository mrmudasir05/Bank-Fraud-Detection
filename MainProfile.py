# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QInputDialog, QLineEdit


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 505)
        MainWindow.setStyleSheet("background-color: rgb(111, 87, 130);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"color: rgb(252, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_balance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_balance.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_balance.setObjectName("pushButton_balance")
        self.gridLayout.addWidget(self.pushButton_balance, 1, 0, 1, 1)

        self.pushButton_deleteAccount = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deleteAccount.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_deleteAccount.setObjectName("pushButton_deleteAccount")
        self.gridLayout.addWidget(self.pushButton_deleteAccount, 9, 0, 1, 1)

        self.pushButton_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_transfer.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_transfer.setObjectName("pushButton_transfer")
        self.gridLayout.addWidget(self.pushButton_transfer, 2, 0, 1, 1)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.gridLayout.addWidget(self.pushButton_logout, 10, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #######################################
        #connecting Butttons to the profile functions
        ###############################################

        self.pushButton_balance.clicked.connect(self.CheckBal)
        self.pushButton_transfer.clicked.connect(self.Transfer)
        self.pushButton_deleteAccount.clicked.connect(self.DeleteAcc)
        self.pushButton_logout.clicked.connect(self.Logout)

    def CancleNow(self):
        print('working')

# Pop Messages
    def MessagesProfile(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setText(message)
        mssg.buttonClicked.connect(self.buttonClickeed)
        mssg.exec_()

    def buttonClickeed(self, me):
        if me.text() == QMessageBox.Ok:
            print('quite')
            quit()

    from PyQt5.QtWidgets import QMessageBox

    def Logout(self):
        # Ask the user for confirmation
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            # User confirmed, close the application
            quit()
        else:
            # User canceled, return to the dashboard or take appropriate action
            self.setupUi(MainWindow)  # Replace with the actual function to show the dashboard

    def DeleteAcc(self):
        import sqlite3
        from PyQt5.QtWidgets import QMessageBox

        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()

        password, okPressed = QInputDialog.getText(self, "Delete Account", "Please Enter Your Password:",
                                                   QtWidgets.QLineEdit.Password)

        if okPressed:
            # Check if the password matches a record in the database
            cur.execute("SELECT * FROM NEWBANK WHERE PASSWORD = ?", (password,))
            user_data = cur.fetchone()

            if user_data is not None:
                # If a matching user is found, delete the user's record
                cur.execute("DELETE FROM NEWBANK WHERE PASSWORD = ?", (password,))
                conn.commit()
                conn.close()

                # Show a success message
                QMessageBox.information(self, "Account Deleted", "Your account has been successfully deleted.")
            else:
                conn.close()
                # Show an error message for incorrect password
                QMessageBox.warning(self, "Deletion Failed", "Incorrect password. Account not deleted.")
        else:
            self.mainwindow.show()


    def Transfer(self):
        self.mainwindow.close()
        from Transfer import Ui_TransferWindow
        self.TransferWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TransferWindow()
        self.ui.setupUi(self.TransferWindow)
        self.TransferWindow.show()


    def Passwordmessage(self):
        pmsg = QMessageBox()
        pmsg.setIcon(QMessageBox.Information)
        pmsg.setInformativeText('Please Enter Your Password?')
        pmsg.show()
        pmsg.exec_()

    def initUI(self):
        self.getText()

    from PyQt5.QtWidgets import QInputDialog, QMessageBox

    # ...

    def CheckBal(self):
        import sqlite3

        # Get the password from the user
        password, okPressed = QInputDialog.getText(self, "Check Balance", "Please Enter Your Password:",
                                                   QtWidgets.QLineEdit.Password)

        # Check if the user pressed OK and entered a password
        if okPressed and password:
            conn = sqlite3.connect('BankNH.db')
            cur = conn.cursor()

            # Check if the entered password matches a record in the database
            cur.execute("SELECT BAL FROM NEWBANK WHERE PASSWORD = ?", (password,))
            data = cur.fetchone()

            if data is not None:
                # Display the balance
                balance = data[0]
                QMessageBox.information(self, "Balance", f"Your balance is: {balance}")
            else:
                # Show an error message for incorrect password
                QMessageBox.warning(self, "Invalid Password", "Invalid password. Please try again.")
        else:
            # Show an error message if no password was entered
            QMessageBox.warning(self, "Invalid Input", "Invalid input. Please enter a password.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME TO Your MTBL DASHBOARD"))
        self.pushButton_balance.setText(_translate("MainWindow", "BALANCE"))
        self.pushButton_deleteAccount.setText(_translate("MainWindow", "DELETE ACCOUNT"))
        self.pushButton_transfer.setText(_translate("MainWindow", "TRANSFER"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOG OUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

