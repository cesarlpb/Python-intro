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
    for j in range(1,i+1):
        fila += str(i) + " "
    print(fila)