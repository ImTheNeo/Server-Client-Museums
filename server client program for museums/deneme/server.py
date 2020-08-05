import socket, threading
import sqlite3
import string


def login_search_admin(msg):# search for the login function
    un_length = msg[1]
    pw_length = msg[2]
    user_name = msg[3:(3 + int(un_length))]
    pw = msg[3 + int(un_length):]
    connection = sqlite3.connect("myDB.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM staffs where role = 'admin'  ")
    ans = crsr.fetchall()
    connection.commit()

    connection.close()
    # ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get())
    for i in range(len(ans)):
        if ans[i][1] == user_name and ans[i][2] == int(pw):
            return 1

    return 0


def display_cities():#display cities function
    connection = sqlite3.connect("myDB.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM tourists ")#take everything from tourists
    ans = crsr.fetchall()
    connection.commit()
    print(ans)
    connection.close()
    sum_ar = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for i in range(len(ans)):#then search for the historical place manager code
        if ans[i][5] < 1003:
            for j in range(5):
                sum_ar[0][j] = sum_ar[0][j] + ans[i][j]
        elif ans[i][5] < 1005:
            for j in range(5):
                sum_ar[1][j] = sum_ar[1][j] + ans[i][j]
        elif (ans[i][5] < 1007):
            for j in range(5):
                sum_ar[2][j] = sum_ar[2][j] + ans[i][j]

        elif (ans[i][5] < 1009):
            for j in range(5):
                sum_ar[3][j] = sum_ar[3][j] + ans[i][j]
        elif (ans[i][5] < 1011):
            for j in range(5):
                sum_ar[4][j] = sum_ar[4][j] + ans[i][j]
        else:
            for j in range(5):
                sum_ar[5][j] = sum_ar[5][j] + ans[i][j]

    print(sum_ar)

    b = repr(sum_ar)

    return b


def login_search_manager(msg):#search for the manager if it exists
    un_length = msg[1]
    pw_length = msg[2]
    user_name = msg[3:(3 + int(un_length))]
    pw = msg[3 + int(un_length):]
    connection = sqlite3.connect("myDB.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM staffs where role = 'hpm'  ")
    ans = crsr.fetchall()
    connection.commit()

    connection.close()
    # ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get())
    for i in range(len(ans)):
        if ans[i][1] == user_name and ans[i][2] == int(pw):
            return 1

    return 0


def update_tourists(msg):# update the statics for historical place
    msg = eval(msg)
    total = int(msg[1])
    male = int(msg[2])
    female = int(msg[3])
    local = int(msg[4])
    tour = int(msg[5])
    date = msg[6]
    staff = int(msg[7])
    if (total != male + female):
        return "Number of total should equal to male + female\n Please send the correct statitics again!"
    if (total != local + tour):
        return "Number of total should equal to local + tourist\n Please send the correct statitics again!"

    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()

    sql_command = """INSERT INTO tourists (no_of_local,no_of_tourist,no_of_male,no_of_female,staff,no_of_total,date) 
    VALUES (? , ?, ?, ?, ?, ?, ?); """
    my_tuple = (total, male, female, local, tour, staff, date)
    crsr.execute(sql_command, my_tuple)
    print("cikti")
    connection.commit()
    connection.close()

    return "Statics are send to the system sucsessfully"


def places_in_city(msg): #search the statics for the places in a city
    msg = eval(msg)
    cityname = msg[1]
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()
    print("1")
    crsr.execute("SELECT city_code FROM cities WHERE city_name=?", (cityname,))
    print("2")
    ans = crsr.fetchall()

    connection.commit()
    connection.close()
    print(len(ans))
    if (len(ans) == 0):

        return "error"
    print("3")
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()
    crsr.execute("SELECT * FROM places WHERE city_code=?", (ans[0][0],))
    print("4")
    ans = crsr.fetchall()
    print(ans)
    connection.commit()
    connection.close()

    sum_ar = [[ans[0][1], 0, 0, 0, 0, 0], [ans[1][1], 0, 0, 0, 0, 0]]

    print(sum_ar)

    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()


    a = ans[0][3]
    b = ans[1][3]

    crsr.execute("SELECT * FROM tourists ")
    ans3 = crsr.fetchall()#save all tourists into ans3
    print(ans3)
    staff = "staff"


    connection.commit()

    connection.close()
    print(ans3)
    print("30")
    for i in range(len(ans3)):
        print("1")
        if (ans3[i][5] == a):#if match
            print("2")
            for j in range(5):
                print("3")
                sum_ar[0][j + 1] = sum_ar[0][j + 1] + ans3[i][j]#find total
        if (ans3[i][5] == b):#if match
            print("4")
            for j in range(5):
                print("5")
                sum_ar[1][j + 1] = sum_ar[1][j + 1] + ans3[i][j]#find total

    print("here")
    print(sum_ar)
    ans3 = repr(sum_ar)#convert it to string

    return ans3


