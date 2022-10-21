# conjuntos:

L = [1,2,3,4]

s = {}
s[0] = 12
s[45] = 55
s["gt"] = "GT"
s[0] = 23

print (s)

# Es como una lista que no admite repetidos y mantiene los elementos ordenados

s1 = set([2,1,3,4,5,5,1])
print (s1)

# no soporta asignaciones:
try:
        s1[0] = 2
        print (s1)
        
except Exception as e:
        print (e)

s = "hola"
L = list(s);
S = set(s)
print ("L:", L)
print ("S:", S)


