#%% Devuelve una lista con cada uno de los str entre saltos de línea

my_multiline_str = """Esto es un texto más largo de varias líneas con variable.
    La segunda con variable.
    Y, la última variable."""

my_inline_str = "Thank you for the music\nWelcome to the jungle"

print(my_multiline_str.splitlines())
print(my_inline_str.splitlines())
print(my_inline_str.splitlines(True))   # incluimos \n