# Operadores de comparación
    # Equals: a == b
    # Not Equals: a != b
    # Less than: a < b
    # Less than or equal to: a <= b
    # Greater than: a > b
    # Greater than or equal to: a >= b

#%% Bucles if
a = input("Introduce un número:")
b = input("Introduce otro número:")
if int(b) > int(a):
  print("b es mayor")
if int(b) < int(a):
  print("a es mayor")
elif int(a) == int(b):
  print("son iguales")

#%% Forma corta de if
a = input("Introduce un número:")
b = input("Introduce otro número:")
if int(a) > int(b): print("a es mayor que b")
#%% if else en corto
a = input("Introduce un número:")
b = input("Introduce otro número:")
print("a mayor") if int(a) > int(b) else print("b mayor")
#%% Colocamos el caso del == con múltiples else
a = input("Introduce un número:")
b = input("Introduce otro número:")
print("a mayor") if int(a) > int(b) else print("Son iguales") if a == b else print("b mayor")
#%% and
a = int(input("Introduce un número:"))
b = int(input("Introduce otro número:"))
print("a es mayor y positivo") if a > b and a > 0 else print("a es mayor pero negativo") if a < 0 and a > b else print("a no es mayor")
#%% or
a = int(input("Introduce un número:"))
b = int(input("Introduce otro número:"))
print("a es mayor, positivo o par") if a > b and a > 0 or a % 2 == 0 else print("a es mayor, negativo o impar") if a < 0 and a > b or a % 2 != 0 else print("a no es mayor")
#%% pass -> no hace nada en esa condición
a = int(input("Introduce un número:"))
b = int(input("Introduce otro número:"))
if a > b:
    print("a mayor")
elif a < b:
    print("a menor")
else:
    pass