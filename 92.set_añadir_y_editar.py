#%% add() y update()

this_set = {1, 2, 3}
lista = [4, 5, 6]

this_set.add(-1)
this_set.add(10)

# Podemos añadir cualquier colección al set con update()
this_set.update(lista)
print("set actual:", this_set)

for el in this_set:
    print(el, end=" ")