#%% Slice o slicing
    # Cortar un str según los índices

my_str = "Esto es un heading y no tenemos más espacio que 65 caracteres para mostrar el mensaje en el front así que recortamos este str."
# Desde el principio al caracter 62 que está en pos 61
my_new_str = my_str[:61]
print(my_new_str + "...")

#%% Desde pos 5 hasta el final
my_new_str = my_str[5:]
print(my_new_str.capitalize())

#%% Índices negativos
# ... str.
print("Último carracter del str:", my_str[-1])  # .
print("Últimos 4 caracteres:", my_str[-4:])     # str.
print("Quitamos el punto final:", my_str[-4:-1])# str

#%% Ejercicio - slice en txt más largo por oraciones

my_str = """
    Esto es un texto más largo
    de varias líneas.
    Donde queremos acortar la primera oración, la segunda.
    Y, la última.
"""

