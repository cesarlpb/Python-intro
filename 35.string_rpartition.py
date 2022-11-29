#%% Análogo a partition pero por la derecha, es decir, busca la última ocurrencia

txt = "I could eat bananas all day, bananas are my favorite fruit"

print(txt.partition("bananas")) # primera ocurrencia
print(txt.rpartition("bananas"))# última ocurrencia