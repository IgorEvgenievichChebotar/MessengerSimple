import pathlib
import socket
import sqlite3
import threading


def Main():  # main func
    users = {}
    host = '127.0.0.1'
    port = 8080
    con = sqlite3.connect("login_data.db", check_same_thread=False)
    con.execute("PRAGMA journal_mode=WAL")
    c = con.cursor()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(10)
    print("socket is listening")
    thread = threading.Thread(target=join_clients, args=(s, "helo", users, con, c))
    thread.start()


def join_clients(sock, a, users, con, c):  # func for catching connections
    print("the _join_clients_ function has now started working")
    while True:
        conn, addr = sock.accept()
        print('Connected to :', addr[0], ':', addr[1])
        thread_1 = threading.Thread(target=receive, args=(conn, "helo", addr, users, con, c))
        thread_1.start()


def registration(data, conn, con, c):  # func for registrating user
    print("the _registration_ function has now started working")
    check = c.execute("""SELECT * From login_data Where login = ?""", (data[2],))
    check = c.fetchone()
    if check is None:
        path_file_dir = pathlib.Path.cwd().parent.joinpath('path_avatarka.log')
        path_file = open(path_file_dir, 'r')
        image_dir = path_file.read()
        print(image_dir)
        c.execute("INSERT INTO login_data VALUES (?,?,?)", (data[2], data[4], image_dir))
        conn.send(("Зарегистрирован").encode('utf-8'))
        print("Зарегистрирован")
        con.commit()
    else:
        conn.send("Такой пользователь уже существует".encode('utf-8'))


def login(data, conn, con, c):  # func for searching user in database and sending response to the client
    print("the _login_ function has now started working")
    dat = c.execute("SELECT password FROM login_data WHERE login = ?", (data[2],))
    dat = c.fetchone()
    if dat is not None:
        d = dat[0]
        if d == data[4]:
            conn.send("Вход выполнен".encode('utf-8'))
        else:
            conn.send("Пароль неверен".encode('utf-8'))
    else:
        conn.send("Такого пользователя не существует".encode('utf-8'))


def receive(conn, a, addr, users, con, c):  # func for catching data from client
    print("the _receive_ function has now started working")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8').split()
            users[addr] = conn
            if not data:
                break
            if 'reg' in data:
                registration(data, conn, con, c)
            else:
                if 'log' in data:
                    login(data, conn, con, c)
        except:
            print("connection: ", str(addr[0]) + ' : ' + str(addr[1]), " losted")
            break


if __name__ == '__main__':  # that protects users from accidentally invoking the script
    Main()