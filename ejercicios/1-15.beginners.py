# Basado en https://pynative.com/python-basic-exercise-for-beginners/

#%% 1 - Prod y suma de dos números
def prod(a, b):
    return a * b

def suma(a, b):
    return a + b

def calc(a, b):
    if a * b <= 1000:
        res = prod(a, b)
    else: 
        res = suma(a, b)
    return res

print(calc(20, 30))
print(calc(40, 30))
#%% 2 - Print de suma num actual con anterior
suma = 0
actual = 0
prev = 0
while actual < 10:
    print(actual, prev, actual + prev)
    actual += 1
    prev = actual - 1
#%% 3 - Escribir chars en índices pares de un str

def get_even_chars(string):
    idx = 0
    new_str = ""
    while idx < len(string):
        if idx % 2 == 0:
            char = string[idx]
            new_str += char
        idx += 1
    return new_str

my_str = "EstoEsUnMensaje."
my_str2 = "pynative"

print(get_even_chars(my_str))
print(get_even_chars(my_str2))

#%% 4 - Quitar n chars de string
def remove_chars(string, n):
    return string[n:]

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

#%% 5 - Comprobar lista

def check_list(lst):
    return lst[0] == lst[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(check_list(numbers_x))
print(check_list(numbers_y))

#%% 6 - Print múltiplos de 5

nums = [10, 20, 33, 46, 55]

for num in nums:
    if num % 5 == 0:
        print(num)

#%% 7 - Cuenta de substr en str

def contar_substr(string, substr):
    return string.count(substr)

my_str = "Emma is good developer. Emma is a writer"
contar_substr(my_str, "Emma")

#%% 8 Escribimos triángulo de números

for i in range(1, 6):
    fila = ""
    # nos sirven los rangos
    # 0,i -> 0,1 o 0,1,2...
    # 1,i+1 -> 1,2 o 1,2,3... 
    for j in range(0,i):
        fila += str(i) + " "
    print(fila)
#%% 9 - Palíndromo

my_str = "Anna"
my_str2 = "129"
        #012 n -> 3
        # idx -> n-idx-1
        # 0 -> 3 - 0 - 1 = 2
my_str3 = "1231"
my_str4 = "qwertytrewq"

def is_palindrome(string):
    idx = 0
    n = len(string)
    lower_str = string.lower()
    while idx < n // 2:
        if not lower_str[idx] == lower_str[n-idx-1]: 
            return False
        idx += 1
    return True

print(my_str, is_palindrome(my_str))
print(my_str2, is_palindrome(my_str2))
print(my_str3, is_palindrome(my_str3))
print(my_str4, is_palindrome(my_str4))

#%% 10 Mezclar listas números par / impar

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# suponemos que son listas del mismo tamaño
def combinar_listas(list1, list2):
    idx = 0
    new_lst = []
    while idx < len(list1):
        if list1[idx] % 2 != 0:
            new_lst.append(list1[idx])
        if list2[idx] % 2 == 0:
            new_lst.append(list2[idx])
        idx += 1
    new_lst.sort()
    return new_lst

print(combinar_listas(list1, list2))

#%% 11 - Inversión de num

def invertir_num(num):
    my_str = str(num)
    new_str = ""
    idx = len(my_str) - 1
    while idx >= 0:
        new_str += my_str[idx] + " "
        idx -= 1
    return new_str

print(invertir_num(7536))
print(invertir_num(1005))

#%% 12 - Cálculo de tramos de impuestos

def calc_taxes(num):
    # porcentajes de cada tramo
    tramos = [0, 10, 20]
    
    if num > 10000 and num < 20000:
        cantidades = [10000, num-10000, 0]
    elif num > 20000:
        cantidades = [10000, 10000, num-20000]
    else:
        cantidades = [num, 0, 0]

    # cantidades tiene el mismo tamaño
    # que tramos
    idx = 0
    suma = 0
    while idx < len(cantidades):
        cantidades[idx] = cantidades[idx] * tramos[idx]/100
        suma += cantidades[idx]
        idx += 1

    return (cantidades, suma)

print(calc_taxes(9999))
print(calc_taxes(15000))
print(calc_taxes(45000))

#%% 13 - Tabla de multiplicar

def crear_tabla(num):
    tabla = ""
    for i in range(1, num + 1):
        fila = ""
        for j in range(1, num + 1):
            fila += str(i * j) + "\t"
        fila = fila.expandtabs(num // 3) # 3 para num=10 y 5 para num=20
        fila = fila.ljust(num * 5)       # 30 chars para 10 y 105 para 20
        tabla += fila + '\n'
    return tabla

print(crear_tabla(10))
print(crear_tabla(20))

#%% 14 - Triángulo de chars

def dibujar_triangulo(num, char):
    idx = num
    triangulo = ""
    while idx > 0:
        linea = "".ljust(idx, "+").replace("+", f"{char} ")
        triangulo += linea + '\n'
        idx -= 1
    return triangulo

print(dibujar_triangulo(5, "*"))
print(dibujar_triangulo(10, "o"))

#%% 15 - Calcular exponencial

def calc_exp(base, exp):
    return base ** exp

print(calc_exp(10, 2))  # 100
print(calc_exp(0, 0))   # 1
print(calc_exp(10, -2)) # 0.01
print(calc_exp(10, 6)) # 0.01