import socket
from _thread import *
import threading
server = '192.#######'
#server=socket.gethostname()
port=5555
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    print(e)
s.listen(5)
print("connecting and searching for connections")
conlist=[]

def recieve(co):
    while True:
        try:
            data=co.recv(2048)
            for c in conlist:
                c.sendall(data)
        except:
            break
def thread_function(conn):
    thread = threading.Thread(target=recieve, args=(conn,))
    thread.daemon = True
    thread.start()

while True:
    conn,addr=s.accept()
    conlist.append(conn)
    cthred=threading.Thread(target=thread_function,args=(conn,),daemon=True)
    cthred.start()
    print(conlist)
    print("connected to:",addr)