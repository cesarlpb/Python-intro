#%% test

def calc_tax(num):
 
    tramos =[0, 10, 20]
 
    if num > 10000 and num < 20000:
        cantidades =  [10000, num-10000, 0]
    elif num > 20000:
        cantidades = [10000, 10000, num-20000]
    else:
        cantidades = [num, 0, 0]
     
    #cantidades tiene el mismo tamaño que tramos       
    idx = 0
    suma = 0
    while idx < len(cantidades):
        cantidades[idx] =  cantidades[idx] * tramos[idx]/100
        suma += cantidades[idx]
        idx += 1
        
    return (cantidades, suma)   
       

print(calc_tax(9999))
print(calc_tax(15000))
print(calc_tax(45000))
# %%
