# Quitar elementos del dict y borrar diccionario

#%% pop()
pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}
pepe.pop("edad")
print("keys actuales:", pepe.keys())
# popitem()
pepe.popitem()
print("keys actuales:", pepe.keys())
# del
del pepe["Apellido"]
print(pepe)
#%% clear()
pepe.clear()
print(pepe)
# del dict
del pepe
print(pepe) # Error -> pepe no definido
# %%
