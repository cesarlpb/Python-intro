#%% Devuelve True si cada palabra empieza por Mayúsculas
# False en caso contrario
# Más casos de validación de títulos y formatos para inglés en:
# https://capitalizemytitle.com/

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
e = "Este Es Un Título Válido"

print(a, a.istitle())
print(b, b.istitle())   # True
print(c, c.istitle())   # True
print(d, d.istitle())   # True
print(e, e.istitle())   # True