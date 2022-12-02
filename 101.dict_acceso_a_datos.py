#%% Acceso a datos en dict
    # - get(key) -> conseguimos un dato de la llave que le pasamos
    # - keys() -> lista que se actualiza si se añaden valores en el dict -> view
    # - values() -> también se actualiza si hay nuevas entradas

pepe = {
    "Nombre": "Pepe", 
    "Apellido": "The Frog", 
    "color": "verde",
    "edad": 3
}

print("Nombre", pepe.get("Nombre"))

#%% keys(), values()
print("Usando un for:")
keys = pepe.keys()
values = pepe.values()

# keys
for k in keys:
  print(f"{k}: {pepe.get(k)}")

# values
for v in values:
    print(v)

#%% Comprobamos que keys y values se actualizan el editar el dict

print("keys:", keys)
print("values:", values)
keys_lst = list(keys)
values_lst = list(values)
print("lista de keys:", keys_lst)    # tiene 4 datos
print("lista de values:", values_lst)# tiene 4 datos

pepe["nuevo_key"] = "nuevo valor"

print("keys:", keys)    # ahora tiene 5 datos
print("values:", values)# ahora tiene 5 datos
print("lista de keys:", keys_lst)    # sigue con 4 datos
print("lista de values:", values_lst)# sigue con 4 datos   
#%% items() -> retorna pares key, value en tuplas

# Iteramos todos los items del dict
pepe_items = pepe.items()   # también se actualiza si cambian los datos del dict

print("items:")
for item in pepe_items:
    print(item)
print("\nkeys:")
# Solo keys
for item in pepe_items:
    print(item[0])
print("\nvalues:")
# Solo values
for item in pepe_items:
    print(item[1])
print("\nitems:")
#Ambos con índice
for item in pepe_items:
    print(item[0], item[1])

#%% Comprobamos que items se actualiza
print("Hay items:", len(pepe_items))
pepe["sonido"] = "croac"
print("Hay items:", len(pepe_items))

#%% Comprobación de key en dict
keys = pepe.keys()

# Mirando en keys
print("Existe 'sonido' en dict?", "sonido" in keys)
print("Existe 'algo_random' en dict?", "algo_random" in keys)

# Mirando en dict -> comprueba keys
print("Existe 'sonido' en dict?", "sonido" in pepe)
print("Existe 'algo_random' en dict?", "algo_random" in pepe)

#%% Comprobación de values en dict

values = pepe.values()

# Mirando en keys
print("Existe 'croac' en dict?", "croac" in values)
print("Existe 'algo_random' en dict?", "algo_random" in values)