# Operadores en Python

#%% Arithmetic operators
    # + - * /
    # % ** //
    # Siendo // la división floor -> división entera que redondea hacia abajo
print(15 // 2)
#%% Assignment operators
    # = += -= *= /=
    # %= **= //=
    # Bitwise + asignación
#%% Comparison operators
    # == != > < >= <=
#%% Logical operators
    # and or not
# and - todas las condiciones deben ser True para que devuelva True
print(7 > 5 and 6 < 10)

print("\nTabla de verdad AND")
print("".ljust(20, "-"))
my_bool1 = True
my_bool2 = True

espacio = 25
print(f"#1\t\t #2\t #1 AND #2".center(espacio))
print(f"{my_bool1}\t{my_bool2}\t| {my_bool1 and my_bool2}".center(espacio))
print(f"{not my_bool1}\t{my_bool2}\t| {not my_bool1 and my_bool2}".center(espacio))
print(f"{my_bool1}\t{not my_bool2}\t| {my_bool1 and not my_bool2}".center(espacio))
print(f"{not my_bool1}\t{not my_bool2}\t| {not my_bool1 and not my_bool2}".center(espacio))

# or
print("\nTabla de verdad OR")
print("".ljust(20, "-"))
print(f"#1\t\t #2\t #1 OR #2".center(espacio))
print(f"{my_bool1}\t{my_bool2}\t| {my_bool1 or my_bool2}".center(espacio))
print(f"{not my_bool1}\t{my_bool2}\t| {not my_bool1 or my_bool2}".center(espacio))
print(f"{my_bool1}\t{not my_bool2}\t| {my_bool1 or my_bool2}".center(espacio))
print(f"{not my_bool1}\t{not my_bool2}\t| {not my_bool1 or not my_bool2}".center(espacio))

# not
print("\nTabla de verdad NOT")
print("".ljust(20, "-"))
print(f"#1 \t NOT #1".ljust(espacio))
print(f"{my_bool1}\t| {not my_bool1}".ljust(espacio))
print(f"{not my_bool1}\t| {my_bool1}".ljust(espacio))
#%% Identity operators

#%% Membership operators

#%% Bitwise operators
