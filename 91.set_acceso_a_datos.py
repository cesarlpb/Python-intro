#%% Iteración en los sets

# for in
this_set = {1, 2, 3, 4, 5}
for elemento in this_set:
    print("elemento:", elemento)

# Podemos crear un índice enumerate // pero NO es un índice en el set
for idx, val in enumerate(this_set):
    print(idx, val)

# comprobamos pertenencia con in
print("2 está en el set?", 2 in this_set)