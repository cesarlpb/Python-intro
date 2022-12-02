#%% Métodos de diccionarios
navidad = {
    "responsable": "Santa Claus", 
    "regalos": ["PS5", "chuches", "juguetes"],
    "activo": True
}
# clear() - borra el diccionario, sigue siendo accesible como {}
navidad.clear()
print(navidad)
#%% copy() - crea una copia del diccionario
navidad = {
    "responsable": "Santa Claus", 
    "regalos": ["PS5", "chuches", "juguetes"],
    "activo": True
}
navidad_copy = navidad.copy()
print("copia es idéntico a original?", navidad == navidad_copy)
print("copia ES original", navidad is navidad_copy)
#%% fromkeys() - Crea dict con el iterable de keys pero con EL MISMO value // por defecto en None
keys = ["key1", "key2", "key3"]
valor_por_defecto = "valor_por_defecto"
new_dict = dict.fromkeys(keys, valor_por_defecto)
print("\ntipo:", type(new_dict))
print("nuevo diccionario:")
print(new_dict)

print("\nAlternativa con None como value")
new_new_dict = dict.fromkeys(keys)
print("nuevo nuevo diccionario:")
print(new_new_dict)
#%% get() - Devuelve el valor de la key correspondiente
print(navidad.get("\nresponsable")) # Santa Claus
print(navidad.get("asdf"))        # None -> no arroja error
#%% items() - Devuelve tuplas (key, value) // view -> se actualiza con cambios en diccionario
print("\nitems:", navidad.items())
#%% keys() - Devuelve los keys // view -> se actualiza con cambios en diccionario
print("\nkeys:", navidad.keys())
#%% pop() - Elimina el key correspondiente -> por defecto el último
navidad = {
    "responsable": "Santa Claus", 
    "regalos": ["PS5", "chuches", "juguetes"],
    "activo": True
}
print("\npop:")
navidad.pop("responsable")
print(navidad)
#%% popitem() - Borra el último elemento (item) del diccionario
navidad = {
    "responsable": "Santa Claus", 
    "regalos": ["PS5", "chuches", "juguetes"],
    "activo": True
}
print("\npopitem:")
navidad.popitem()
print(navidad)
#%% setdefault()
navidad = {
    "responsable": "Santa Claus", 
}
navidad.setdefault("responsable", "Santa") # como existe el key, no tiene efecto
navidad.setdefault("regalos", "todos") # inserta el valor en la llave regalos
navidad.setdefault("activo")    # inserta None
print("\nsetdefault:", navidad)
#%% update() - actualiza un diccionario
navidad = {
    "responsable": "Santa Claus", 
    "regalos": None,
    "activo": True
}
regalos = {
    "electronica": ["PS5", "iPhone14", "Samsung Fold"],
}
mas_regalos = {
    "programacion": ["Python", "JS", "C++"]
}
navidad["regalos"] = regalos # asigna dict a values del key "regalos"
navidad.update(mas_regalos)  # adjunta dict a diccionario navidad (al final)
print("\nupdate:", navidad)
#%% values() Devuelve los values // view -> se actualiza con cambios en diccionario
print("\nvalues:", navidad.values())
# %%
