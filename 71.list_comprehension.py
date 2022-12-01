#%% Ejemplos de sintaxis de list comprehension

# Se crea una nueva lista para aquellas frutas que contienen "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("for:", newlist)

#%% List comprehension
# Sintáxis
# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [el for el in fruits if "a" in el]
print("list comprehension:", newlist)

#%% Otro ejemplo

# Lista sin "apple"
newlist = [x for x in fruits if x != "apple"]
print("list comprehension:", newlist)

#%% Si omitimos condición final iteramos todos los elementos

newlist = [x for x in fruits]
print("nueva lista:", newlist)

#%% Listado de números con range

newlist = [x for x in range(1, 11)]
print("nueva lista:", newlist)

#%% Añadiendo una condición al rango

newlist = [x for x in range(10) if x < 5]
print("nueva lista:", newlist)

#%% Aplicando método de string en expresión

newlist = [x.upper() for x in fruits]
print("nueva lista:", newlist)

#%% Colocar todos los valores constantes en lista
newlist = ['x' for x in fruits]
print("nueva lista:", newlist)
#%% Condición inicial más compleja
newlist = [x if x != "banana" else "new_banana" for x in fruits]
print("nueva lista:", newlist)