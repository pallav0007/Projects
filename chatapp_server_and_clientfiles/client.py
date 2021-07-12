import socket
from _thread import *
import threading
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server=socket.gethostname()
server = '192.#####'
port=5555
addr=(server,port)
name=input("enter your name:")
print_lock = threading.Lock()
try:
    client.connect(addr)
except:
    print("unable to establish connection")
def thread_msg():
    while True:
        inp=input()
        if inp=="quit":
            break
        else:
            client.sendall(str.encode(name+" : "+inp,"utf-8"))

thread = threading.Thread(target=thread_msg)
thread.daemon = True
thread.start()

while thread.is_alive():
    #client.sendall(str.encode(name+"connected"))
    try:
        data=client.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            print("disconnected")
            break
        else:
            try:
                re=reply.split(' : ')
                r=re[0]
                ply=re[1]
                if r!=name:
                    print(str(r).rjust(40," ")+"\n"+str(ply).rjust(40," "))
                else:
                    print(r,ply,sep="\n")
            except:
                print(reply)
    except:
        print("error")
        break
