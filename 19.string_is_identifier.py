#%% isidentifier verifica si el str es username válido con
# a-z, 0-9 y _ 
# no puede haber espacios

username1 = "_myUsername"
username2 = "2username2"
username3 = "username user"
username4 = "username123"

print(username1, username1.isidentifier())
print(username2, username2.isidentifier())
print(username3, username3.isidentifier())
print(username4, username4.isidentifier())