#%% Set
    # - No hay índice
    # - No están ordenados
    # - No se admiten duplicados

this_set = {"apple", "banana", "cherry"}
print("set:", this_set, len(this_set), type(this_set))

# No se pueden repetir elementos
set3 = {True, False, False}
print(set3)

# Creando set con el constructor set()
this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print("set:", this_set)