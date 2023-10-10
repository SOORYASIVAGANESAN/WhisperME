# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:15:46 2023

@author: Hp
"""

import pyodbc
import pandas as pd

# Connect to SQL Server
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=<YOUR SERVER>;DATABASE=<YOUR DATABASE>;UID=<YOUR USER ID>;PWD=<YOUR PASSWORD>')
previous_value = ""
while True:
    current_value = str(pd.read_sql_query('SELECT _check FROM change_table',cnxn)['_check'].tolist()[0])
    if current_value != previous_value:
        prev_value = current_value
        #Write your code here