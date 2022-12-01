#Unpacking de tuplas
    # Asignación de los datos de la tupla a variables

#%% Unpacking con nombre de variables
usuario = ("Pepe", "Gonzalez", 25, "pepe@gonzalez.com", "Soy un fan de Python")

(nombre, apellido, edad, email, bio) = usuario

print("""
    Datos de usuario:
    - Nombre:\t{0}
    - Apellido:\t{1}
    - Edad:\t\t{2} años
    - Email:\t{3}
    - Bio:\t\t{4}
""".format(nombre, apellido, edad, email, bio))

#%% Unpacking con *

# Ejemplo 1
print("Ejemplo 1")
usuario = ("Pepe", "Gonzalez", 25, "pepe@gonzalez.com", "Soy un fan de Python")
(nombre, apellido, *datos) = usuario
datos_formateados = ""
for dato in datos:
    datos_formateados += f"\n\t-- dato:\t {dato}"
print("""
    Datos de usuario:
    - Nombre:\t{0}
    - Apellido:\t{1}
    - Datos de Lista:\t{2}
""".format(nombre, apellido, datos_formateados))

print("".center(40, "-"))
# Ejemplo 2
print("Ejemplo 2")
usuario = ("Pepe", "Gonzalez", 25, "pepe@gonzalez.com", "HTML", "CSS", "JS", "Python", "Soy un fan de Python")
(nombre, apellido, edad, email, *lenguajes, bio) = usuario
datos_formateados = ""
for dato in lenguajes:
    datos_formateados += f"\n\t-- Lenguaje:\t {dato}"
print("""
    Datos de usuario:
    - Nombre:\t{}
    - Apellido:\t{}
    - Edad:\t{}
    - Email:\t{}
    - Tecnologías que conoce el usuario:\t{}
    - Bio:\t{}
""".format(nombre, apellido, edad, email, datos_formateados, bio))