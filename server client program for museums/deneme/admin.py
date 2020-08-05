import sqlite3
import marshal
from tkinter import *
import socket
from pickle import dump
def operation(): # operation screen for admin
    global operation_screen
    operation_screen = Toplevel(login_screen)
    operation_screen.title("Login")
    operation_screen.geometry("400x350")

    Button(operation_screen, text="The historical place with the maximum number of visitors", command=ope_5, height=2,
           width=100).pack()
    Button(operation_screen, text="The city with the maximum number of visitors", command=ope_4, height=2,
           width=100).pack()
    Button(operation_screen, text="Tourists for each city", command=ope_3, height=2, width=100).pack()
    Button(operation_screen, text="Historical place details in a City", command=ope_2, height=2, width=100).pack()
    Button(operation_screen, text="Historical place details on a specific date", command=ope_1, height=2,
           width=100).pack()


def ope_1(): # displaying historical place details function
    global ope_1_screen
    ope_1_screen = Toplevel(operation_screen)
    ope_1_screen.title("Enter")
    ope_1_screen.geometry("300x250")
    global hp
    global hp_ope
    global date
    global date_ope

    hp_ope = StringVar()
    date_ope = StringVar()
    Label(ope_1_screen, text="Place * ").pack()
    hp = Entry(ope_1_screen, textvariable=hp_ope)
    hp.pack()
    Label(ope_1_screen, text="Date * ").pack()
    date = Entry(ope_1_screen, textvariable=date_ope)
    date.pack()
    Button(ope_1_screen, text="Login", width=10, height=1, command=ope_1_print).pack()
    print(hp.get())

def ope_1_print(): #this function prints the information taken from server
    x=hp.get()
    y=date.get()
    a = []
    a.append("i")
    a.append(x)
    a.append(y)
    a = repr(a)
    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()
    if(servermsg=="error"): # if invalid search print error messega
        servermsg = "There is no places as you searched"
        servermsg1 = "Unfortunately : "
        global error_screen_1
        error_screen_1 = Toplevel(ope_1_screen)
        error_screen_1.title("Error")
        error_screen_1.geometry("350x50")
        Label(error_screen_1, text=servermsg1).pack()
        Label(error_screen_1, text=servermsg).pack()
    else: # else display information
        servermsg = eval(servermsg)
        print(servermsg)
        v=1
        m=1
        l=1
        f=1
        t=1
        global ope_1_print_screen

        ope_1_print_screen = Toplevel(ope_1_screen)
        ope_1_screen.title("Historical Place Details")
        ope_1_screen.geometry("300x250")
        Label(ope_1_print_screen, text=x).pack()
        Label(ope_1_print_screen, text="V="+str(servermsg[1])+" M="+str(servermsg[2])+" L="+str(servermsg[3])+" F="+str(servermsg[4])+" T="+str(servermsg[5])).pack()
        Label(ope_1_print_screen, text="\n").pack()
        Label(ope_1_print_screen, text="V = Number of Visitors").pack()
        Label(ope_1_print_screen, text="M = Number of Male Visitors").pack()
        Label(ope_1_print_screen, text="L = Number of Local Visitors").pack()
        Label(ope_1_print_screen, text="F = Number of Female Visitors").pack()
        Label(ope_1_print_screen, text="T = Number of Tourists").pack()

def ope_2(): # display historical place details function
    global ope_2_screen
    ope_2_screen = Toplevel(operation_screen)
    ope_2_screen.title("Enter")
    ope_2_screen.geometry("300x250")
    global city
    global city_ope
    city_ope = StringVar()
    Label(ope_2_screen, text="City * ").pack()
    city = Entry(ope_2_screen, textvariable=city_ope)
    city.pack()
    Button(ope_2_screen, text="Login", width=10, height=1, command=ope_2_input).pack()


def ope_2_input(): # the function takes input for ope_2
    b= []
    b.append("q")
    b.append(city_ope.get())
    b = repr(b)
    client.sendall(bytes(b, 'UTF-8'))
    servermsg = client.recv(2048).decode()
    #
    print(servermsg)
    if(servermsg=="error"): #if invalid search , then display error
        servermsg = "There is no city as you searched"
        servermsg1 = "Unfortunately : "
        global error_screen
        error_screen = Toplevel(ope_2_screen)
        error_screen.title("Error")
        error_screen.geometry("350x50")
        Label(error_screen, text=servermsg1).pack()
        Label(error_screen, text=servermsg).pack()

    else: # else display information
        servermsg = eval(servermsg)
        global ope_2_input_screen
        ope_2_input_screen = Toplevel(ope_2_screen)
        ope_2_input_screen.title(city_ope.get())
        ope_2_input_screen.geometry("250x380")
        Label(ope_2_input_screen, text=("Historical Place details in "+city_ope.get())).pack()
        Label(ope_2_input_screen, text="\n").pack()
        Label(ope_2_input_screen, text=servermsg[0][0]).pack()
        Label(ope_2_input_screen,
              text="V=" + str(servermsg[0][1]) + " M=" + str(servermsg[0][2]) + " L=" + str(servermsg[0][3]) + " F=" + str(servermsg[0][4]) + " T=" + str(
                  servermsg[0][5])).pack()
        Label(ope_2_input_screen, text="\n").pack()
        Label(ope_2_input_screen, text=servermsg[1][0]).pack()
        Label(ope_2_input_screen,
              text="V=" + str(servermsg[1][1]) + " M=" + str(servermsg[1][2]) + " L=" + str(servermsg[1][3]) + " F=" + str(
                  servermsg[1][4]) + " T=" + str(
                  servermsg[1][5])).pack()
        Label(ope_2_input_screen, text="\n").pack()
        Label(ope_2_input_screen, text="V = Number of Visitors").pack()
        Label(ope_2_input_screen, text="M = Number of Male Visitors").pack()
        Label(ope_2_input_screen, text="L = Number of Local Visitors").pack()
        Label(ope_2_input_screen, text="F = Number of Female Visitors").pack()
        Label(ope_2_input_screen, text="T = Number of Tourists").pack()


