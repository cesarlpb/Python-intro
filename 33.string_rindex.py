#%% Encuentra la última ocurrencia el substr en el str
    # Similar a rfind pero arroja un error si no encuentra el substr

txt = "Mi casa, su casa."
print(txt.rindex("casa"))

txt2 = "Este es un str"
# print(txt2.rindex("casa")) # arroja error

txt3 = "Este str es un str"
print(txt2.rindex("str", 9, 16)) # sí lo encontramos
print(txt2.rindex("str", 9, 13)) # no lo encontramos
# %%
