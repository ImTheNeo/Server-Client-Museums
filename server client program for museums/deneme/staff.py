import sqlite3

#table creates function for staffs in database

def fill_Staff():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()


    sql_command = """CREATE TABLE staffs (  
    staff_ID INTEGER PRIMARY KEY,  
    username VARCHAR(30),
    pw INTEGER,
    role VARCHAR(30)
    
    );"""

    crsr.execute(sql_command)

    sql_command = """INSERT INTO staffs VALUES (1001 , "1001HPM", 1234, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1002 , "1002HPM", 5678, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1003 , "1003HPM", 9123, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1004 , "1004HPM", 4567, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1005 , "1005HPM", 8912, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1006 , "1006HPM", 3456, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1007 , "1007HPM", 7891, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1008 , "1008HPM", 2345, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1009 , "1009HPM", 6789, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1010 , "1010HPM", 1234, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1011 , "1011HPM", 5678, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1012 , "1012HPM", 9123, "hpm");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1013 , "1013A", 4567, "admin");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1014 , "1014A", 8912, "admin");"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO staffs VALUES (1015 , "1015A", 3456, "admin");"""
    crsr.execute(sql_command)


    connection.commit()


    connection.close()




fill_Staff()