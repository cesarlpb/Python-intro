#%% Formas de iterar una tupla

tupla = (1, 2, 3, 4, 5)
# for in
print("for in")
for el in tupla:
    print(el, end=" ")

print(" ")
# enumerate()
print("enumerate() \nidx  val")
for idx, val in enumerate(tupla):
    print(idx, "   ", val)

# range()
print("range() \ni  val")
for i in range(len(tupla)):
    print(i, " ", tupla[i])

# while
print("while \ni  val")
idx = 0
while idx < len(tupla):
    print(idx, " ", tupla[idx])
    idx += 1
