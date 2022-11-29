#%% Devuelve una tupla con:
    # lo que viene antes de la primera ocurrencia del substr
    # el match del substr
    # lo que viene después del match

txt = "I could eat bananas all day"
my_tuple = txt.partition("bananas")
print(my_tuple)

print("\nIteramos tupla:")
for i in range(3):
  print(i, my_tuple[i])

print("\nCuando no hay match:")
# En caso de no encontrar el substr devuelve:
    #(txt, '' ,'')
txt = "I could eat bananas all day"
print(txt.partition("apples"))