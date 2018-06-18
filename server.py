#!/usr/bin/env python
from socket import *
from threading import Thread
import sys,os
from stuff import *
import logging,signal,time


##Logger##
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
#####

MSG_SIZE=50

def pad_msg(msg):
  return msg + ' ' * (MSG_SIZE - len(msg))

def clientHandler():
    lista_p=[]
    flag_GAMESTART=False
    flag_GAME_GO = False
    flag_1 = False
    flag_1_ok=False
    flag_2 = False
    flag_2_ok=False
    flag_3 = False
    flag_3_ok=False
    flag_4 = False
    flag_4_ok=False
    nick=''
    hajs=0

    while True:
        conn, addr = s.accept()
        print(addr, "is connected")
        logger.info('Połaczenie nowe')
        cmd = conn.recv(MSG_SIZE).strip()
        if cmd.decode("utf8") == "NIE":
            logger.error('Typ nie chce wygrac miliona')
            conn.close()
            s.close()
            os._exit(1)
        
        conn.send(pad_msg("Proste kazdy chce wygrac, wiec wpisz START").encode())

        while True:
            try:
                data = conn.recv(1024)
            except ConnectionError as r:
                print("Polaczenie zerwane: ",r.strerror)
                os._exit(1)
            if not data:
                sys.exit()
            if data.decode("utf8") == "":
                sys.exit()
            if data.decode("utf8") == "EXIT":
                conn.close()
                s.close()
                os._exit(1)
                
            print(f"{addr} : ", repr(data))
            #---------------------------------------------------

            if flag_4:
                flag_4=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),3)
                if poprawna1:
                    hajs=10000
                    flag_4_ok=True
                    conn.send(b'Good! Masz 10000zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej.")
            
            elif flag_3_ok and data.decode("utf8")=="TAK":
                test_str4='#4'
                lista_p = OsiemPytan()
                test_str4+=lista_p[3][1]
                test_str4+=":"
                test_str4+=lista_p[3][2]
                test_str4+=":"
                test_str4+=lista_p[3][3]
                test_str4+=":"
                test_str4+=lista_p[3][4]
                test_str4+=":"
                test_str4+=lista_p[3][5]
                conn.send(test_str4.encode())
                print(test_str4)
                flag_3_ok=False
                flag_4 = True
            #--
            elif flag_3:
                flag_3=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),2)
                if poprawna1:
                    hajs=10000
                    flag_3_ok=True
                    conn.send(b'Good! Masz 1000zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej.")
            
            elif flag_2_ok and data.decode("utf8")=="TAK":
                test_str3='#3'
                lista_p = OsiemPytan()
                test_str3+=lista_p[2][1]
                test_str3+=":"
                test_str3+=lista_p[2][2]
                test_str3+=":"
                test_str3+=lista_p[2][3]
                test_str3+=":"
                test_str3+=lista_p[2][4]
                test_str3+=":"
                test_str3+=lista_p[2][5]
                conn.send(test_str3.encode())
                print(test_str3)
                flag_3 = True

            elif flag_2:
                flag_2=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),1)
                if poprawna1:
                    hajs=500
                    flag_2_ok=True
                    conn.send(b'Good! Masz 500zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej.")
            

            elif flag_1_ok and data.decode("utf8")=="TAK":
                test_str2='#2'
                lista_p = OsiemPytan()
                test_str2+=lista_p[1][1]
                test_str2+=":"
                test_str2+=lista_p[1][2]
                test_str2+=":"
                test_str2+=lista_p[1][3]
                test_str2+=":"
                test_str2+=lista_p[1][4]
                test_str2+=":"
                test_str2+=lista_p[1][5]
                conn.send(test_str2.encode())
                print(test_str2)
                flag_2 = True
                
            elif flag_1:
                flag_1=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),0)
                if poprawna1:
                    hajs=100
                    flag_1_ok=True
                    conn.send(b'Good! Masz 100zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej.")
            
            elif(flag_GAME_GO and data.decode("utf8") == "TAK"):
                test_str='#1'
                lista_p = OsiemPytan()
                test_str+=lista_p[0][1]
                test_str+=":"
                test_str+=lista_p[0][2]
                test_str+=":"
                test_str+=lista_p[0][3]
                test_str+=":"
                test_str+=lista_p[0][4]
                test_str+=":"
                test_str+=lista_p[0][5]
                conn.send(test_str.encode())
                print(test_str)
                flag_1 = True

            elif data.decode("utf8")=="ODCHODZE":
                 if nick!='' and hajs>0:
                    DodajDoTabeli(nick,hajs)
                    end_str= f"Dzieki za grę {nick} wygrales {hajs} zl! Powodzenia"
                    conn.send(end_str.encode())
                    conn.close()
                    os._exit(-1)
        

            elif flag_GAMESTART:
                st = data.decode("utf8")+" jestes gotowy na pierwsze pytanie? (TAK/NIE) "
                nick=data.decode("utf8")
                conn.send(st.encode())
                flag_GAMESTART=False
                flag_GAME_GO=True

            elif data.decode("utf8") == "START":
                flag_GAMESTART=True
                conn.send(b"OK, Podaj swoj nick")
                
            else: 
                conn.send(b"Graj wedlug protokolu!")

HOST = "127.0.0.1"
PORT = 12313

s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)

print("Server Up")
for i in range(10):
    t =  Thread(target=clientHandler)
    # t.daemon=True
    t.start()

s.close()
