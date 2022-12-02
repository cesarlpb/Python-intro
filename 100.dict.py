#%% Diccionarios
    # - Ordenados desde +3.7
    # - Editables
    # - No admiten duplicados (en keys)

this_dict = {
  "brand": "Ford",
  "model": "dato a sobreescribir",
  "model": "Mustang",
  "year": 1964
}
# si colocamos keys idénticos hay una sobreescritura
# y solo el último valor se guarda
print(this_dict)

#%% bucle
print("{")
for key in this_dict:
    print(f"\t{key}: {this_dict[key]}".expandtabs(4))
print("}")

#%% len para conocer tamaño de arrays de keys o values
print(len(this_dict))

#%% Tipos de datos almacenados
this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(this_dict)
print(type(this_dict))

#%% constructor
this_dict = dict(name = "John", age = 36, country = "Norway")
print(this_dict)
print(type(this_dict))