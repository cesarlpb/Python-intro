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