import sqlite3

#table creates function for tourists in database
def tourist_details():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()

    sql_command = """CREATE TABLE tourists (  
        no_of_local INTEGER,
        no_of_tourist INTEGER,
        no_of_male INTEGER,
        no_of_female INTEGER,
        staff INTEGER,
        no_of_total INTEGER,
        date VARCHAR(20)

        );"""
    crsr.execute(sql_command)

    connection.commit()


    connection.close()

tourist_details()