# Iteraciones en diccionarios

#%% for in
pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}
print("for in:")
for key in pepe:
    print(f"{key}: {pepe[key]}")
#%% keys
print("\nkeys:")
for k in pepe.keys():
    print(f"{k}: {pepe[k]}")
#%% values
print("\nvalues:")
for v in pepe.values():
    print(f"{v}")
#%% items
print("\nitems:")
for item in pepe.items():
    print(f"{item[0]}: {item[1]}")

print("\nitems (otra forma):")
for k,v in pepe.items():
    print(f"{k}: {v}")