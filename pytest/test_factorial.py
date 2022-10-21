"""
Prueba del factorial iterativo
"""

def fact2(n):
	r = 1
	for i in range(1,n+1):
		r *= i
		
	return r
	
	
	
def test_fact2():
	for i in range(1000):
		fact2(900)
