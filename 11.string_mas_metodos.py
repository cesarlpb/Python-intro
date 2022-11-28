#%% Métodos de string

# capitalize() - upper el primer char y lower lo demás
my_str = "esto es una ORACIÓN."
print(my_str.capitalize())

#%% casefold() - similar a lower() pero puede dar más matches
my_str = "EstO Es una OraCión #cOn mAyuS# en cualquier _POSICIÓN_."
print(my_str.casefold())
print(my_str.lower())

#%% center(len, char) - devuelve un str de len de longitud y centrado con char a ambos lados
my_str = " Esto es un texto centrado "
print(my_str.center(40, "="))
print("".center(40, "-"))

# count() - devuelve número de ocurrencias de substr en str
my_str = "Este str tiene str en varias posiciones. str"
print(my_str.count("str"))          # 3
print(my_str.count("str", 15, 44))  # 2

# encode() - método para codificar el string a bytes
txt = "Esto es una oración en español."
print(txt.encode()) # utf-8
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
print(txt.encode(encoding="ascii", errors="strict"))

#%% endswith() - devuelve boolean verificando si str acaba en substr
my_str = "Hola, me llamo César."
print(my_str.endswith("César."))
print(my_str.endswith("César"))
print(my_str.endswith("César.", 4, 21))
print(my_str.endswith("César.", 4, 20))
#%% expandtabs() - cambia el valor de espacios para \t
txt = "H\to\tl\ta\t!"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#%% find() - primera ocurrencia de un substr
my_str = "Hola, estudio Python."
sub_str = "estudio"

print(my_str.find(sub_str))
print(my_str.find(sub_str, 4, 20))
print(my_str.find(my_str, 12, 21))
print(my_str.index(my_str, 12, 21))

#%% format() - podemos añadir diversas opciones de formato en los str con format()

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {1}, I'm {0}".format(36, "John")
txt4 = "My name is {}, I'm {}".format("John",36)    # importa el orden de variables

print(txt1)
print(txt2)
print(txt3)
print(txt4)

# Continuamos opciones de format en string_format.py