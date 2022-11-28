#%% Opciones de format()

my_str = "Hola, tengo {} años."
print(my_str.format(33))
#%% left-align, center y right-align

my_str = "Hola, tengo {age:<10} años."
print(my_str.format(age = 33))
my_str = "Hola, tengo {age:^10} años."
print(my_str.format(age = 33))
my_str = "Hola, tengo {age:>10} años."
print(my_str.format(age = 33))
#%% signo a la izq
my_str = "En Alaska, hace {temp:>7} grados."
print(my_str.format(temp = -10.00))
my_str = "En Alaska, hace {temp:=7} grados."
print(my_str.format(temp = -10.00))

#%% colocamos +, - o espacio según signo de forma automática
my_str = "En Alaska, hace {temp} grados."
print(my_str.format(temp = 10.00))
my_str = "En Alaska, hace {temp:-} grados."
print(my_str.format(temp = -10.00))
my_str = "En Alaska, hace {temp:+} grados."
print(my_str.format(temp = 10.00))
my_str = "En Alaska, hace {temp:} grados."
print(my_str.format(temp = 10.00))
my_str = "En Alaska, hace {temp:} grados."
print(my_str.format(temp = -10.00))
#%% separadores de coma de miles
my_str = "En el mundo, hay {pob:,} personas."
print(my_str.format(pob = 8002440850))
my_str = "En el mundo, hay {pob:_} personas."
print(my_str.format(pob = 8002440850))
#%% formato binario
my_str = "El valor binario de 25 es: {:b}"
print(my_str.format(25))
#%% unicode - no hace falta :c
my_str = "El valor unicode de mayor o igual es: {}"
char_unicode = u'\u2265'
print(my_str.format(char_unicode))
print(my_str.format(char_unicode.encode('utf-8')))
# print(my_str.format(char_unicode.encode('ascii'))) # este falla por el caracter que le pasamos
#%% binario a decimal
mi_binario = 0b1111101
my_str = "El número 1111101 del binario a decimal es: {:d}"
print(my_str.format(mi_binario))
#%% notación científica
masa_sol = 2000000000000000000000000000000
my_str = "La masa del Sol es: {:e} kg."
print(my_str.format(masa_sol))
my_str = "La masa del Sol es: {:E} kg."
print(my_str.format(masa_sol))

#%% número fijo de decimales
precio = 49.325 # euros
my_str = "Precio: {:.2f} €"
print(my_str.format(precio))