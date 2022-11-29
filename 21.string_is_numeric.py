#%% isnumeric() verifica que los chars son dígitos
# se adminten superíndices y fracciones como: ² o ¾

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
f = '²'
g = '¾'

print(a.encode(), a.isnumeric())
print(b.encode('utf-8'), 'o ²', b.isnumeric())
print(c, c.isnumeric())
print(d, d.isnumeric())
print(e, e.isnumeric())
print(f, f.isnumeric())
print(g, g.isnumeric())