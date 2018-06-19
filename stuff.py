import sqlite3
import random
import copy

    
def Tabela():
    wyniki= []
    conn_db = sqlite3.connect('baza.db')
    c = conn_db.cursor()
    for row  in c.execute('''SELECT * FROM Wyniki '''):
        wyniki.append(row)

    wyniki.sort(key= lambda tup: tup[1], reverse=True)
    nr = 0
    print('***ALL PLAYERS***')
    print('''Miejsce     Nick           Wygrana''')
    for r in wyniki:
        nr = nr+1
        result = f'''{nr}.          {r[0]}      {r[1]}'''
        
        print(result)
    
def ZasadyGry():
    zasady = '''Zanim czaniesz zapoznaj sie z zasadami gry:
*****************************************
0.Jest 8 pytan:
    1 -> 100zl
    2 -> 500zl
    3 -> 1000zl
    4 -> 10000zl
    5 -> 50000zl
    6 -> 100000zl
    7 -> 500000zl
    8 -> 1000000zl #Milioner
1.Postepuj wg. protokolu inaczej nie wygrasz nic  #smutek
2.Mozesz w kazdym pytaniu uzyc kola ratunkowego
    -50:50    -> nacisnij "#1"
    -Telefon do przyjaciela -> nacisnij "#2"
    -Glos publicznosci -> nacisnij "#3"

3.Zaczynasz Gre Od Momentu Gdy Potwierdzisz gotowosc do Gry poprzez "START"
4.Wybierz sobie jakis nick, jesli wygrasz cos to bedziesz w Tabeli pod takim nickiem
5.Po przeczytaniu kazdego pytania bedziesz mial 4 odpowiedzi, odpowiadasz poprzez wpisanie tej odpowiedzi, wielkosc liter ma znaczenie
6.Jesli cos juz wygrasz bedziesz mogl odejsc z hajsem poprzez "ODCHODZE" , bedziesz zapisany w tabeli wtedy ale odejsc mozesz po odpowiedzi na pytanie.
7.Jesli bedziesz chcial odejsc od gry po przeczytaniu nowego pytania wtedy traktowane to jest jako zla odpowiedz
*****************************************
    '''
    print(zasady)

def OsiemPytan():
    lista_pytan= []
    conn_db = sqlite3.connect('baza.db')
    c = conn_db.cursor()
    for row  in c.execute('''SELECT * FROM GRA '''):
        lista_pytan.append(row)
    conn_db.close()

    return lista_pytan


# 6index poprana 
# 1index pytanie
# 2,3,4,5 odpowiedzi

def KoloRatunkowe5050(pytanie):
    x = random.randrange(2,5)
    y=pytanie[6]
    if y==pytanie[x]:
        x=random.randrange(2,5)
    if x%2==0:
        return list((y,pytanie[x]))
    return list((pytanie[x],y))

def KoloRatunkoweGlosPublicznosci(pytanie):
    new_list = copy.copy(list(pytanie))
    new_list.pop(0)
    new_list.pop(0)

    x = random.choices(new_list)
    return x


def KoloRatunkoweTelefon(pytanie):
    new_list = copy.copy(list(pytanie))
    new_list.pop(0)
    new_list.pop(0)
    x = random.choices(new_list)
    return x    
def SklejNapis(nr,str1):
    nr = int(nr)
    test_str2=str1
    lsta_p= []
    lista_p = OsiemPytan()
    test_str2+=lista_p[nr][1]
    test_str2+=":"
    test_str2+=lista_p[nr][2]
    test_str2+=":"
    test_str2+=lista_p[nr][3]
    test_str2+=":"
    test_str2+=lista_p[nr][4]
    test_str2+=":"
    test_str2+=lista_p[nr][5]
    
    return test_str2


def DodajDoTabeli(name,hajs):
    if hajs < 0:
        hajs=0
    conn_db = sqlite3.connect('baza.db')
    c = conn_db.cursor()
    c.execute(f"INSERT INTO Wyniki  VALUES ('{name}','{hajs}')")
    conn_db.commit()
    conn_db.close()

def Pytanie(pytanie):
    pytanie_ = pytanie[2:]
    foo = pytanie_.split(":")
    return foo
def WyswietlPytanie(pytanie):
    print(f'''***A więc dobrze, Pytanie  brzmi: ",{pytanie[0]}***
    --->  {pytanie[1]}
    --->  {pytanie[2]}
    --->  {pytanie[3]}
    --->  {pytanie[4]}

    
    ***Jaka jest Twoja odpowiedz?***
    ''')


def SprawdzOdp(pytanie,odpowiedz,nr):
    nr = int(nr)
    # print(pytanie[nr])
    # print(">>>",odpowiedz)
    # print(">>>",pytanie[nr][5])
    
    if odpowiedz==pytanie[nr][6]:
        return True
    else:
        return False


def HajsWygrany(tablica):
    pass

# p = ('1','2+2','dwa','trzy','cztery','jeden','cztery')
# print(KoloRatunkowe5050(p))
# print(KoloRatunkoweGlosPublicznosci(p))
# Tabela()
    