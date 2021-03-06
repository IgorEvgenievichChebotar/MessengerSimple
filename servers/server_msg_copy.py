import socket
import threading
import sqlite3
import pickle
import time


def Main():  # main func
    host = '127.0.0.1'
    port = 60005
    con = sqlite3.connect("login_data.db", check_same_thread=False)

    con.execute("PRAGMA journal_mode=WAL")

    connection = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(5)
    print("socket is listening")
    thread = threading.Thread(target=join_clients, args=(s, con, connection))
    thread.start()


def join_clients(sock, con, connection):  # func for catching connections
    print("the _join_clients_ function has now started working")
    while True:
        conn, addr = sock.accept()
        print('Connected to :', addr[0], ':', addr[1])
        thread_1 = threading.Thread(target=receive, args=(conn, sock, addr, con, connection))
        thread_1.start()


def save_dialog(con, data, conn, nam, m, f, connection, addr):  # func for saving dialog
    print("the _save_dialog_ function has now started working")
    c = con.cursor()
    c.execute("""SELECT name FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
    name = c.fetchone()[0]
    print("empty message")
    message = ' '.join(data[m + 1:])
    c.execute("""SELECT * from sqlite_master where type = 'table'""")
    tables = c.fetchall()

    table = ''
    for x in tables:
        if nam in (x[1]).split("_"):
            if name in (x[1]).split("_"):
                table = x[1]
                break
            else:
                table = ''
        else:
            table = ''
    if table == '':
        c.execute(
            """CREATE TABLE IF NOT EXISTS """ + "'" + name + '_' + nam + "'" + """(sender TEXT, receiver TEXT, message TEXT, status TEXT)""")
        table = str("'" + name + '_' + nam + "'")
        save_dialog(con, data, conn, nam, m, f, connection, addr)
    else:
        c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
        f = c.fetchall()
        c.execute("""SELECT * from sqlite_master where type = 'table'""")
        if f:  # executing when both are online
            message = data[m + 1:]
            msg = ' '.join(message)
            c.execute("""INSERT INTO """ + '{0}'.format("'" + table + "'") + """ Values (?,?,?,?)""",
                      (str(name), str(nam), str(msg), "1"), )
            c.execute("""SELECT * FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
            sender = c.fetchall()[0][0]
            c.execute("SELECT link FROM login_data Where login = ? ", (sender,))
            image = c.fetchone()[0]
            image = open(image, "rb")
            messages = {"sender:": sender,
                        "message:": msg,
                        "image:": image.read()}

            ip_port = f[-1][1]
            receiver = connection[ip_port]
            receiver.send(pickle.dumps(messages))
            c.close()
        else:  # executing when receiver are offline

            th = threading.Thread(target=checking_user,
                                  args=(nam, con, data, conn, name, message, m, connection, addr, table))
            th.start()


# func for checking user existence when he is offline
def checking_user(nam, con, data, conn, name, message, m, connection, addr, table):
    print("the _checking_user_ function has now started working")
    st = True
    while st:

        c = con.cursor()
        c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
        f = c.fetchall()
        time.sleep(1)

        if f:  # starts when the receiver is connected
            print("f statement is running")
            print("the receiver is online at this moment")
            message = data[m + 1:]
            msg = ' '.join(message)

            c.execute("""INSERT INTO {0} Values (?,?,?,?)""".format('{0}'.format('"' + table + '"')),
                      (str(name), str(nam), str(msg), "1"), )

            c.execute("""SELECT * FROM base_connection WHERE address = ?""",
                      ((str(addr[0]) + '_' + str(addr[1])),))
            sender = c.fetchall()[0][0]
            c.execute("SELECT link FROM login_data Where login = ? ",
                      (sender,))
            image = c.fetchone()[0]
            image = open(image, "rb")
            messages = {"sender:": sender,
                        "message:": msg,
                        "image:": image.read()}
            ip_port = f[0][1]
            try:
                receiver = connection[ip_port]
                receiver.send(pickle.dumps(messages))
                c.close()
                break
            except:
                checking_user(nam, con, data, conn, name, message, m, connection, addr, table)
        else:  # starts until the receiver goes connected
            print("the receiver is offline at this moment")
            save_dialog(con, data, conn, nam, m, f, connection, addr)
            break


def receive(conn, sock, addr, con, connection):  # func for catching data from client and working with database
    print("the _receive_ function has now started working")
    try:
        while True:
            data = conn.recv(40960000).decode('utf-8').split()
            if 'name:' in data:
                c = con.cursor()
                name = " ".join(data[1:])
                c.execute("""INSERT INTO base_connection VALUES (?,?)""", (name, (str(addr[0]) + '_' + str(addr[1])),))
                con.commit()
                ip_port = ('{0}_{1}'.format(str(addr[0]), str(addr[1])))
                connection[ip_port] = conn
                c.close()
            elif not data:
                print("no data")
                break
            else:
                if len(data) > 3:
                    c = con.cursor()
                    m = data.index('message:')
                    nam = " ".join(data[data.index('receiver:') + 1:m])
                    c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
                    f = c.fetchall()
                    c.close()
                    threading.Thread(target=save_dialog, args=(con, data, conn, nam, m, f, connection, addr)).start()
    except socket.error:
        c = con.cursor()
        print("socket_error")
        c.execute("""DELETE FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
        con.commit()
        connection.pop((str(addr[0]) + '_' + str(addr[1])))
        print("connection: ", str(addr[0]) + ' : ' + str(addr[1]), " losted")

        c.close()


if __name__ == '__main__':
    Main()
