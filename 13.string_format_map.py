#%% format_map() permite pasar un diccionario al string 
# con variables para colocar en las plantillas

# input stored in variable a.
a = {'x':'John', 'y':'Wick', 'z': 3.0}

# Use of format_map() function
print("{x} {y} tiene {z} películas.".format_map(a))

#%% Más info: https://www.geeksforgeeks.org/python-string-format_map-method/
