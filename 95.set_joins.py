#%% union() - genera un nuevo set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("set3:", set3)

# update() - añade elementos al primer set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print("set1:", set1)

# intersección -> intersection_update()
    # modifica el primer set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print("set1:", set1)

# intersección con intersection()
    # retorna un nuevo set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

interseccion = set1.intersection(set2)
interseccion2 = set2.intersection(set1)

print("intersección 1 con 2:", interseccion)
print("intersección 2 con 1:", interseccion2)

# symmetric_difference_update()
    # Mantiene todos los que NO están en ambos
    # modifica el primer elemento
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print("set1:", set1)

# symmetric_difference()
    # retorna nuevo set
    # elementos no presentes en ambos sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
my_bool = set1.symmetric_difference(set2) == set2.symmetric_difference(set1)
print("set1:", set3)
print("Las operaciones son equivalentes:", my_bool)
