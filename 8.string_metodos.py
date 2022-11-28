#%% Aplicamos métodos al mismo string

my_str = """
    esto es un texto más largo
    de varias líneas.
    Donde queremos acortar la primera oración, la segunda.
    Y, la última.
"""

# métodos para str
print(my_str.upper())
print(my_str.lower())
print(my_str.strip().capitalize())  # Primero limpiamos str para que 
                                    # encuentre caracter para mayus
#%% strip para quitar espacios delante y detrás
print(my_str.strip())   # Quitamos espacios al principio
print(my_str.rstrip())  # Quitamos espacios al final
#%% replace
print(my_str.replace(".", ",")) # Cambiamos . por ,
print(my_str.strip().rstrip().replace("\n    ", "").split(".")) # Split por . y limpiamos strs

#%% Limpiamos las oraciones del ej con métodos
lst = my_str.strip().rstrip().replace("\n    ", "").split(".")
print("Oraciones:")
for oracion in lst:
    if oracion != '':
        print(oracion.capitalize() + ".")

# %%
