import socket
from _thread import *
import threading
import time
class Client:
    number=1
    def __init__(self,addr,name="client"):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.server=socket.gethostname()
        self.server = '192.168.18.12'
        self.port=5555

        self.addr=addr
        self.name=name

        try:
            self.client.connect(self.addr)
            print("established connection")
            Client.number=int(self.client.recv(2048).decode('utf-8'))
            print(Client.number)
        except:
            print("unable to establish connection")
    def thread_msg(self):
        while True:
            inp=input()
            if inp=="quit":
                break
            else:
                try:
                    self.client.sendall(str.encode(self.name+" : "+inp,"utf-8"))
                except:
                    print("msg not sent")
    def threaduse(self):
        thread = threading.Thread(target=self.thread_msg)
        thread.daemon = True
        thread.start()

        while thread.is_alive():
            #client.sendall(str.encode(name+"connected"))
            try:
                data=self.client.recv(2048)
                reply = data.decode('utf-8')
                if not data:
                    print("disconnected")
                    break
                else:
                    print(reply)
                    # try:
                    #     re=reply.split(' : ')
                    #     r=re[0]
                    #     ply=re[1]
                    #     if r!=self.name:
                    #         print(str(r).rjust(40," ")+"\n"+str(ply).rjust(40," "))
                    #     else:
                    #         print(r,ply,sep="\n")
                    # except:
                    #     print(reply)
            except:
                print("error")
                break
