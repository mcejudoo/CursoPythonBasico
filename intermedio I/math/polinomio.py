#Generador del polinomio para cambiar un numero a base 10

numero = 10001001

numero = 324
pos = 0
base = 10
L = []

while numero > 0:
        cifra = numero % 10
        L = L + [cifra]  
        numero = numero // 10

print (L)
print ("\nPolinomio:")

num2 = 0
for d in L:
        num2 += d * base ** pos
        pos += 1

print ("numero resultante: ", num2)

        
