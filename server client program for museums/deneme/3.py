import sqlite3
# table creates function for places in database

def fill_Places():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()

    sql_command = """CREATE TABLE places (  
        hp_Code INTEGER PRIMARY KEY,
        hp_Name VARCHAR(30),
        city_code INTEGER , 
        hp_Manager INTEGER 
            
        );"""

    crsr.execute(sql_command)
    x = 1
    sql_command = """INSERT INTO places (hp_Code,hp_Name,city_code,hp_Manager) VALUES (? , ?, ?, ?);"""
    crsr.execute(sql_command,(x,"Othello Castle",1,1001))
    sql_command = """INSERT INTO places VALUES (2 , "St. Barnabas Monastery", 1, 1002);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (3 , "St. Hilarion Castle", 2, 1003);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (4 , "Bellapais Abbey", 2, 1004);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (5 , "Guzelyurt Museum ", 3, 1005);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (6 , "St. Mamas Monastery", 3, 1006);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (7 , "Apostolos Andreas Monastery", 4, 1007);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (8 , "Kantara Castle", 4, 1008);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (9 , "Soli", 5, 1009);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (10 , "Vouni Palace", 5, 1010);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (11 , "St. Sophia Cathedral", 6, 1011);"""
    crsr.execute(sql_command)
    sql_command = """INSERT INTO places VALUES (12 , "Dervis Pasa Mansion", 6, 1012);"""
    crsr.execute(sql_command)

    connection.commit()

    connection.close()


fill_Places()