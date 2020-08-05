import sqlite3
from tkinter import *
import socket


def operation():
    global n_dt #these variables are the inputs for the statistics
    global n_m
    global n_v
    global n_l
    global n_f
    global n_t
    global n_dt_v
    global n_m_v
    global n_v_v
    global n_l_v
    global n_f_v
    global n_t_v
    n_m_v = StringVar() #get inputs
    n_v_v = StringVar()
    n_l_v = StringVar()
    n_f_v = StringVar()
    n_t_v = StringVar()
    n_dt_v =StringVar()
    global operation_screen
    operation_screen = Toplevel(login_screen)
    operation_screen.title("Login")
    operation_screen.geometry("400x350")
    Label(operation_screen, text="Number of Visitors").pack()
    n_v = Entry(operation_screen, textvariable=n_v_v)
    n_v.pack()
    Label(operation_screen, text="Number of Nake Visitors").pack()
    n_m = Entry(operation_screen, textvariable=n_m_v)
    n_m.pack()
    Label(operation_screen, text="Number of Female Visitors").pack()
    n_f = Entry(operation_screen, textvariable=n_f_v)
    n_f.pack()
    Label(operation_screen, text="Number of Local Visitors").pack()
    n_l = Entry(operation_screen, textvariable=n_l_v)
    n_l.pack()
    Label(operation_screen, text="Number of Tourists").pack()
    n_t = Entry(operation_screen, textvariable=n_t_v)
    n_t.pack()
    Label(operation_screen, text="Date").pack()
    n_dt = Entry(operation_screen, textvariable=n_dt_v)
    n_dt.pack()
    Label(operation_screen, text="").pack()
    Button(operation_screen, text="Send Statitics", width=10, height=1, command=send_to_server).pack()

def send_to_server(): #sending statitics to the server

    print(n_v.get())
    print(n_m.get())
    print(n_f.get())
    print(n_l.get())
    print(n_t.get())
    array = []
    array.append("b")
    array.append(n_v.get())
    array.append(n_m.get())
    array.append(n_f.get())
    array.append(n_l.get())
    array.append(n_t.get())
    array.append(n_dt.get())

    find_manager()

    array.append(hm)

    print(array)
    array = repr(array)
    client.sendall(bytes(array, 'UTF-8'))

    servermsg = client.recv(2048).decode()
    global confirm_screen #confirmation or error screen
    confirm_screen = Toplevel(operation_screen)
    confirm_screen.title("Confirm")
    Label(confirm_screen, text=servermsg).pack()
    check_tourist_table()

def check_tourist_table():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()
    sql_command = 'SELECT * FROM tourists  '
    crsr.execute(sql_command)
    ans = crsr.fetchall()




    connection.commit()
    connection.close()
    print(ans)

def login(): #check login function
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



def find_manager():
    connection = sqlite3.connect("myDB.db")

    crsr = connection.cursor()
    crsr.execute("SELECT * FROM staffs where role = 'hpm'  ")
    ans = crsr.fetchall()

    connection.commit()

    connection.close()

    global hm
    #ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get())
    for i in range(len(ans)):
        if ans[i][1] == username_login_entry.get() and ans[i][2] == int(password_login_entry.get()) :
           hm = ans[i][0]


    return 0

def login_verify(): #check login function
    b = ["a", username_login_entry.get(), password_login_entry.get()]

    a = "a" + str(len(username_login_entry.get())) + str(
        len(password_login_entry.get())) + username_login_entry.get() + password_login_entry.get()

    client.sendall(bytes(a, 'UTF-8'))
    servermsg = client.recv(2048).decode()

    if servermsg == "1":
        login_success()
    else:
        user_not_found()




def login_success(): #if login sucsess open main screen
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=operation).pack()




def user_not_found():#if password and id not match then open error screen
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("240x100")
    Label(user_not_found_screen, text="Invalid username or Password ").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()




def delete_login_success():#destroy error screen
    login_success_screen.destroy()





def delete_user_not_found_screen():#destroy error screen
    user_not_found_screen.destroy()


SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))


check_tourist_table()
login()
