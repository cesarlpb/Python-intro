# Repaso de las formas de iterar una lista
# Fuentes:
    # - https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
    # - https://python-programs.com/python-different-ways-to-iterate-over-a-list-in-reverse-order/

#%% for / in en lista
from hashlib import new


list = [1, 3, 5, 7, 9]   

for el in list:
    print(el, end=" ")
#%% for / in con len(lista)

list = [1, 3, 5, 7, 9]
   
for i in range(len(list)):
    print(list[i], end=" ")
#%% while

list = [1, 3, 5, 7, 9]

idx = 0

while idx < len(list):
    print(list[idx], end=" ")
    idx += 1

#%% List comprehension o comprensión de lista

list = [1, 3, 5, 7, 9]

print([el for el in list]) 
# Nota: el primer el se puede sustituir 
# por una operación en cada uno de los 
# elementos de la nueva lista

# %% Usando enumerate

list = [1, 3, 5, 7, 9]
# enumerate -> devuelve índice y valor de colección
for idx, valor in enumerate(list):
	print (f"({idx}, {valor})", end="\n")

#%% Iteración en reversa
list = [1, 3, 5, 7, 9]

for i in reversed(list):
    print(i, end=" ")

