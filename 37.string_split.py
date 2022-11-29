#%% Hace el split desde la izq y si no le indicamos maxsplit 
# equivale a split()
    # Devuelve n+1 elementos si maxsplit es n

txt = "apple, banana, cherry, orange, pineapple"

print(txt.split(", ", 1)) # devuelve 2 elmentos
print(txt.split(", ", 2)) # devuelve 3 elementos
# Similar a split():
mi_split = txt.split(", ")
mi_rsplit = txt.rsplit(", ")
print(mi_split)      # 5 elementos
print(mi_rsplit)     # 5 elementos

print("Son iguales?", mi_rsplit == mi_split)