# Formas de "editar" elementos de tuplas
    # No se puede cambiar los elementos de una tupla una vez creada
    # Vemos alternativas para poder crear listas o tuplas con los elementos que necesitemos en cada caso

#%% "Edición" en tupla - en realidad creamos una nueva tupla con los datos correctos mediante una lista
old_tuple = ("apple", "banana", "cherry")
my_list = list(old_tuple)
my_list[1] = "kiwi"
new_tuple = tuple(my_list)

print("tupla inicial:", old_tuple, type(old_tuple))
print("lista:", list, type(my_list))
print("nueva tupla:", new_tuple, type(new_tuple))

#%% Formas de "añadir" elementos en tupla
# Conversión a lista
old_tuple = ("apple", "banana", "cherry")
my_list = list(old_tuple)
my_list.append("kiwi")
new_tuple = tuple(my_list)

print("tupla inicial:", old_tuple, type(old_tuple))
print("my_list:", my_list, type(my_list))
print("nueva tupla:", new_tuple, type(new_tuple))
#%% Añadir tupla a tupla
thistuple = ("apple", "banana", "cherry")
y = ("orange",) # Hay que colocar coma final para que se reconozca como tupla
thistuple += y  # concatenación

print("tupla final:", thistuple, type(thistuple))
#%% Quitar elementos de tupla
    # Como no se pueden quitar elementos de una tupla podemos convertir en lista, editar y crear nueva tupla

thistuple = ("apple", "banana", "cherry")
my_list = list(thistuple)
my_list.remove("apple")
thistuple = tuple(my_list)
print("tupla actual:", thistuple, type(thistuple))

#%% del - borra de memoria la tupla (usar con cuidado)
thistuple = ("apple", "banana", "cherry")
print(thistuple)
del thistuple
print(type(thistuple))  # Tira error porque la tupla ya no está definida
