''' llegir un número n, seguit d'una seqüència de n números reals.
Si n no és major que 0, el programa acaba '''

from yogi import read   # Importar read de yogi

n = read(int)   # Llegir un número enter que el guardara a 'n'
                # 'n' serveix per a saber la quantitat de vegades que repetirem el bucle)"

for i in range(n):      # Si n és mes gran que 0 fer n vegades:
    dada = read(float)      # Llegir un número real i guardar-lo a la variable 'dada
    

