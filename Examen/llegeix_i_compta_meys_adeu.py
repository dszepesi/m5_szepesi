'''Llegeix sequencia de paraules i compta quantes hi ha. 
Mentre la paraula sigui diferent de "adeu", no compta "adeu" i guarda la paraula a la variable paraula'''
from yogi import read   # Importar read de yogi

paraula = read(str)     # Llegir i guardar paraules a la variable paraula
cont = 0    # Inicio la variable contador 

while paraula != "adeu":    # Mentre paraula no es igual a 'adeu'
    cont = cont + 1         # Al contador de paraules li afegeixo un volta
    paraula = read(str)     # Llegir paraula

print(cont, paraula)  # Quan paraula acaba, retorno el ultima paraula que s'ha escrit i el numero de paraules correctes
