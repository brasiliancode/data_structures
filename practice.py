import random 

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1 
        lista[j + 1] = chave



def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista,meio, fim)
        merge(lista, inicio, meio,fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0 
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1 
        elif top_right >= len(right):
            lista[k] = left[top_left]
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1 

any_number = random.sample(range(1, 1000), 40)

if __name__=='__main__':
    test_case = {'Numeros aliatorios': any_number}
    for name, lista in test_case.items():
        print(f'\n{name}:\n {lista}:')
        print()
        print('Numeros aliatorios:\n')
        insertion_sort(lista)
        print(lista)

        

         