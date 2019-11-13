a = "abcdefaaddbe"
print(len(a))
from random import shuffle
lista = list(a)
shuffle(lista)
print("".join(list(lista)))