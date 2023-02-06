"""
Prueba con cadenas:
"""

# Comprobar si una cadena palíndromo:
s = "narran"

for i in s:
    print(i)

for pos, i in enumerate(s):
    print(pos, i)

# Slicing: 
print(s[1:-1])

if s == s[::-1]:
    print(s,'es palindromo')
else:
    print('No lo es')

# modificar elementos:
# s[0] = 'H' ERROR!

print('len: ', len(s))
print('min: ', min(s))