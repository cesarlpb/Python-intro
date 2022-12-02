#%% Bucles for

frutas = ["apple", "banana", "cherry"]
for fruta in frutas:
  print(fruta)

for char in "Esto es un string.":
    if char == ".":
        break
    print(char, end=" ")

#%% break
frutas = ["manzana", "pera", "kiwi"]
frutas_aceptadas = ["pera", "manzana"]
for fruta in frutas:
    if fruta not in frutas_aceptadas:
        break
    print(fruta)
#%%
for fruta in frutas:
    if fruta in frutas_aceptadas:
        continue
    print(fruta)