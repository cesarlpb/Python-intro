# Métodos de sets
#%% add()
my_set = {1, 2, 3, 4, 5}
print("set actual:", my_set)
for i in range(5):
    my_set.add(i**2)
print("set actual:", my_set)
#%% clear()
print("set actual:", my_set)
my_set.clear()
print("set actual:", my_set)
#%% copy()
my_set = {1, 2, 3, 4, 5}
print("set actual:", my_set)
new_set = my_set.copy()
print("nuevo set:", new_set)
print("Son iguales?", my_set == new_set)
print("Son el mismo set?", my_set is new_set)
#%% difference()
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 2, 4}
set3 = set1.difference(set2)
set4 = set2.difference(set1)
print("set3:", set3)
print("set4:", set4)
#%% difference_update() - edita el primer set
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 2, 4}
set1.difference_update(set2)
print("set1:", set1)

#%% discard()
set1 = {1, 2, 3, 4, 5}
print("set1 actual:", set1)
set1.discard(3)
set1.discard(4)
set1.discard(4)
set1.discard(5)
print("set1 editado:", set1)
#%% intersection() - retorna un nuevo set
set1 = {1, 2, 3}
set2 = {3, 2, 4}
set3 = set1.intersection(set2)
print("set3", set3)
#%% intersection_update() - actualiza el primer set
set1 = {1, 2, 3}
set2 = {3, 2, 4}
set1.intersection_update(set2)
print("set1 actual:", set1)
# isdisjoint()
set1 = {1, 2, 3}
set2 = {3, 2, 4}
print("No tienen intersección?:", set1.isdisjoint(set2))
print("Tienen intersección?:", not set1.isdisjoint(set2))
#%% issubset()
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

print("set1 es subset de set2?", set1.issubset(set2))
print("set2 es subset de set1?", set2.issubset(set1))
#%% issuperset()
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

print("set1 es subset de set2?", set1.issuperset(set2))
print("set2 es subset de set1?", set2.issuperset(set1))
#%% pop()
set1 = {1, 2, 3, 4, 5}
print(set1)
for i in range(len(set1)):
    print(i, "elemento eliminado:", set1.pop())
print(set1)
#%% remove()
set1 = {1, 2, 3, 4, 5}
print("set1 actual:", set1)
set1.remove(3)
set1.remove(4)
# set1.remove(4) # Arroja error porque no se puede eliminar el elemento dos veces
set1.remove(5)
print("set1 editado:", set1)
#%% symmetric_difference()
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
set3 = set1.symmetric_difference(set2)
print("diferencias set 1 con set 2:", set3)
# symmetric_difference_update() - edita el primer set
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print("diferencias set 1 con set 2:", set1)
# union()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print("unión de sets:", set3)
#%% update() - modifica el primer set
my_set = {1, 2, 3}
lista = [3, 4, 5]
tupla = (4, 5, 6, 7, 8, 9, 10)

my_set.update(lista, tupla)
print("set final:", my_set)