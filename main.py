import ciklusok

a: int = int(input("a: "))
b: int = int(input("b: "))

"""A felhasználó csak olyan b-t tudjon megadni, ami >a"""
while (a>=b):
    print("B-nek nagyobbnak kell lennie A-nal.")
    b: int = int(input(f"Adj {a}-nál nagyobbat!"))

ciklusok.szamok(a,b)