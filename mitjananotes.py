qnotes = int(input())
contador = 0
suma = 0
mitjana = 0
while (contador<qnotes):
    contador = contador+1
    num = int(input())
    if (num<0) or (num>100):
        break
    else:
        suma = suma + num

if mitjana==0:
    print("Les notes no estan dins del rang burro!!")
else:
    mitjana = suma//qnotes
    print(mitjana)