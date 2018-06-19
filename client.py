import sys
import socket
from stuff import *
BUF_SIZE = 4096

if __name__ == "__main__":

  if len(sys.argv) != 3:
    sys.stderr.write("usage: tcp_client ip port\n")
    exit(1)

  try:
    addr = sys.argv[1]
    port = int(sys.argv[2])
    assert port > 0 
  except:
    sys.stderr.write("error: invalid port\n")
    exit(1)

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((addr, port))
    Tabela()
    print('')
    print("Chcesz wygrać milion zlotych ? TAK/NIE")
    while True:
      data = input('Ty :')

      if data == '':
        break
      if data=="START":
        ZasadyGry()
      sock.send(data.encode())
      data = sock.recv(BUF_SIZE)
      msg = data.decode("utf8")
      if len(msg)>0:
        if msg[0]=="@":
          print(msg[1:])
          break
      #print("Msg: ",msg) zlapanie pytania  
      if len(msg)>0:
        if msg[0]=="$":
          print(msg[1:])
          Tabela()
          break
      if len(msg)>0:
        if msg[0]=="#":
          foo = Pytanie(msg)
          # print(foo)
          WyswietlPytanie(foo)
      if not data:
        break
      if msg[0]!="#":
        print('Prowadzacy: ', data.decode("utf8"))
    sock.close()

  except socket.error:
    print('Error:', socket.error)