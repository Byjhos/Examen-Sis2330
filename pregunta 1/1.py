import math
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C"]
for N in range(1,101):
	u= N % 10
	d=int(math.floor(N/10))%10
	c=int(math.floor(N/100))
	'''Funcion para  convertir a base 8'''
	def dec_a_oct(N):
		base = 0
		i = 0
		while N:
			base += (N % 8) * (10 ** i)
			N = N / 8
			i += 1
		return [base]
	'''fin de la funcion'''
	print "El numero", N ,"en romano es:"
	if(N<=100): 
	 print "[",Centena[c]+Decena[d]+Unidad[u],"]"
	print "Y en base 8 es:"
	print dec_a_oct(N)