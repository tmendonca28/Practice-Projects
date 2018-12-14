schuhschrank = []
a = []


def eingabe(schuhschrank, a):
    farbe = input("Farbe: ")
    if(farbe == ''):
        print(schuhschrank)
    else:
        a = []
        a.append(farbe)
        typ = input("Typ: ")
        a.append(typ)
        groesse = int(input("Groesse: "))
        a.append(groesse)
        preis = float(input("Preis: "))
        a.append(preis)
        schuhschrank.append(a)
        eingabe(schuhschrank, a)
eingabe(schuhschrank, a)