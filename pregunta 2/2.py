Pingles = ["I","Am","Very","Tired","Jesus","Love","You","My","Name","Is","Jose"]
Pespanol = ["yo","estoy","muy","cansado","jesus","ama","te","mi","nombre","es","jose"]
print ("Escriba una oracion en espanol")
oracion = raw_input()
l=oracion.split()
traducir=[]
print ("\n_________La oracion traducida es:_________\n")
for i in range(len(l)):
	traducir.append(Pingles[Pespanol.index(l[i])])
oracion_traducida =' '.join(traducir)
print "\t  ",oracion_traducida.upper(),"  \t"
print ("\n__________________________________________\n")