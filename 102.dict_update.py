#%% Añadir y editar datos en dict

pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}

pepe["edad"] = 4    # actualizar o añadir campos
pepe.update({"edad": 5})
pepe.update({"dato_no_existente": "algo"}) # Añade el dato al dict

print("Edad actual:", pepe["edad"])

print(pepe) # ahora tiene 5 keys, values

#%% update()
    # Añadimos varios datos
pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}

pepe.update({
    "dato_nuevo1": "algo_1",
    "dato_nuevo2": "algo_2",
    "dato_nuevo3": "algo_3"
    }) 
print("\nupdate con datos:")
print(pepe) 

new_dict = {
    "dato_nuevo4": "algo_4",
    "dato_nuevo5": "algo_5",
    "dato_nuevo6": "algo_6"
}

pepe.update(new_dict)
print("\nupdate con dict:")
print(pepe)