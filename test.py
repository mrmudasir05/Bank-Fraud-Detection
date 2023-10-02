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

def pipeline(df):

    #numerical feats

    num_feats = df.drop(["type"], axis=1)
    num_feats_pipe=Pipeline([
        ("scaler",MinMaxScaler())
    ])
    num_feats_preprocessing=num_feats_pipe.fit_transform(num_feats)
    #cat_feats
    cat_feats=df[["type"]]
    cat_feats_pipe=Pipeline([
        ("encoder",OneHotEncoder())
    ])
    cat_feats_preprocessed=cat_feats_pipe.fit_transform(cat_feats)
    num_list=list(num_feats)
    #print(num_list)
    cat_list=list(cat_feats)
    #print(cat_list)

    final_pipeline=ColumnTransformer([
        ("num",num_feats_pipe,num_list),
        ("cat",cat_feats_pipe,cat_list)
    ])
    row_preprocessed=final_pipeline.fit_transform(df)
    return row_preprocessed

def fetch_data_from_NEWt():
    try:
        # Connect to the BANKNH database
        conn = sqlite3.connect("BANKNH.db")

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute a SQL query to fetch specific columns from the NEWt table
        cursor.execute("SELECT TTYPE, AMOUNT, SENDEROLDBAL, SENDERNEWBAL, RECOLDBAL, RECNEWBAL FROM NEWT")

        # Fetch all rows from the result set into a list of tuples
        data_list = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Return the fetched data
        return data_list

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []

# Call the function to fetch data from the NEWt table
fetched_data = fetch_data_from_NEWt()
j = list(fetched_data[-1])
i = random.randint(0,9)
j.insert(0,i)

# a = [0,"TRANSFER",900,0,80,70,0]
df= pd.DataFrame([j] , columns=['count','type','amount','	oldbalanceOrig','newbalanceOrig','oldbalanceDest	','newbalanceDest'])

loaded_model = joblib.load("banking_app_rf.pkl")

prediction=loaded_model.predict(pipeline(df))
if prediction == 1:
    message = 'Invalid Amount. Please enter a valid positive amount.'
else:
    message = 'Transaction done.'

# Create a PyQt application
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
