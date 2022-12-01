#%% Copia de lista

thislist = ["apple", "banana", "cherry"]
thislist2 = thislist
new_list = thislist.copy()
new_new_list = list(thislist)
print("lista original:", thislist)
print("lista2 con misma ref a lista1:", thislist2)
print("nueva lista", new_list)
print("nueva lista con list()", new_new_list)

#%% Modificamos lista 1

thislist.append("nuevo elemento")

print("lista original:", thislist)
print("lista2 con misma ref a lista1:", thislist2)
print("nueva lista con copy()", new_list)
print("nueva lista con list()", new_new_list)