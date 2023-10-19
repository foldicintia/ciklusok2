import math 

def szamok(a:float, b:float):
    if a==b:
        print("A két szám egyenglő!")
        return
    
    if a>b:
        csere:float = a
        a = b
        b = csere

def szamok(a:float, b:float):
    i = math.ceil(a)
    while i<b:
        if i == b - 1:
            print(i)
        else:
            print(i, end=",")
        i+=1