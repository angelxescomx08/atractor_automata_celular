from graphviz import Digraph

class Atractor():
		
	def convertir(self,exp):
		return int(exp)

	def getEstados(self,n):
		estados = []
		temp = self.convertir(n)
		num_estados = 2**temp
		for i in range(num_estados):
			estados.append(format(i,'0'+str(n)+'b'))
		return estados

	def comparar(self,cad, regla):
		estado = []
		for i in range(len(cad)):
			if(int(cad[i-1])==int(cad[i])==int(cad[(i+1)%len(cad)])==1):
				estado.append(regla[0])
			elif(int(cad[i-1])==int(cad[i])==1 and int(cad[(i+1)%len(cad)])==0):
				estado.append(regla[1])
			elif(int(cad[i-1])==int(cad[(i+1)%len(cad)])==1 and int(cad[i])==0):
				estado.append(regla[2])
			elif(int(cad[i])==int(cad[(i+1)%len(cad)]) == 0 and int(cad[i-1]) == 1):
				estado.append(regla[3])
			elif(int(cad[i-1])==0 and int(cad[i])==int(cad[(i+1)%len(cad)])==1):
				estado.append(regla[4])
			elif(int(cad[i-1])==int(cad[(i+1)%len(cad)])==0 and int(cad[i])==1):
				estado.append(regla[5])
			elif(int(cad[i-1])==int(cad[i])==0 and int(cad[(i+1)%len(cad)])==1):
				estado.append(regla[6])
			elif(int(cad[i-1])==int(cad[i])==int(cad[(i+1)%len(cad)])==0):
				estado.append(regla[7])
		return estado

	def evolucionar(self,regla,estados):
		relacion = []
		regla_binaria = format(int(regla),'08b')
		for i  in range(len(estados)):
			aux="".join(map(str,self.comparar(estados[i],regla_binaria)))
			relacion.append((estados[i],aux))
		return relacion

	def generar_imagen(self,tam,regla):
		self.diagrama = Digraph(
			format='jpg',
			engine='neato',
			node_attr={'color': 'lightblue2', 'style': 'filled'},
			filename='atractor'
		)
		self.nodos = self.getEstados(tam)
		self.aristas = self.evolucionar(regla,self.nodos)
		for i in range(len(self.aristas)):
			ini = int(self.aristas[i][0],2)
			fin = int(self.aristas[i][1],2)
			rgb = '#%02x%02x%02x' % (ini%256, fin%256, (ini+fin)%256)
			self.diagrama.edge(str(ini),str(fin),color=rgb)
		self.diagrama.view()