def tourist_in_date(msg): #given place and date tourist details
    msg = eval(msg)#convert it to tuple
    print(msg)
    place = msg[1]
    print(type(place))
    day = msg[2]
    print("60")
    connection = sqlite3.connect("myDB.db")
    cursor1 = connection.cursor()
    print("70")
    cursor1.execute("SELECT hp_Manager FROM places WHERE hp_Name='%s' " % (place,))#find the matches
    pl = cursor1.fetchall()
    if(len(pl)==0):#if no match
        return "error"

    place_1 = pl[0][0]
    print("no")
    cursor1.execute("SELECT * FROM tourists ")
    ans = cursor1.fetchall()
    sum_ar = [place, 0, 0, 0, 0, 0, day]
    print("cem")
    print(ans)
    for i in range(len(ans)):# if match sum them

        if (ans[i][5] == place_1 and ans[i][6] == day):
            for j in range(1, 6):
                sum_ar[j] = sum_ar[j] + ans[i][j - 1]
    print(sum_ar)
    sum_ar = repr(sum_ar) #convert it to string
    print("yo")
    connection.commit()
    connection.close()
    return sum_ar  #return


def find(ans, places): #finding most crowded place
    sum_ar = [[0, 0, 0, 0, 0, places[0]], [0, 0, 0, 0, 0, places[1]], [0, 0, 0, 0, 0, places[2]],
              [0, 0, 0, 0, 0, places[3]], [0, 0, 0, 0, 0, places[4]], [0, 0, 0, 0, 0, places[5]],
              [0, 0, 0, 0, 0, places[6]], [0, 0, 0, 0, 0, places[7]], [0, 0, 0, 0, 0, places[8]],
              [0, 0, 0, 0, 0, places[9]], [0, 0, 0, 0, 0, places[10]], [0, 0, 0, 0, 0, places[11]]]
    print(ans)
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][5])
    for i in range(len(ans)):
        print("3")
        if (ans[i][5] < 1002):
            print("1")
            sum_ar[0][0] = sum_ar[0][0] + ans[i][0]
        elif (ans[i][5] < 1003):
            print("2")
            sum_ar[1][0] = sum_ar[1][0] + ans[i][0]
        elif (ans[i][5] < 1004):
            sum_ar[2][0] = sum_ar[2][0] + ans[i][0]
        elif (ans[i][5] < 1005):
            sum_ar[3][0] = sum_ar[3][0] + ans[i][0]
        elif (ans[i][5] < 1006):
            sum_ar[4][0] = sum_ar[4][0] + ans[i][0]
        elif (ans[i][5] < 1007):
            print("3")
            sum_ar[5][0] = sum_ar[5][0] + ans[i][0]
        elif (ans[i][5] < 1008):
            sum_ar[6][0] = sum_ar[6][0] + ans[i][0]
        elif (ans[i][5] < 1009):
            sum_ar[7][0] = sum_ar[7][0] + ans[i][0]
        elif (ans[i][5] < 1010):
            sum_ar[8][0] = sum_ar[8][0] + ans[i][0]
        elif (ans[i][5] < 1011):
            sum_ar[9][0] = sum_ar[9][0] + ans[i][0]

        elif (ans[i][5] < 1012):
            sum_ar[10][0] = sum_ar[10][0] + ans[i][0]

        else:
            sum_ar[11][0] = sum_ar[11][0] + ans[i][0]

    crowded = sum_ar[0][0]
    crowded_n = 0
    for i in range(12):
        if (crowded < sum_ar[i][0]):
            print("girdi")
            crowded = sum_ar[i][0]
            crowded_n = i

    if (sum_ar[crowded_n][0] == 0): #if most crowded is zero there is no visitor in any city
        return "error"
    return sum_ar[crowded_n][5]


