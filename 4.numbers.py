#%% int
mi_int = 1
print(type(mi_int))            # class 'int'
print(type(mi_int).__name__)   # str del tipo

a1 = 1000000
a2 = 1e6
print("a1 y a2 son iguales:", a1 == a2)

#%% float
mi_float = 1.5
print(type(mi_float))            # class 'float'
print(type(mi_float).__name__)   # str del tipo

# Notación científica
G = 6.67e-11
print(G)
M_Sol = 2.0e30
M_Tierra = 6.0e24

cociente = M_Sol / M_Tierra # 1/3 millón -> 333333.333...
print(round(cociente, 5) == round(2.0/6.0 * 1e6, 5))    # había una discrepancia en el decimal 10º
                                                        # redondeamos a 5 decimales para poder comparar
print(f"El Sol tiene {int(cociente)} de veces más masa que la Tierra")

#%% complex
z1 = 2 + 1j
z2 = 1 + 1j
print(f"Suma: {z1 + z2}")
print(f"Resta: {z1 - z2}")
print(f"División: {z1 * z2}")   # El cálculo de prod y división de complejos difiere
print(f"Suma: {z1 / z2}")       # de las operaciones con números reales en general

#%% Casting
my_int = int(3.1415)
my_float = float(25)
my_complex = complex(1)

print(my_int, type(my_int).__name__)
print(my_float, type(my_float).__name__)
print(my_complex, type(my_complex).__name__)
#%% random
import random
for i in range(1,4):
    print(random.randrange(1, 100))

# %%
