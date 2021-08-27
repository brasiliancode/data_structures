from time import sleep



def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

if __name__=='__main__':
    lista = ['python','django','javascript','1.4', '5.5']

    elemento = input('Buscar elemento:').strip()

    indice = busca(lista, elemento)
    if indice is not None:
        print(f'o indice do elemento {elemento} is {indice}.')
    else:
        print(f'O elemento {elemento} nao se encontra na lista.')




