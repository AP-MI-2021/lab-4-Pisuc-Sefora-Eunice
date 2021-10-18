def meniu():
    print("1.Citire lista")
    print("2.Afisare lista dupa eliminarea numerelor prime din lista")
    print("3.Sa se afiseze daca media aritmetica a numerelor este mai mare ca un numar n dat")
    print("4.")
    print("5.")

def citire():
    n=int(input("Dati nr de elemente ale listei"))
    lst=[]
    for i in range(n):
        val=int(input("Indrodu element"))
        lst.append(val)
    return lst


def run():
    while True == True:
       meniu()
       opt=int(input("Introdu optiunea"))
       if opt == "1" :
           pass
       if opt == "2" :
           pass
       if opt == "3" :
           pass
       if opt == "4" :
           pass
       if opt == "5" :
           pass


