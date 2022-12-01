#%% Eliminar elementos de un set
# remove() - arroja error si el elemento no se encuentra en el set
# discard() - NO arroja error
# pop() - quita el último elemento y retorna el valor eliminado del set

this_set = {1, 2, 3}
this_set.remove(3)
# this_set.remove(3) # arroja error porque no se puede eliminar el elemento dos veces
print("set actual:", this_set)

this_set.discard(3) # no tira error
this_set.discard(2)
print("set actual:", this_set)

# pop
this_set = {1, 2, 3, 4, 5}
valor1 = this_set.pop()
valor2 = this_set.pop()
valor3 = this_set.pop()
print("Elemento eliminado:", valor1)
print("Elemento eliminado:", valor2)
print("Elemento eliminado:", valor3)
print(this_set)

# clear
this_set.clear()
print("set borrado:", this_set, type(this_set))

# del
del this_set
print(this_set) # arroja error porque está no definida