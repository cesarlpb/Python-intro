#%% Sirve para reemplazar characteres en función de los 
# params que le pasamos 

# 1 param
txt = "Hi Sam!"
dict = {"S": "P", "i": "ola"}
mytable = txt.maketrans(dict)
print(mytable)
print(txt.translate(mytable))

# 2 params
txt = "Hi Sam!"
x = "Sm"
y = "Pt"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

# 3 params

txt = "Hi Sam!"
x = "Sm"
y = "Mt"
z = "Hi "
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))