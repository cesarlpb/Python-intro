#%% copy()
pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}
pepe_copy = pepe.copy()
print(pepe_copy)

#%% dict()

pepe_new_copy = dict(pepe)
print(pepe_new_copy)

#%% Comprobando igualdad con == y coincidencia con is
print("copia es idéntico a original?", pepe_copy == pepe)
print("copia ES el original?", pepe_copy is pepe)
print("nueva copia es idéntico al original?", pepe_new_copy == pepe)
print("nueva copia ES el original?", pepe_new_copy is pepe)