#%% Sort en listas - sort()

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("orden alfabético:", thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("sort() en números:", thislist)

#%% sort() en orden desc

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print("orden desc:", thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print("sort() en números:", thislist)

#%% Personalización del sort()

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("ordenación usando myfunc:", thislist)

#%% case insensitive

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("primero sort() en mayus:", thislist)

# Aplicamos una transformación a lower para ordenar de forma correcta todos los elementos:
new_list = [x.lower() for x in thislist]
new_list.sort()
print("sort() con lower():", new_list) # imprimimos lista YA ordenada
# Este métodos SI modifica los elementos originales de la lista

# Aplicando str.lower a cada elemento como param de sort()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print("lista ordenada con str.lower", thislist)
# Este método no transforma el lower/uppercase de los elementos

#%% Reverse

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("lista en orden inverso:", thislist)