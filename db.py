#https://docs.python.org/3/library/sqlite3.html

import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()

#c.execute(''' CREATE TABLE GRA (id integer primary key,Pytanie text, odp1 text, odp2 text, odp3 text, odp4 text, dobra text)''')
#c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('2*2','1','2','3','4','4')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('Ile mamy wojewodztw?','10','40','16','4','16')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('Stolica Polski?','Warszawa','Lublin','Krakow','Lublin','Warszawa')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('Ktory mamy rok?','2020','2000','2001','2018','2018')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('Kopa ile to?','60','12','30','42','60')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('500ml ile to l?','0.5','2','3','4','0.5')''')
# c.execute(''' INSERT INTO GRA (Pytanie, odp1,odp2,odp3,odp4,dobra)  VALUES ('10*10?','0','22','3','100','100')''')

# c.execute('''UPDATE GRA SET Pytanie = "2+0" WHERE id = 1;''')
# conn.commit()
for row  in c.execute('''SELECT * FROM GRA '''):
    print(row)


# Tabela z wynikami
# c.execute('''CREATE TABLE Wyniki (Nick text,Wynik INTEGER)''')
#c.execute(''' INSERT INTO Wyniki  VALUES ('Test111','10')''')
conn.commit()

conn.close()

def Wylosuj_pytanie():
    pass

def Zapisz_Wynik(x):
    pass

def Wyswietl10Naj():
    pass