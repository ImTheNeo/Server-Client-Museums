
import sqlite3
#table create function for cities in database


def fill_Cities():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()


    sql_command = """CREATE TABLE cities (  
    city_code INTEGER PRIMARY KEY,  
    city_name VARCHAR(20)
    );"""

    crsr.execute(sql_command)


    sql_command = """INSERT INTO cities VALUES (1 , "Gazimagusa");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO cities VALUES (2 , "Girne");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO cities VALUES (3 , "Guzelyurt");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO cities VALUES (4 , "Iskele");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO cities VALUES (5 , "Lefke");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO cities VALUES (6 , "Lefkosa");"""
    crsr.execute(sql_command)


    connection.commit()


    connection.close()




fill_Cities()







