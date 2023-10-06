from PyQt5 import QtCore, QtGui, QtWidgets
from MainLogin import Ui_LoginWindow
from registrationNew import Ui_registrationPage
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('BankNH.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS NEWBANK(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME CHAR(20) NOT NULL,
            FIRSTNAME TEXT NOT NULL,
            LASTNAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            PASSWORD TEXT NOT NULL,
            CONFIRM_PASSWORD TEXT NOT NULL,
            PHONE CHAR(11) NOT NULL,
            SEX TEXT,
            ADDRESS CHAR(50) NOT NULL);''')

class Ui_Page(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.resize(800, 600)
        WelcomePage.setMinimumSize(QtCore.QSize(800, 600))

        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")

        # Vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 20pt 'Arial'; color: #2980b9;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 14pt 'Arial'; color: #e74c3c;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_WELCOME_YES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_WELCOME_YES.setStyleSheet("background-color: #2ecc71; color: white;")
        self.pushButton_WELCOME_YES.setObjectName("pushButton_WELCOME_YES")
        self.verticalLayout.addWidget(self.pushButton_WELCOME_YES, alignment=QtCore.Qt.AlignHCenter)

        self.pushButton_WELCOME_NO = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_WELCOME_NO.setStyleSheet("background-color: #e74c3c; color: white;")
        self.pushButton_WELCOME_NO.setObjectName("pushButton_WELCOME_NO")
        self.verticalLayout.addWidget(self.pushButton_WELCOME_NO, alignment=QtCore.Qt.AlignHCenter)

        self.pushButton_QUIT_WELCOME = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_QUIT_WELCOME.setStyleSheet("background-color: #34495e; color: white;")
        self.pushButton_QUIT_WELCOME.setObjectName("pushButton_QUIT_WELCOME")
        self.verticalLayout.addWidget(self.pushButton_QUIT_WELCOME, alignment=QtCore.Qt.AlignHCenter)

        WelcomePage.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(WelcomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        WelcomePage.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        self.statusbar.setObjectName("statusbar")
        WelcomePage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

        ###################################################
        ####               Connecting buttons          ####
        ###################################################
        self.connect_buttons()

    def connect_buttons(self):
        self.pushButton_WELCOME_NO.clicked.connect(self.reg)
        self.pushButton_WELCOME_YES.clicked.connect(self.Login)
        self.pushButton_QUIT_WELCOME.clicked.connect(self.Quitprogram)

    def Quitprogram(self):
        exit()

    def Login(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.beginLogin(self.LoginWindow)
        self.LoginWindow.show()
        WelcomePage.close()

    def reg(self):
        self.registrationPage = QtWidgets.QMainWindow()
        self.ui = Ui_registrationPage()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.show()
        WelcomePage.close()

    def open_window(self, ui_class):
        window = QtWidgets.QMainWindow()
        ui = ui_class()
        ui.setupUi(window)
        window.show()
        WelcomePage.close()

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Welcome to MTBL"))
        self.label.setText(_translate("WelcomePage", "Welcome to MT Bank Limited"))
        self.label_2.setText(_translate("WelcomePage", "Do You Have An Existing Account?"))
        self.pushButton_WELCOME_YES.setText(_translate("WelcomePage", "YES"))
        self.pushButton_WELCOME_NO.setText(_translate("WelcomePage", "NO"))
        self.pushButton_QUIT_WELCOME.setText(_translate("WelcomePage", "QUIT PROGRAM"))
        self.menuQuit.setTitle(_translate("WelcomePage", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
