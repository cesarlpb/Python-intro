#%% Reemplaza un substr por otro en el str
    # por defecto reemplaza todos los matches pero
    # podemos pasarle un tercer param para indicar número de reemplazos 

txt = "one one was a race horse, two two was one too."

print(txt.replace("one", "1"))
print(txt.replace("one", "1", 1)) # Reemplaza solo la primera ocurrencia