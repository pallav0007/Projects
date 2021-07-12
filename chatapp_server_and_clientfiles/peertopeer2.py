from chatapp_server_and_clientfiles.replyerver import Server
from chatapp_server_and_clientfiles.peer2_client import Client
import time
import random
import sys
import socket
"""
    This class will take care of converting client to server
"""

class p2p:
    server = '192.168.56.1'
    port = 5555
    addr = (server, port)
    # make ourself the default peer
    peers = [addr]
num=1
while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 seconds
            time.sleep(random.randint(1,4))
            for peer in p2p.peers:
                try:
                    n = 0
                    while n < num:
                        client = Client(peer)
                        client.threaduse()
                        num = Client.number
                        print("number client", num)
                        n += 1
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = Server()
                    server.run(p2p.peers)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)