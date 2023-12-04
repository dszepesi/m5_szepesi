'''Llegeix sequencia de paraules i compta quantes hi ha. 
Mentre la paraula que s'introdueixi no estigui buida, i guarda la paraula correcta a la variable paraula '''
from yogi import scan   # Importar scan de yogi

paraula = scan(str)     # Llegir i guardar paraules a la variable paraula
cont = 0    # Inicio la variable contador 

while paraula is not None:  # Mentre la variable paraula hi ha algo escrit, executa el bucle
    contc = cont + 1        # Al contador de paraules li afegeixo un volta
    paraula = scan(str)     # Llegir paraula

print(cont, paraula)  # Quan paraula acaba, retorno el ultima paraula que s'ha escrit i el numero de paraules correctes