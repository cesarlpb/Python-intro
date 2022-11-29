#%% Encuentra la última ocurrencia el substr en el str

txt = "Mi casa, su casa."
print(txt.rfind("casa"))

txt2 = "Este es un str"
print(txt2.rfind("casa")) # retorna -1 si no lo encuentra

txt3 = "Este str es un str"
print(txt2.rfind("str", 9, 13)) # no lo encontramos
print(txt2.rfind("str", 9, 16)) # sí lo encontramos