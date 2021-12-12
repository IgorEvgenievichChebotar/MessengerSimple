import pickle
import socket
import sqlite3
import threading

from colorama import init, Fore

init(autoreset=True)


def Main():
    users = {}
    host = '127.0.0.1'
    port = 8888
    con = sqlite3.connect("login_data.db", check_same_thread=False)

    con.execute("PRAGMA journal_mode=WAL")

    c = con.cursor()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(10)
    print("socket is listening")
    thread = threading.Thread(target=join_clients, args=(s, users, c))
    thread.start()


def join_clients(sock, users, c):
    print("the _join_clients_ function has now started working")
    while True:
        conn, addr = sock.accept()
        print('Connected to :', addr[0], ':', addr[1])
        thread_1 = threading.Thread(target=receive, args=(conn, addr, users, c))
        thread_1.start()


def find(conn, c, data):
    print("the _find_ function has now started working")
    c.execute("SELECT login, link FROM login_data Where login Like ? ", ('%' + data + '%',))
    f = c.fetchall()
    lis = ""
    py = {}
    if f is not None:
        for x in range(0, len(f)):
            a = f[x]
            b = a[0]
            image = open(a[1], "rb")
            py[b] = image.read()
        lis = pickle.dumps(py)
    conn.send(lis)


def receive(conn, addr, users, c):
    print("the _receive_ function has now started working")
    while True:
        try:
            data = conn.recv(4096).decode('utf-8')

            print(Fore.GREEN + (str(addr[0]) + ' : ' + str(addr[1]) + " is online"))

            users[addr] = conn
            if not data:
                print("data empty")
                break
            else:
                threading.Thread(target=find, args=(conn, c, data)).start()
        except:

            print(Fore.RED + (str(addr[0]) + ' : ' + str(addr[1]) + " is offline"))

            break


if __name__ == '__main__':
    Main()