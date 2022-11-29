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
precio = 49.32512121 # euros
iva = precio * 0.21  # euros
total = precio + iva # euros
my_str = """
    Precio base :\t {:.2f} €
    IVA (21%)   :\t {:.2f} €
    Precio total:\t {:.2f} €
"""
print(my_str.format(precio, iva, total))
#%% :F -> INF y NAN
inf = float('inf')
nan = float('nan')
num = 1/3
my_str = "Infinito con f: {:f}\nInfinito con F: {:F}"
print(my_str.format(inf, inf))
my_str = "NAN con f: {:f}\nNAN con F: {:F}"
print(my_str.format(nan, nan))
my_str = "Num con f: {:.3f}\nNum con F: {:.3F}"
print(my_str.format(num, num))
#%% g y G
num = 2/3
num2 = 1000000000
my_str = "Num con g: {:g} y num con G: {:G}"
print(my_str.format(num, num))
my_str = "Num2 con g: {:g} y num2 con G: {:G}"
print(my_str.format(num2, num2))
#%% Octal con :o
my_num = 5050 # 11672 en octal
my_str = "{0} en octal es {1:o}"
print(my_str.format(my_num, my_num))
#%% Hex con :x y :X
my_num = 5050 # 13ba o 13BA en hex
my_str = "{0} en hex con x: {1:x} y con X: {2:X}"
print(my_str.format(my_num, my_num, my_num))

#%% Formato de número con :n y variantes
num1 = 3e9
num2 = 3e-9
num3 = 2.123456e12
my_str = "{:n}\t {:.10f}\t {:7.2e}"
print(my_str.format(num1, num2, num3))
#%% Formato de %
my_num = 25/100
my_num2 = 50.12/100
my_num3 = 99.11111111/100

my_str = "{:.2%}\t {:.2%}\t {:.3%}"
print(my_str.format(my_num, my_num2, my_num3))
