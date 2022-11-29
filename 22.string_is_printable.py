#%% Verifica si los chars se pueden "imprimir"
# Chars no imprimibles son: \n \r \r\n \t ...

txt1 = "Hello!\tAre you #1?" # False por \t
txt2 = "Hello!\rAre you #2?" # False por \r
txt3 = "Hello! Are you #3?"  # True

print(txt1, txt1.isprintable())
print(txt2, txt2.isprintable())
print(txt3, txt3.isprintable())