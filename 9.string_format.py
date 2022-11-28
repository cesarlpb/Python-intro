#%% format

my_str = """Esto es un texto más largo
de varias líneas con variable {}.
La segunda con variable {}.
Y, la última variable {}."""

print(my_str.format(123, 3.1415, 2.71))

#%% format con índices

my_str = """Esto es un texto más largo
de varias líneas con variable {2}.
La segunda con variable {1}.
Y, la última variable {0}."""

print(my_str.format(123, 3.1415, 2.71))
#%% Podemos usar format con variables
num = 123
pi = 3.1415
e = 2.71

print(my_str.format(num, pi, e))