import socket
from _thread import *
import threading
import time

class Server:
    def __init__(self,name="server"):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.server = socket.gethostname()
        self.server = '192.168.18.12'
        self.name=name
        self.port = 5555
        print("i have become server")
        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            print(e)
        self.s.listen(5)
        print("connecting and searching for connections")
        self.conlist = []

    def recieve(self, co):
        while True:
            try:
                data = co.recv(2048)
                print(data.decode('utf-8'))
                for c in self.conlist:
                    c.sendall(data)
            except:
                break
    def send(self):
        while True:
            try:
                data = str.encode(self.name+" : "+input(),"utf-8")
                print(data.decode('utf-8'))
                for c in self.conlist:
                    c.sendall(data)
            except:
                pass

    def thread_function(self, conn):
        thread = threading.Thread(target=self.recieve, args=(conn,))
        thread.daemon = True
        thread.start()

        '''conn.sendall(str.encode("connected"))
        reply=""
        while True:
            try:
                data=conn.recv(2048)
                msg.append(data)
                reply=data.decode('utf-8')
                if not data:
                    print("disconnected")
                    break
                else:
                    print(reply)
                    conn.sendall(str.encode(reply))

            except:
                break
    '''

    def run(self, lis):
        while True:
            conn, addr = self.s.accept()
            conn.send(str.encode(str(len(lis)),"utf-8"))
            self.conlist.append(conn)
            lis.append(addr)
            tthred = threading.Thread(target=self.send)
            tthred.start()
            cthred = threading.Thread(target=self.thread_function, args=(conn,), daemon=True)
            cthred.start()
            print("peers",lis)