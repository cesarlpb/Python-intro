#%% Método que junta (join = unir) los elementos de un iterable
# como una tupla, lista, etc en un solo str usando un str como separador.

my_dict = {"name": "John", "country": "Norway"}
my_separator = "-"

print(my_separator.join(my_dict)) # une los keys del dict

my_separator = ", "
tupla = ("dato 1", "dato 2")
print(my_separator.join(tupla))