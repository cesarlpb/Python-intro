#%% index() permite encontrar la primera ocurrenci del substr
# Arroja un error si no encuentra el substr

txt = "Hello, welcome to my world."

x = txt.index("welcome", 6, 26)

print(x)
#%% ValueError
txt = "Hello, welcome to my world."

x = txt.index("q")

print(x) # ValueError: substring not found

"""
    Es similar a find() pero find devuelve -1 si no 
    encuentra el string
"""
