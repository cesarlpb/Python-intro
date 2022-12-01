#%%https://www.w3schools.com/python/python_tuples.asp Tuplas

tupla = (1, "dato", [1, 2, 3])
usuario = ("Nombre", 25, "email@mail.com")

for dato in usuario:
    print("dato:", dato)

print("tupla:", usuario)

#%% Acceso por índice
usuario = ("Nombre", 25, "email@mail.com", "Nombre")
idx = 0
while idx < len(usuario):
    print(idx, usuario[idx])
    idx += 1

#%% Tupla de un elemento
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#%% Creamos tupla con tuple()

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(type(thistuple))