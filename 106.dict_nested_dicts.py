#%% Diccionarios anidados
memes_dict = {
            "meme_1": "meme1.gif",
            "meme_2": "meme2.gif",
            "meme_3": "meme3.gif",
            "dict": {}
        }
        
pepe = {
    "nombre": "Pepe Original", 
    "apellido": "The Frog", 
    "color": "verde",
    "pepe_anidado_1": {
        "nombre": "Pepe Anidado 1", 
        "memes": memes_dict
        }, 
    "pepe_anidado_2": {
        "nombre": "Pepe Anidado 2", 
        },
    "pepe_anidado_3": {
        "nombre": "Pepe Anidado 3", 
        }
    }

# Navegamos entre los diccionarios

pepe_keys = pepe.keys()
print(pepe_keys)

print("\nDeterminamos que keys son dict:")
for k in pepe_keys:
    print(type(pepe[k]).__name__ == 'dict')

#%% Creamos una lista de keys que contienen diccionarios
dict_key_list = []
for k in pepe_keys:
    es_dict = type(pepe[k]).__name__ == 'dict'
    if es_dict:
        dict_key_list.append(k)
print("keys que contienen dict:", dict_key_list)

#%% Diccionarios encontrados en pepe
print("\nDiccionarios encontrados:")
for k in dict_key_list:
    print("Diccionario:", pepe[k])

# Idea de ejercicio: iterar (while ?) para conseguir toda la lista de diccionarios anidados
"""
    pepe
        pepe_anidado_1
            memes
                dict
                    ...
        pepe_anidado_2
        pepe_anidado_3
"""
