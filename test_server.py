 
import socket, threading

class ClientThread(threading.Thread):
    
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        flag_GAMESTART=False
        nick=''
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye' or msg=='':
              break
            print ("from client", msg)
            # self.csocket.send(bytes(msg,'UTF-8'))
            if self.flag_GAMESTART:
                self.flag_GAMESTART=False
                st = "Lets Begin "+msg
                self.nick = msg
                self.csocket.send(bytes(st))

            if(msg=="START"):
                self.flag_GAMESTART=True
                self.csocket.send(bytes("Witaj w grze wybierz swoj nick",'UTF-8'))
            else:
                self.csocket.send(bytes("Type START",'UTF-8'))
                continue
        print ("Client at ", clientAddress , " disconnected...")
        

LOCALHOST = "127.0.0.1"
PORT = 12313
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
