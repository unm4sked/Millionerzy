
from socket import *
from threading import Thread
import sys,os
from stuff import *
import logging,signal,time


##Logger##
logging.basicConfig(filename='game.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-4s %(levelname)-4s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
# logger = logging.getLogger('myapp')
# hdlr = logging.FileHandler('myapp.log')
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr) 
# logger.setLevel(logging.WARNING)
#####

MSG_SIZE=50

def pad_msg(msg):
  return msg + ' ' * (MSG_SIZE - len(msg))

def clientHandler():
    lista_p=[]
    KoloRatunkowe5050_=True
    KoloRatunkoweGlosPublicznosci_=True
    KoloRatunkoweTelefon_=True
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
    flag_5 = False
    flag_5_ok=False
    flag_6 = False
    flag_6_ok=False
    flag_7 = False
    flag_7_ok=False
    flag_8 = False
    nick=''
    hajs=0

    while True:
        conn, addr = s.accept()
        print(addr, "is connected")
        cmd = conn.recv(MSG_SIZE).strip()
        # if cmd.decode("utf8") == "NIE":
        #     logging.error(f'Wpisana komenda "NIE", nie chce wygrac miliona {addr}')
        #     conn.send(b"@Jak nie to nie")
        #     conn.close()
        #     os._exit(1)
        
        conn.send(pad_msg("Proste ze kazdy chce wygrac, wiec wpisz START").encode())
        logging.info(f'Rozpoczyna sie gra {addr}')

        while True:
            try:
                data = conn.recv(1024)
                mess = data.decode("utf8")
            except ConnectionError as r:
                print("Polaczenie zerwane: ",r.strerror)
                logging.info(f'Polaczenie zerwane:  {addr}')
                os._exit(1)
            if not data:
                sys.exit()
            if data.decode("utf8") == "":
                logging.info(f'Wyslana pusta linia {addr}')
                conn.send(b'@Bye!')
                sys.exit()
            if data.decode("utf8") == "EXIT":
                conn.send(b'@Bye!')
                logging.info(f'Uzytkownik wychodzi z gry "EXIT" {addr}')
                conn.close()
                s.close()
                os._exit(1)
                
            print(f"{addr} : ", repr(data))
            #---------------------------------------------------
            if flag_8 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[7]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
            elif flag_8:
                flag_8=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),7)
                if poprawna1:
                    hajs=1000000
                    DodajDoTabeli(nick,hajs)
                    conn.send(b'$Jestes Millionerem! BRAWO!  1 000 000 zl')
                    logging.info(f'Uzytkownikowi {nick} wygral 1 000 000 zl  {addr}')
                    conn.close()

                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej. ")
            
            elif flag_7_ok and data.decode("utf8")=="TAK":
                test_str8='#7'
                lista_p = OsiemPytan()
                test_str8+=lista_p[7][1]
                test_str8+=":"
                test_str8+=lista_p[7][2]
                test_str8+=":"
                test_str8+=lista_p[7][3]
                test_str8+=":"
                test_str8+=lista_p[7][4]
                test_str8+=":"
                test_str8+=lista_p[7][5]
                conn.send(test_str8.encode())
                print(test_str8)
                flag_7_ok=False
                flag_8 = True
                logging.info(f'Uzytkownikowi {nick} zadano 8 pytanie  {addr}')

            
            elif flag_7 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[6]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())

            elif flag_7:
                flag_7=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),6)
                if poprawna1:
                    hajs=500000
                    flag_7_ok=True
                    conn.send(b'Good! Masz 500000zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej. ")
            
            elif flag_6_ok and data.decode("utf8")=="TAK":
                test_str7='#6'
                lista_p = OsiemPytan()
                test_str7+=lista_p[6][1]
                test_str7+=":"
                test_str7+=lista_p[6][2]
                test_str7+=":"
                test_str7+=lista_p[6][3]
                test_str7+=":"
                test_str7+=lista_p[6][4]
                test_str7+=":"
                test_str7+=lista_p[6][5]
                conn.send(test_str7.encode())
                print(test_str7)
                flag_6_ok=False
                flag_7 = True
                logging.info(f'Uzytkownikowi {nick} zadano 7 pytanie  {addr}')

            
            elif flag_6 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[5]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())

            elif flag_6:
                flag_6=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),5)
                if poprawna1:
                    hajs=100000
                    flag_6_ok=True
                    conn.send(b'Good! Masz 100000zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej. ")
            
            elif flag_5_ok and data.decode("utf8")=="TAK":
                test_str6='#5'
                lista_p = OsiemPytan()
                test_str6+=lista_p[5][1]
                test_str6+=":"
                test_str6+=lista_p[5][2]
                test_str6+=":"
                test_str6+=lista_p[5][3]
                test_str6+=":"
                test_str6+=lista_p[5][4]
                test_str6+=":"
                test_str6+=lista_p[5][5]
                conn.send(test_str6.encode())
                print(test_str6)
                flag_5_ok=False
                flag_6 = True
                logging.info(f'Uzytkownikowi {nick} zadano 6 pytanie  {addr}')

            elif flag_5 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[4]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
            
            elif flag_5:
                flag_5=False
                poprawna1 = SprawdzOdp(lista_p,data.decode("utf8"),4)
                if poprawna1:
                    hajs=50000
                    flag_5_ok=True
                    conn.send(b'Good! Masz 50000zl! Jesli chcesz odejsc z pieniedzmi "ODCHODZE" jesli grasz dalej "TAK"')
                else:
                    conn.send(b"@Bad! No niestety przegrywasz wszystko! sprobuj szczescie pozniej. ")
            
            elif flag_4_ok and data.decode("utf8")=="TAK":
                test_str5='#4'
                lista_p = OsiemPytan()
                test_str5+=lista_p[4][1]
                test_str5+=":"
                test_str5+=lista_p[4][2]
                test_str5+=":"
                test_str5+=lista_p[4][3]
                test_str5+=":"
                test_str5+=lista_p[4][4]
                test_str5+=":"
                test_str5+=lista_p[4][5]
                conn.send(test_str5.encode())
                print(test_str5)
                flag_4_ok=False
                flag_5 = True
                logging.info(f'Uzytkownikowi {nick} zadano 5 pytanie  {addr}')


            elif flag_4 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[3]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
            elif flag_4:
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
                logging.info(f'Uzytkownikowi {nick} zadano 4 pytanie  {addr}')


            elif flag_3 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[2]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
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
                flag_2_ok= False
                flag_3 = True
                logging.info(f'Uzytkownikowi {nick} zadano 3 pytanie  {addr}')


            elif flag_2 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[1]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
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
                flag_1_ok=False
                flag_2 = True
                logging.info(f'Uzytkownikowi {nick} zadano 2 pytanie  {addr}')

            elif flag_1 and mess[0]=="#":
                msg_kolo = data.decode("utf8")
                if msg_kolo[0]=="#":
                    lista_p1 = OsiemPytan()[0]
                    if msg_kolo=="#1" and KoloRatunkowe5050_:
                        x = KoloRatunkowe5050(lista_p1)
                        foo = f"50:50 -> {x[0]} , {x[1]}"
                        conn.send(foo.encode())
                        KoloRatunkowe5050_=False
                    elif msg_kolo=="#2" and KoloRatunkoweGlosPublicznosci_:
                        x = KoloRatunkoweGlosPublicznosci(lista_p1)
                        x= x[0]
                        foo = f"Publicznosc stawia na -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweGlosPublicznosci_=False
                    elif msg_kolo=="#3" and KoloRatunkoweTelefon_:
                        x = KoloRatunkoweTelefon(lista_p1)
                        x= x[0]
                        foo = f"Kompel stawia na  -> {x}"
                        conn.send(foo.encode())
                        KoloRatunkoweTelefon_=False
                    else:
                        foo = "No nie mozesz tutaj wziac kola niestety"
                        conn.send(foo.encode())
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
                flag_GAME_GO=False
                flag_1 = True
                logging.info(f'Uzytkownikowi {nick} zadano 1 pytanie  {addr}')

            elif data.decode("utf8")=="ODCHODZE":
                if hajs>0:
                    logging.info(f'Uzytkownik {nick} odchodzi z gry "ODCHODZE", wygral {hajs}  {addr} ')
                    DodajDoTabeli(nick,hajs)
                    end_str= f"@Dzieki za grę {nick} wygrales {hajs} zl! Powodzenia"
                    conn.send(end_str.encode())
                    
                else:
                    logging.info(f'Uzytkownik {nick} odchodzi z gry "ODCHODZE", wygral {hajs}  {addr} ')
                    # DodajDoTabeli(nick,hajs)
                    end_str= f"@Dzieki za grę {nick} wygrales {hajs} zl! Powodzenia"
                    conn.send(end_str.encode())
                    conn.close()
                    os._exit(-1)
        

            elif flag_GAMESTART:
                st = data.decode("utf8")+" jestes gotowy na pierwsze pytanie? (TAK/NIE) "
                nick=data.decode("utf8")
                conn.send(st.encode())
                flag_GAMESTART=False
                flag_GAME_GO=True
                logging.info(f'Uzytkownik ma nick {nick} {addr}')

            elif data.decode("utf8") == "START":
                logging.info(f'Uzytkownik chce grac "START" {addr}')
                flag_GAMESTART=True
                conn.send(b"OK, Podaj swoj nick")
                
                
            else: 
                conn.send(b"Graj wedlug protokolu!")
                zxccv= data.decode("utf8")
                logging.info(f'Uzytkownik wpisuje cos niezgodnego z protokolem "{zxccv}" {addr}')

HOST = "127.0.0.1"
PORT = 12312

s = socket(AF_INET,SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)

print("Server Up")
for i in range(10):
    t =  Thread(target=clientHandler)
    # t.daemon=True
    t.start()

s.close()