def find_crowded_place(): #finding most crowded place function
    print("yo")
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tourists ")

    ans = cursor.fetchall()
    print(ans)
    connection.commit()
    connection.close()
    print(ans)

    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT hp_Name FROM places")
    places = cursor.fetchall()
    connection.commit()
    print(ans)
    print(len(ans))
    connection.close()
    return find(ans, places)#return the place name


def find_crowded_city():
    connection = sqlite3.connect("myDB.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM tourists ")

    ans = crsr.fetchall()
    crsr.execute("SELECT city_name FROM cities")
    places = crsr.fetchall()
    connection.commit()
    print(ans)
    connection.close()
    sum_ar = [[0, 0, 0, 0, 0, places[0]], [0, 0, 0, 0, 0, places[1]], [0, 0, 0, 0, 0, places[2]],
              [0, 0, 0, 0, 0, places[3]], [0, 0, 0, 0, 0, places[4]], [0, 0, 0, 0, 0, places[5]]]

    for i in range(len(ans)):
        if ans[i][5] < 1003:
            for j in range(5):
                sum_ar[0][j] = sum_ar[0][j] + ans[i][j]
        elif ans[i][5] < 1005:
            for j in range(5):
                sum_ar[1][j] = sum_ar[1][j] + ans[i][j]
        elif (ans[i][5] < 1007):
            for j in range(5):
                sum_ar[2][j] = sum_ar[2][j] + ans[i][j]

        elif (ans[i][5] < 1009):
            for j in range(5):
                sum_ar[3][j] = sum_ar[3][j] + ans[i][j]
        elif (ans[i][5] < 1011):
            for j in range(5):
                sum_ar[4][j] = sum_ar[4][j] + ans[i][j]
        else:
            for j in range(5):
                sum_ar[5][j] = sum_ar[5][j] + ans[i][j]

    crowded = sum_ar[0][0]
    crowded_n = 0
    for i in range(6):
        if (crowded < sum_ar[i][0]):
            crowded = sum_ar[i][0]
            crowded_n = i

    if (sum_ar[crowded_n][0] == 0):#if most crowded is 0 then all are ampty
        return "error"

    return sum_ar[crowded_n][5] #return the city name


def checkope(msg):  #check operation function
    print("check ope de")

    if (msg[0] == 'a'): #search manager
        print("a da")
        if login_search_manager(msg):
            return 1
        else:
            return 0

    if (msg[0] == '0'): #search admin
        print("b de")
        if login_search_admin(msg):
            return 1
        else:
            return 0
    if (msg[0] == '1'): #search most crowded place
        print("place donuyor")
        return find_crowded_place()
    if (msg[0] == '2'): #search most crowded city
        print("2 donuyor")
        return find_crowded_city()
    if (msg[0] == '3'): #display cities
        print("city if icinde")
        return display_cities()
    if (msg[2] == 'b'):  #send statitics

        return update_tourists(msg)
    if (msg[2] == 'q'): #sarch places in city
        print("burada")
        return places_in_city(msg)
    if (msg[2] == 'i'): #search tourists in a place in given date
        return tourist_in_date(msg)

    print("0 donuyor")
    return 0


class ClientThread(threading.Thread): #server thread
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):

        try:
            print("Connection from : ", clientAddress)

            while True:
                data = self.csocket.recv(2048)
                msg = data.decode()
                if msg == 'bye':
                    break
                print("from client", msg)

                a = str(checkope(msg))
                self.csocket.send(bytes(a, 'UTF-8'))
            print("Client at ", clientAddress, " disconnected...")
        except:
            self.csocket.close()


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")
while True:
    try:
        server.listen(2)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
    except:

        print("thread kapandi")