def ope_3():# display cities function
    a="3"
    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()
    print(servermsg)
    v = eval(servermsg)
    print(len(v))
    global ope_3_screen
    ope_3_screen = Toplevel(operation_screen)
    ope_3_screen.title("Cities")
    ope_3_screen.geometry("300x450")
    Label(ope_3_screen, text="Gazimagusa").pack()
    Label(ope_3_screen,text="V=" + str(v[0][0]) + " M=" + str(v[0][1]) + " L=" + str(v[0][2]) + " F=" + str(v[0][3]) + " T=" + str(v[0][4])).pack()
    Label(ope_3_screen, text="Girne").pack()
    Label(ope_3_screen,text="V=" + str(v[1][0]) + " M=" + str(v[1][1]) + " L=" + str(v[1][2]) + " F=" + str(v[1][3]) + " T=" + str(v[1][4])).pack()
    Label(ope_3_screen, text="Guzelyurt").pack()
    Label(ope_3_screen,text="V=" + str(v[2][0]) + " M=" + str(v[2][1]) + " L=" + str(v[2][2]) + " F=" + str(v[2][3]) + " T=" + str(v[2][4])).pack()
    Label(ope_3_screen, text="Iskele").pack()
    Label(ope_3_screen,text="V=" + str(v[3][0]) + " M=" + str(v[3][1]) + " L=" + str(v[3][2]) + " F=" + str(v[3][3]) + " T=" + str(v[3][4])).pack()
    Label(ope_3_screen, text="Lefke").pack()
    Label(ope_3_screen,text="V=" + str(v[4][0]) + " M=" + str(v[4][1]) + " L=" + str(v[4][2]) + " F=" + str(v[0][3]) + " T=" + str(v[4][4])).pack()
    Label(ope_3_screen, text="Lefkosa").pack()
    Label(ope_3_screen,text="V=" + str(v[5][0]) + " M=" + str(v[5][1]) + " L=" + str(v[5][2]) + " F=" + str(v[5][3]) + " T=" + str(v[5][4])).pack()
    Label(ope_3_screen, text="\n").pack()
    Label(ope_3_screen, text="V = Number of Visitors").pack()
    Label(ope_3_screen, text="M = Number of Male Visitors").pack()
    Label(ope_3_screen, text="L = Number of Local Visitors").pack()
    Label(ope_3_screen, text="F = Number of Female Visitors").pack()
    Label(ope_3_screen, text="T = Number of Tourists").pack()







def ope_4(): # display most crowded city function
    a="2"
    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()
    if(servermsg=="error"):
        servermsg="There is no visitors for any cities"
        servermsg1 = "Unfortunately : "
    else:
        servermsg= servermsg[2:(len(servermsg)-3)]
        servermsg1="The city with the maximum number of visitors is :"
    global ope_4_screen
    ope_4_screen = Toplevel(operation_screen)
    ope_4_screen.title("Cities")
    ope_4_screen.geometry("350x50")
    Label(ope_4_screen, text=servermsg1).pack()
    Label(ope_4_screen, text=servermsg).pack()



def ope_5(): #display most crowded place function

    a="1"
    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()
    if (servermsg == "error"):
        servermsg = "There is no visitors for any places"
        servermsg1 = "Unfortunately : "
    else:
        servermsg = servermsg[2:(len(servermsg) - 3)]
        servermsg1 = "The place with the maximum number of visitors is :"
    global ope_5_screen
    ope_5_screen = Toplevel(operation_screen)
    ope_5_screen.title("Cities")
    ope_5_screen.geometry("350x50")
    Label(ope_5_screen, text=servermsg1).pack()
    Label(ope_5_screen, text=servermsg).pack()



def just_print():
    print("yp90")


def login():#check login function
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()


    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

    login_screen.mainloop()


# Implementing event on register button


# Implementing event on login button
"""
def find_admin():# i didnt use this function
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()
    crsr.execute("SELECT * FROM staffs where role = 'admin'  ")
    ans = crsr.fetchall()
    print(ans)
    print(username_login_entry.get())
    print(password_login_entry.get())
    #ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get())
    for i in range(len(ans)):
        if ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get()):

            return 1

    return 0
"""
def login_verify(): #send login details to the server and take input
    b = ["0",username_login_entry.get(),password_login_entry.get()]

    a = "0"+str(len(username_login_entry.get()))+str(len(password_login_entry.get()))+username_login_entry.get()+password_login_entry.get()

    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()

    if servermsg == "1":
        login_success()
    else:
        user_not_found()




def login_success():#if login success open this screen
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=operation).pack()



"""
def password_not_recognised():#else invalid password function
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
"""



def user_not_found(): #
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("240x100")
    Label(user_not_found_screen, text="Invalid username or password !").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()




def delete_login_success():
    login_success_screen.destroy()

"""
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
"""

def delete_user_not_found_screen():
    user_not_found_screen.destroy()


SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

login()
