# Resumen de los métodos de listas
#%% append()
lista = [1, 2, 3]
print("lista original:", lista)
lista.append(4)
lista.append(5)
print("lista actual:", lista)
#%% clear()
lista = [1, 2, 3]
print("lista original:", lista)
lista.clear()
print("lista clear:", lista)
#%% copy()
lista = [1, 2, 3]
print("lista original:", lista)
nueva_lista = lista.copy()
print("lista copiada:", nueva_lista)
#%% count()
lista = [1, 2, 2, 2, 3]
print("lista original:", lista)
cuenta = lista.count(2)
print("número de 2 encontrados:", cuenta)
#%% extend()
lista1 = [1, 2, 3]
lista2 = [3, 4, 5, 6]
lista1.extend(lista2)
print("lista completa:", lista1)
#%% index()
lista = [1, 2, 3]
print("índice del 2 es:", lista.index(2))
# insert()
lista = [1, 2, 3]
lista.insert(0, 5) # si pasamos un índice superior lo pone al final
print("lista con nuevo elemento:", lista)
#%% pop()
lista = [1, 2, 3]
lista.pop(0) # podemos quitar elemento en índice o por defecto quita el último
lista.pop()
print("lista actual:", lista)
#%% remove()
lista = [1, 2, 3]
lista.remove(3)
print("lista actual:", lista)
#%% reverse()
lista = [1, 2, 3]
lista.reverse()
print("lista actual:", lista)
#%% sort()
lista = [1, 2, 3]
lista.sort(reverse=True)
print("lista actual:", lista)
