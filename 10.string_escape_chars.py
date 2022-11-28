#%% Escapar caracteres especiales
#%% Escapar ""
my_str = "He visto la última película de 'Thor'."
print(my_str)
my_str = "He visto la última película de \'Thor\'."
print(my_str)
my_str = "He visto la última película de \"Thor\"."
print(my_str)
#%% \
my_str = "La ruta del archivo empieza por C:\\\\Users:..."
print(my_str)
#%% \n \r\n
my_str = "La ruta de la web empieza por http:\\\\ \nel dominio es: midominio\ncon extensión: .yo"
print(my_str)
my_str = "La ruta de la web empieza por http:\\\\ \r\nel dominio es: midominio\ncon extensión: .yo"
print(my_str)
#%% \t
my_str = "\t\tTítulo\nLa ruta de la web empieza por http:\\\\ \n\tel dominio es: midominio\n\tcon extensión: .yo\n\t\tEsto está doblemente tabulado"
print(my_str)
#%% \b
my_str = "Esto tiene un \bespacio\nEsto tiene  \bdos espacios.\nEsto tiene   \b\btres espacios."
print(my_str)
#%% \f
my_str = "Esto es un envío de formulario.\f"
print(my_str)
print("Después del form.")
print("\f", "Después del \\f", end="") # resultado: espacio en blanco
print("Algo más.")  # \f no corta los siguientes prints.
#%% Octal - https://onlinestringtools.com/convert-string-to-octal
my_octal_str = "\105\163\164\157\40\145\163\40\165\156\40\155\145\156\163\141\152\145\56"
print("Mensaje en octal:", my_octal_str)
#%% Hex - https://onlinestringtools.com/convert-string-to-hexadecimal
my_hex_str = "\x45\x73\x74\x6f\x20\x65\x73\x20\x75\x6e\x20\x6d\x65\x6e\x73\x61\x6a\x65\x20\x65\x6e\x20\x68\x65\x78"
print(my_hex_str)