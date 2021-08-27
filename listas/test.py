"""
Test automatizado

"""

import random 
from search import binary_search

empty = []
single = [7]
pair = [3, 7]
odd = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43]
even = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43, 70]
repeated = [1, 2, 2, 5, 5, 9, 13, 21, 21, 21]

def test_empty():
    if binary_search(empty, random.randint(0, 1000)) is not None:
        return False
    return True

def test_single():
    if binary_search(single, 7):
        return False
    if binary_search(single, 10) is not None:
        return False
    return True

if __name__=='__main__':
    print('********************************************')
    if test_empty():
        print('PASSOU VAZIO')
    else:
        print('FALHOU VAZIO')
    if (test_single()):
        print('PASSOU UNICO')
    else:
        print('FALHOU UNICO')

    test_cases = {
        'Dupla':pair,
        'Impar': odd, 
        'Par':even,
        'Repetido': repeated
    }

    again ='s'
    while(again == 's'):
        for name, lista in test_cases.items():
            print(f'\n Caso de teste: {name}\n {lista}')
            # seleciona a lista 

            e = int(input('elemento a ser buscado:').strip())
            i = binary_search(lista, e)
            print('\n Indice encontrado:', i)
        again = input('Repetir? (S/N):').lower()
    
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++=')
