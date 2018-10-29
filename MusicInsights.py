#Let's first start this project by importing all the modules needed and
#then set up some helper functions. I think it would be best to create a
#context manager to handle the connection to the SQLite database. This could
#make life easier by having it take care of opening and closing the connection
#to the database, as well as making sure I don't acccidently make changes to
#the database if one of queries has an error.
import sqlite3
import pandas as pd
import numpy as np
import matplotlib as py
%matplotlib inline

db='chinook.db'

#Takes a SQL query as an argument and returns a 
#pandas dataframe of that query
def run_query(q):
    with sqlite3.connect(db) as conn:
        return pd.read_sql(q, conn)
    
#Takes a SQL command as an argument and 
#executes it using the sqlite module. The 'conn.isolation_Level=None'
# tells SQLite to autocommit any changes.
def run_command(c):
    with sqlite3.connect(db) as conn:
        conn.isolation_level = None
        conn.execute(c)
        
#Calls the run_query() function to return a list 
#of all tables and views in the database
def show_tables():
    q = '''
    SELECT
        name,
        type
    FROM sqlite_master
    WHERE type IN ("table","view");
    '''
    return run_query(q)

show_tables()