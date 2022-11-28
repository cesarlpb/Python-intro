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
# Sabiendo que cada OS (Windows, Mac, o Linux)
# salta línea en strings así:
UNIX_NEWLINE = '\n'
WINDOWS_NEWLINE = '\r\n'
MAC_NEWLINE = '\r'

chars_saltos_de_linea = ['\n', '\r\n', '\r']
oracion = ""
oraciones = []
i = 0
char = my_str[i]

while(char != "." and i < len(my_str) - 1):
    if char not in chars_saltos_de_linea:
        oracion += char
    i += 1
    char = my_str[i]

print("oracion:", oracion)

# Limpiamos los espacios del medio de la oración
oracion_sin_espacios_iniciales = oracion[4:]
print(oracion[4:].find("    "))
print(oracion_sin_espacios_iniciales[:26], oracion_sin_espacios_iniciales[30:])
oracion_final = oracion_sin_espacios_iniciales[:26] + " " + oracion_sin_espacios_iniciales[30:]
print(oracion_final)

#%% Buscamos puntos para saber donde están las oraciones
i = 0
c = my_str[i]
puntos = [] # 0, 1, 2 

while (i < len(my_str) - 1):
    if(c == '.'):
        puntos.append(i)
    i += 1
    c = my_str[i]

print("Índices de los puntos:", puntos)

oracion1 = my_str[4:puntos[0]+1]
oracion2 = my_str[puntos[0]+1:puntos[1]+1]
oracion3 = my_str[puntos[1]+1:puntos[2]+1]

print(oracion1)
print(oracion2)
print(oracion3)

# %%
