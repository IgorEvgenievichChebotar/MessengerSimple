import socket
import threading
import sqlite3
import pickle


def accepting(sock, con, connection):
    try:

        while True:
            conn, addr = sock.accept()
            print('Connected to :', addr[0], ':', addr[1])
            thread_1 = threading.Thread(target=receive, args=(conn, sock, addr, con, connection))
            thread_1.start()

    except socket.error:

        print("NO")


def save_dialog(con, data, conn, nam, m, f, connection, addr):
    c = con.cursor()
    c.execute("""SELECT name FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
    name = c.fetchone()[0]
    message = ' '.join(data[m + 1:])
    c.execute("""SELECT * from sqlite_master where type = 'table'""")
    tables = c.fetchall()

    table = ''
    print(name, nam)
    for x in tables:
        print(x)
        print(x[1])
        print((x[1]).split("_"))
        if nam in (x[1]).split("_"):
            if name in (x[1]).split("_"):
                table = x[1]
                print(table)
                break
            else:
                table = ''
        else:
            table = ''
    print(table)
    if table == '':
        c.execute(
            """CREATE TABLE IF NOT EXISTS """ + "'" + name + '_' + nam + "'" + """(sender TEXT, receiver TEXT, message TEXT, status TEXT)""")
        table = str("'" + name + '_' + nam + "'")
        save_dialog(con, data, conn, nam, m, f, connection, addr)
    else:
        c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
        f = c.fetchall()
        print(f)
        c.execute("""SELECT * from sqlite_master where type = 'table'""")
        print(c.fetchall())
        print(table)
        if f:
            print(connection)
            message = data[m + 1:]
            msg = ' '.join(message)
            print((str(addr[0]) + '_' + str(addr[1])))
            c.execute("""INSERT INTO """ + '{0}'.format("'" + table + "'") + """ Values (?,?,?,?)""",
                      (str(name), str(nam), str(msg), "1"), )  # '"' + name + '_' + nam + '"'
            print(msg)
            c.execute("""SELECT * FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
            sender = c.fetchall()[0][0]
            print(sender)
            c.execute("SELECT link FROM login_data Where login = ? ", (sender,))
            image = c.fetchone()[0]
            image = open(image, "rb")
            messages = {"sender:": sender,
                        "message:": msg,
                        "image:": image.read()}

            ip_port = f[-1][1]
            receiver = connection[ip_port]
            print(receiver)
            print(connection)
            print(f[0][1])
            receiver.send(pickle.dumps(messages))
            print(sender + " message: " + msg)
            print("send")
            c.close()
        else:

            th = threading.Thread(target=checking_user,
                                  args=(nam, con, data, conn, name, message, m, connection, addr, table))
            th.start()


def checking_user(nam, con, data, conn, name, message, m, connection, addr, table):
    st = True
    while st:

        c = con.cursor()
        c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
        f = c.fetchall()

        if f:
            print(connection)
            message = data[m + 1:]
            msg = ' '.join(message)
            print((str(addr[0]) + '_' + str(addr[1])))

            c.execute("""INSERT INTO {0} Values (?,?,?,?)""".format('{0}'.format('"' + table + '"')),
                      (str(name), str(nam), str(msg), "1"), )

            print(f[0][1])

            print(msg)
            c.execute("""SELECT * FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
            sender = c.fetchall()[0][0]
            print(sender)
            c.execute("SELECT link FROM login_data Where login = ? ", (sender,))
            image = c.fetchone()[0]
            image = open(image, "rb")
            messages = {"sender:": sender,
                        "message:": msg,
                        "image:": image.read()}
            ip_port = f[0][1]
            print(connection)
            try:
                receiver = connection[ip_port]
                print(receiver)
                receiver.send(pickle.dumps(messages))
                print(sender + " message: " + msg)
                print("send")
                c.close()
                break
            except:
                checking_user(nam, con, data, conn, name, message, m, connection, addr, table)


def receive(conn, sock, addr, con, connection):
    try:

        while True:

            data = conn.recv(40960000).decode('utf-8').split()
            print(data)
            if 'name:' in data:
                c = con.cursor()
                name = " ".join(data[1:])
                c.execute("""INSERT INTO base_connection VALUES (?,?)""", (name, (str(addr[0]) + '_' + str(addr[1])),))
                con.commit()
                ip_port = ('{0}_{1}'.format(str(addr[0]), str(addr[1])))
                print(ip_port)
                connection[ip_port] = conn
                print(connection)
                c.close()

            elif not data:

                print("NO")
                break

            else:

                if len(data) > 3:
                    c = con.cursor()
                    print(data)
                    m = data.index('message:')
                    print(m)
                    nam = " ".join(data[data.index('receiver:') + 1:m])
                    print(nam)
                    c.execute("""SELECT * FROM base_connection WHERE name = ?""", (nam,))
                    f = c.fetchall()
                    print(f)
                    c.close()
                    print(connection)
                    threading.Thread(target=save_dialog, args=(con, data, conn, nam, m, f, connection, addr)).start()

    except socket.error:
        c = con.cursor()
        print("NO")
        c.execute("""DELETE FROM base_connection WHERE address = ?""", ((str(addr[0]) + '_' + str(addr[1])),))
        con.commit()
        connection.pop((str(addr[0]) + '_' + str(addr[1])))
        print(connection)
        c.close()


def Main():
    host = '127.0.0.1'
    port = 60005
    con = sqlite3.connect("login_data.db", check_same_thread=False)
    connection = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    s.listen(5)
    print("socket is listening")
    thread = threading.Thread(target=accepting, args=(s, con, connection))
    thread.start()


if __name__ == '__main__':
    Main()