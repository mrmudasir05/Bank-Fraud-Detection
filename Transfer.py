import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sqlite3
import random
import sklearn
import pickle
import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MainProfile import Ui_MainWindow
class Ui_TransferWindow(object):
    def setupUi(self, TransferWindow):
        self.transfer = TransferWindow
        TransferWindow.setObjectName("TransferWindow")
        TransferWindow.resize(567, 352)
        TransferWindow.setStyleSheet("background-color: rgb(111, 87, 130);\n"
"")
        self.centralwidget = QtWidgets.QWidget(TransferWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 468, 183))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.label_amount2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_amount2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_amount2txf.setObjectName("label_amount2txf")
        self.gridLayout.addWidget(self.label_amount2txf, 1, 0, 1, 1)
        self.lineEdit_name2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_name2txf.setObjectName("lineEdit_name2txf")
        self.gridLayout.addWidget(self.lineEdit_name2txf, 2, 1, 1, 1)
        self.label_name2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_name2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_name2txf.setObjectName("label_name2txf")
        self.gridLayout.addWidget(self.label_name2txf, 2, 0, 1, 1)
        self.label_number2txf = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_number2txf.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.label_number2txf.setObjectName("label_number2txf")
        self.gridLayout.addWidget(self.label_number2txf, 3, 0, 1, 1)
        self.comboBox_accountType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_accountType.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.comboBox_accountType.setObjectName("comboBox_accountType")
        self.comboBox_accountType.addItem("")
        self.comboBox_accountType.addItem("")
        self.comboBox_accountType.addItem("")
        self.gridLayout.addWidget(self.comboBox_accountType, 5, 0, 1, 2)
        self.lineEdit_number2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_number2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_number2txf.setObjectName("lineEdit_number2txf")
        self.gridLayout.addWidget(self.lineEdit_number2txf, 3, 1, 1, 1)
        self.comboBox_bankType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_bankType.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 252, 252);")
        self.comboBox_bankType.setObjectName("comboBox_bankType")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.comboBox_bankType.addItem("")
        self.gridLayout.addWidget(self.comboBox_bankType, 6, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 1, 1, 1)
        self.lineEdit_amount2txf = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_amount2txf.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(12, 31, 45);")
        self.lineEdit_amount2txf.setObjectName("lineEdit_amount2txf")
        self.gridLayout.addWidget(self.lineEdit_amount2txf, 1, 1, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(160, 240, 211, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.pushButton_transferTransfer = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_transferTransfer.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(22, 252, 252);")
        self.pushButton_transferTransfer.setObjectName("pushButton_transferTransfer")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.pushButton_transferTransfer)

        self.pushButton_transferCancle = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_transferCancle.setStyleSheet("font: 75 10pt \"Verdana\";\n"
"color: rgb(252, 55, 9);")
        self.pushButton_transferCancle.setObjectName("pushButton_transferCancle")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pushButton_transferCancle)

        TransferWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TransferWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 26))
        self.menubar.setObjectName("menubar")
        TransferWindow.setMenuBar(self.menubar)

        self.retranslateUi(TransferWindow)
        QtCore.QMetaObject.connectSlotsByName(TransferWindow)
        self.pushButton_transferTransfer.clicked.connect(self.SendTransfer)
        self.pushButton_transferCancle.clicked.connect(self.CancleTxf)

    def message(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setText(message)
        mssg.exec_()

    def SendTransfer(self):
        import sqlite3

        # Create a connection to the BANKNH database
        conn = sqlite3.connect("BankNH.db")
        cur = conn.cursor()

        # Create the NEW table if it doesn't exist
        create_new_table_sql = """
        CREATE TABLE IF NOT EXISTS NEWT (
            SENDER TEXT,
            RECEIVER TEXT,
            TTYPE TEXT,
            AMOUNT REAL,
            SENDEROLDBAL REAL,
            SENDERNEWBAL REAL,
            RECOLDBAL REAL,
            RECNEWBAL REAL
        );
        """

        cur.execute(create_new_table_sql)

        # Get user input
        sender_username = self.lineEdit_name2txf.text()
        amount_str = self.lineEdit_amount2txf.text()
        receiver_username = self.lineEdit_number2txf.text()
        selected_type = self.comboBox_accountType.currentText()

        try:
            # Check if the sender's username exists in the database
            cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (sender_username,))
            sender_data = cur.fetchone()

            if sender_data is not None:
                # Get sender's balance
                sender_balance = sender_data[-1]

                # Convert amount to a float and check if it's a valid number
                try:
                    amount = float(amount_str)
                    if amount <= 0:
                        raise ValueError("Invalid amount")
                except ValueError:
                    self.message('Invalid Amount', 'Please enter a valid positive amount.')
                    conn.close()
                    return

                # Check if the sender has sufficient balance
                if sender_balance >= amount:
                    # Deduct the amount from the sender's balance
                    sender_balance -= amount

                    # Update sender's balance in the database

                    # Check if the receiver's username exists in the database
                    cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (receiver_username,))
                    receiver_data = cur.fetchone()

                    if receiver_data is not None:
                        # Get receiver's balance
                        receiver_balance = receiver_data[1]

                        # Add the amount to the receiver's balance
                        receiver_balance += amount

                        # Update receiver's balance in the database
                        cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?", (sender_balance, sender_username))

                        cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?",
                                    (receiver_balance, receiver_username))

                        # Commit the changes to the database
                        conn.commit()
                        # Insert the transaction data into the BANKMT table
                        cur.execute("""
                            INSERT INTO NEWT (SENDER, RECEIVER, TTYPE, AMOUNT, SENDEROLDBAL, SENDERNEWBAL, RECOLDBAL, RECNEWBAL)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                            sender_username,
                            receiver_username,
                            selected_type,
                            amount,
                            sender_balance + amount,  # SENDERNEWBAL
                            sender_balance,  # SENDEROLDBAL
                            receiver_balance - amount,  # RECOLDBAL
                            receiver_balance  # RECNEWBAL
                        ))
                        print("Transaction Data:")
                        print(f"Sender: {sender_username}")
                        print(f"Receiver: {receiver_username}")
                        print(f"Amount: {amount}")
                        print(f"Sender Old Balance: {sender_balance}")
                        print(f"Sender New Balance: {sender_balance - amount}")
                        print(f"Receiver Old Balance: {receiver_balance}")
                        print(f"Receiver New Balance: {receiver_balance + amount}")
                        # Commit the changes to the BANKMT database
                        conn.commit()
                        sendernew = sender_balance - amount
                        receivernew = receiver_balance + amount

                        list = [random.randint(0, 9), selected_type, amount,sender_balance, sendernew, receiver_balance, receivernew]
                        print(list)
                        # Show a success message
                        self.load(list)
                    else:
                        # Show an error message for receiver not found
                        self.message('Receiver Not Found', 'Receiver username not found.')
                else:
                    # Show an error message for insufficient balance
                    self.message('Insufficient Balance', 'You have insufficient balance for this transfer.')
            else:
                # Show an error message for sender not found
                self.message('Sender Not Found', 'Sender username not found.')

            # Debugging: Print sender and receiver usernames for troubleshooting
            print(f"Sender Username: {sender_username}")
            print(f"Receiver Username: {receiver_username}")

        except sqlite3.Error as e:
            self.message('Database Error', str(e))
        finally:
            conn.close()

    def CancleTxf(self):
        self.transfer.close()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def SendTxf(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def pipeline(self, df):
        num_feats = df.drop(["type"], axis=1)
        num_feats_pipe = Pipeline([
            ("scaler", MinMaxScaler())
        ])
        num_feats_preprocessing = num_feats_pipe.fit_transform(num_feats)
        # cat_feats
        cat_feats = df[["type"]]
        cat_feats_pipe = Pipeline([
            ("encoder", OneHotEncoder())
        ])
        cat_feats_preprocessed = cat_feats_pipe.fit_transform(cat_feats)
        num_list = list(num_feats)
        # print(num_list)
        cat_list = list(cat_feats)
        # print(cat_list)

        final_pipeline = ColumnTransformer([
            ("num", num_feats_pipe, num_list),
            ("cat", cat_feats_pipe, cat_list)
        ])
        row_preprocessed = final_pipeline.fit_transform(df)
        return row_preprocessed

    def load(self, list):
        df = pd.DataFrame([list])
        df.rename(columns={0:'count', 1:'type',2: 'amount', 3:'oldbalanceOrig',4: 'newbalanceOrig',
                                   5:'oldbalanceDest',6: 'newbalanceDest'}, inplace=True)
        print(df)
        loaded_model = joblib.load("banking_app_rf.pkl")
        self.pipeline(df)
        prediction = loaded_model.predict(self.pipeline(df))
        if prediction == 1:
            message = 'Invalid Amount. Please enter a valid positive amount.'
        else:
            message = 'Transaction done.'

        app = QApplication(sys.argv)

        # Display the message using QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle('Transaction Result')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        # Exit the application
        sys.exit(app.exec_())

    # def update_table(self):
    #     conn = sqlite3.connect('BankNH.db')
    #     cur = conn.cursor()
    #     sender_username = self.lineEdit_name2txf.text()
    #     amount = self.lineEdit_amount2txf.text()
    #     receiver_username = self.lineEdit_number2txf.text()
    #     selected_type = self.comboBox_accountType.currentText()
    #     cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (sender_username,))
    #     sender_balance = cur.fetchone()
    #     cur.execute("SELECT USERNAME, BAL FROM NEWBANK WHERE USERNAME = ?", (receiver_username,))
    #     receiver_balance = cur.fetchone()
    #
    #     cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?", (sender_balance, sender_username))
    #
    #     cur.execute("UPDATE NEWBANK SET BAL = ? WHERE USERNAME = ?",
    #                 (receiver_balance, receiver_username))
    #
    #     # Commit the changes to the database
    #     conn.commit()
    #     # Insert the transaction data into the BANKMT table
    #     cur.execute("""
    #         INSERT INTO NEWT (SENDER, RECEIVER, TTYPE, AMOUNT, SENDEROLDBAL, SENDERNEWBAL, RECOLDBAL, RECNEWBAL)
    #         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    #     """, (
    #         sender_username,
    #         receiver_username,
    #         selected_type,
    #         amount,
    #         sender_balance + amount,  # SENDERNEWBAL
    #         sender_balance,  # SENDEROLDBAL
    #         receiver_balance - amount,  # RECOLDBAL
    #         receiver_balance  # RECNEWBAL
    #     ))
    #     conn.commit()
    #     conn.close()


    def retranslateUi(self, TransferWindow):
        _translate = QtCore.QCoreApplication.translate
        TransferWindow.setWindowTitle(_translate("TransferWindow", "Transfer"))
        self.label_amount2txf.setText(_translate("TransferWindow", "ENTER AMOUNT TO DEPOSIT"))
        self.label_name2txf.setText(_translate("TransferWindow", "Sender username"))
        self.label_number2txf.setText(_translate("TransferWindow", "Receiver username"))
        self.comboBox_accountType.setItemText(0, _translate("TransferWindow", "Type"))
        self.comboBox_accountType.setItemText(1, _translate("TransferWindow", "CASH_OUT"))
        self.comboBox_accountType.setItemText(2, _translate("TransferWindow", "TRANSFER"))
        self.comboBox_bankType.setItemText(0, _translate("TransferWindow", "Choose Bank Name Below"))
        self.comboBox_bankType.setItemText(1, _translate("TransferWindow", "FirstBank"))
        self.comboBox_bankType.setItemText(2, _translate("TransferWindow", "GTB"))
        self.comboBox_bankType.setItemText(3, _translate("TransferWindow", "STABIC"))
        self.comboBox_bankType.setItemText(4, _translate("TransferWindow", "POLARIS"))
        self.comboBox_bankType.setItemText(5, _translate("TransferWindow", "FCMB"))
        self.comboBox_bankType.setItemText(6, _translate("TransferWindow", "ACCESS"))
        self.comboBox_bankType.setItemText(7, _translate("TransferWindow", "Others"))
        self.pushButton_transferTransfer.setText(_translate("TransferWindow", "TRANSFER"))
        self.pushButton_transferCancle.setText(_translate("TransferWindow", "CANCEL"))
        # self.pushButton_transferTransfer.setText(_translate("TransferWindow", "TRANSFER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransferWindow = QtWidgets.QMainWindow()
    ui = Ui_TransferWindow()
    ui.setupUi(TransferWindow)
    TransferWindow.show()

    sys.exit(app.exec_())

