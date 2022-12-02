#%% Bucles while

i = 0
print("Números del 0 al 9:")
while i < 10:
    print(i, end=" ")
    i += 1

#%% break
i = 0
print("Números del 0 al 5:")
while i < 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1

#%% continue
i = 0
print("Números del 0 al 9 quitando rango del 4 al 6:")
while i < 9:
    i += 1
    if i > 3 and i < 7:
        continue
    print(i, end=" ")
    
#%% while - else
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
else:
    print("\nHemos llegado al 10")