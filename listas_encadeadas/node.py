"""No e alocacao encadeada - Listas Encadeadas simples | estrutura de dados  """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



no1 = Node(5)
no2 = Node(6)
no1.next = no2

