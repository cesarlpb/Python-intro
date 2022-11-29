#%% startswith() - devuelve boolean verificando si str empieza en substr
my_str = "Hola, me llamo César."
print(my_str.startswith("Hola,"))       # True
print(my_str.startswith("Hola "))       # no es match exacto
print(my_str.startswith("me", 8, 21))   # pasamos un rango sin "me"
print(my_str.startswith("me ", 6, 20))  # True