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

# complex

# random
# %%
