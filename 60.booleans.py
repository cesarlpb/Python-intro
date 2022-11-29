#%% True o False
# Ejemplo de bucle if

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#%% Evaluación de variables
print("Variables:")
print("Hello", "\t", bool("Hello"))
print("", "\t", bool(""))
print(" ", "\t", bool(" "))

print(15, "\t", bool(15))
print(None, "\t", bool(None))
print(0, "\t", bool(0))

print("\nColecciones:")
print([], bool([]))
print(["1", "2", "3"], bool(["1", "2", "3"]))

#%% False
espacio = 7
print(str(False).ljust(espacio, " "), bool(False))
print(str(None).ljust(espacio, " "), bool(None))
print(str(0).ljust(espacio, " "), bool(0))
print("".ljust(espacio, " "), bool(""))
print(str(()).ljust(espacio, " "), bool(()))
print(str([]).ljust(espacio, " "), bool([]))
print(str({}).ljust(espacio, " "), bool({}))

# Caso particular de retorno de False con clase personalizada
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(f"__len__ -> {myobj.__len__()}".ljust(15, " "), bool(myobj))  # False

#%% Boolean como retorno de función
def myFunction() :
  return True

print("myFunction() ->", myFunction())

#%% Funciones que devuelven boolean

num = 200
print(isinstance(num, int))
print(isinstance(num, float))

z = 1 + 1j
print(isinstance(z, complex))