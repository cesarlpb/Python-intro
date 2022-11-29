#%% is_decimal() se usa en objetos unicode para comprobar si 
# respresentan valores numéricos

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print("{}".format(a.encode('utf-8')), a.isdecimal())
print("{}".format(b.encode('utf-8')), b.isdecimal())
# %%
