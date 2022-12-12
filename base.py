import pymysql
import os
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import date, timedelta
import datetime

host = 'localhost'
user = 'root'
password = ''
database = ''

# exec(open("./script.py").read())

def rel_path(relative_path):
    TEST_FILENAME = os.path.join(os.path.dirname(__file__), ("images/" + relative_path))
    return TEST_FILENAME

def InsertData():

    def Add_Book(accession, title, isbn, publisher, year, *authors):
                connection = create_db_connection(host, user, password, database)


                q1 = f"""
                INSERT INTO Book (
                    AccessionNO, 
                    Year, 
                    Title, 
                    Publisher, 
                    Isbn)
                VALUES ("{accession}", "{year}", "{title}", "{publisher}", "{isbn}");
                """
                execute_query_no_error(connection, q1)

                for author in authors:
                    q2 = f"""
                    INSERT INTO BookAuthors (
                        Author, 
                        AccessionNO)
                    VALUES ("{author}", "{accession}");
                    """
                    if author:
                        execute_query_no_error(connection, q2)

                connection.close()

                return

    def Add_Member(id, name, faculty, phone, email):

        q1 = f"""
        INSERT INTO Member (
            MembershipID, 
            Name,
            Faculty, 
            PhoneNumber, 
            EmailAddress)
        VALUES ('{id}', '{name}', '{faculty}', '{phone}', '{email}')
        """

        connection = create_db_connection(host, user, password, database)
        execute_query_no_error(connection, q1)
        connection.close()

        return


    with open(rel_path('../data/LibBooks.txt')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            Add_Book(row[0], row[1], row[5], row[6], row[7], row[2], row[3], row[4])

    with open(rel_path('../data/LibMems.txt')) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            Add_Member(row[0], row[1], row[2], row[3], row[4])

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name, user=user_name, password=user_password, database=db_name)
        print("MySQL Database connection successful")
    except pymysql.Error as e:
        print(f"Error: '{e}'")
    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pymysql.Error as e:
        print(f"Error: '{e}'")

def read_query1(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except pymysql.Error as e:
        print(f"Error: '{e}'")

def output_to_list(output):
    '''Converts read_query output to a list of lists'''
    from_db = []
    for row in output:
        row = list(row)
        from_db.append(row)
    return from_db

def execute_query(connection, query, success_message, failure_message):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
        messagebox.showinfo("Success", message=success_message)
    except pymysql.Error as e:
        print(f"Error: '{e}'")
        messagebox.showerror("Failure", message=failure_message)

def execute_query_no_error(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except pymysql.Error as e:
        print(f"Error: '{e}'")

def execute_list_query(connection, query, value):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, value)
        connection.commit()
        print("Query Successful")
    except pymysql.Error as e:
        print(f"Error: '{e}'")

def execute_list_query(connection, query, value):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, value)
        connection.commit()
        print("Query Successful")
    except pymysql.Error as e:
        print(f"Error: '{e}'")

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func





