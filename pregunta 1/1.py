import math
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C"]
des=[]
r=[]
aocho= []
b = 8
while True:
	num=int(input("Ingrese numeros a convertir(0 para salir):"))
	if(num==0): break
	des.append(num)
	#convertir a base 8
	convertir_string = ""
	O=num
	while O:
		mod = O % b
		O= O // b
		convertir_string = chr(48 + mod + 7*(mod > 10)) + convertir_string
	aocho.append(convertir_string)
	#fin de la convercion a base 8
	N=num
	u= N % 10
	d=int(math.floor(N/10))%10
	c=int(math.floor(N/100))
	if(N<=100): 
		r.append(Centena[c]+Decena[d]+Unidad[u])
print (des)	
print (r)
print (aocho)