#%% Formas de acceder a datos en tuplas
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# índice
i = 0
while i < len(thistuple):
    print(i, thistuple[i])
    i += 1

# range

print("rango 2-4 (4 no se incluye):", thistuple[2: 4])
print("rango 2 al final:", thistuple[2:])
print("rango 0 a 4 (4 no se incluye):", thistuple[:4])

# índices negativos
print("último elemento:", thistuple[-1])
print("rango de índices negativos:", thistuple[-4:-1])

# Verificación de pertenencia con in
print("Hay 'banana' en tupla?", "banana" in thistuple)
print("Hay 'pineapple' en tupla?", "pineapple" in thistuple)