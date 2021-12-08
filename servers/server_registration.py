import socket, threading, sqlite3, os


def registration(data, conn, con, c):
    check = c.execute("""SELECT * From login_data Where login = ?""", (data[2],))
    check = c.fetchone()
    if check is None:
        path = os.path.abspath("avatar.png")
        c.execute("INSERT INTO login_data VALUES (?,?,?)", (data[2], data[4], path))
        conn.send(("Зарегистрирован").encode('utf-8'))
        print("Зарегистрирован")
        con.commit()
    else:
        conn.send("Такой пользователь уже существует".encode('utf-8'))



def login(data, conn, con, c):
    dat = c.execute("SELECT password FROM login_data WHERE login = ?", (data[2],))
    dat = c.fetchone()
    if dat is not None:
        d = dat[0]
        print(dat)
        if d == data[4]:
            conn.send("Вход выполнен".encode('utf-8'))
        else:
            conn.send("Пароль неверен".encode('utf-8'))
    else:
        conn.send("Такого пользователя не существует".encode('utf-8'))


def join_clients(sock, a, users, con, c):
    while True:
        conn, addr = sock.accept()
        print('Connected to :', addr[0], ':', addr[1])
        thread_1 = threading.Thread(target=receive, args=(conn, "helo", addr, users, con, c))
        thread_1.start()


def receive(conn, a, addr, users, con, c):
    while True:
        data = conn.recv(1024).decode('utf-8').split()
        users[addr] = conn
        if not data:
            print("NO")
            break
        if 'reg' in data:
            registration(data, conn, con, c)
        else:
            if 'log' in data:
                login(data, conn, con, c)


def Main():
    users = {}
    host = '127.0.0.1'
    port = 8080
    con = sqlite3.connect("login_data.db", check_same_thread=False)
    c = con.cursor()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(10)
    print("socket is listening")
    thread = threading.Thread(target=join_clients, args=(s, "helo", users, con, c))
    thread.start()


if __name__ == '__main__':
    Main()