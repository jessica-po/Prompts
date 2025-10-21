#~ # MAGIC CODEFORCES PYTHON FAST IO
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
#~ # END OF MAGIC CODEFORCES PYTHON FAST IO

class Arista():
	def __init__(self,salida,llegada,capacidad,flujo,costo,indice):
		self.salida = salida
		self.llegada = llegada
		self.capacidad = capacidad
		self.flujo = flujo
		self.costo = costo
		self.indice = indice
		
	def __str__(self):
		s = ""
		s = s + "salida =" + str(self.salida) + "\n"
		s = s + "llegada =" + str(self.llegada) + "\n"
		s = s + "capacidad =" + str(self.capacidad) + "\n"
		s = s + "flujo =" + str(self.flujo) + "\n"
		s = s + "costo =" + str(self.costo) + "\n"
		s = s + "indice =" + str(self.indice) + "\n"
		s = s + "------------"
		return s
		
		
class Red(): 
	## Representacion de una Red de flujo ##
	def __init__(self,s,t): # Crea una red vacio
		self.lista_aristas = []
		self.lista_adyacencia = {}
		self.vertices = set()
		self.fuente = s
		self.sumidero = t
		
	def agregar_vertice(self,vertice):
		self.vertices.add(vertice)
		
	def agregar_arista(self,arista): 
		self.vertices.add(arista.salida)
		self.vertices.add(arista.llegada)
		self.lista_aristas.append(arista)
		if arista.salida not in self.lista_adyacencia:
			self.lista_adyacencia[arista.salida] = set()
		self.lista_adyacencia[arista.salida].add(arista.indice)
			
	def agregar_lista_aristas(self,lista_aristas):
		for arista in lista_aristas:
			self.agregar_arista(arista)
			
	def cantidad_de_vertices(self):
		return len(self.vertices)
	
	def vecinos(self,vertice):
		if vertice not in self.lista_adyacencia:
			return set()
		else:
			return self.lista_adyacencia[vertice]
	
	def buscar_valor_critico(self,padre):
		INFINITO = 1000000000
		valor_critico = INFINITO
		actual = self.sumidero
		while actual != self.fuente:
			arista_camino = self.lista_aristas[padre[actual]]
			valor_critico = min(valor_critico,arista_camino.capacidad - arista_camino.flujo)
			actual = arista_camino.salida
		return valor_critico
	
	def actualizar_camino(self,padre,valor_critico):
		actual = self.sumidero
		costo_actual = 0
		while actual != self.fuente:
			self.lista_aristas[padre[actual]].flujo += valor_critico
			self.lista_aristas[padre[actual]^1].flujo -= valor_critico
			costo_actual += valor_critico*self.lista_aristas[padre[actual]].costo
			actual = self.lista_aristas[padre[actual]].salida
		return costo_actual,True	
		
	def camino_de_aumento(self):
		INFINITO = 1000000000
		distancia = {v:INFINITO for v in self.vertices}
		padre = {v:-1 for v in self.vertices}
		distancia[self.fuente] = 0
		#~ for iteracion in range(len(self.vertices)-1):
			#~ for arista in self.lista_aristas:
				#~ if arista.flujo < arista.capacidad and distancia[arista.salida] + arista.costo < distancia[arista.llegada]:
					#~ distancia[arista.llegada] = distancia[arista.salida] + arista.costo
					#~ padre[arista.llegada] = arista.indice
		capa_actual,capa_nueva = set([self.fuente]),set()
		while capa_actual:
			for v in capa_actual:
				for arista_indice in self.vecinos(v):
					arista = self.lista_aristas[arista_indice]
					if arista.flujo < arista.capacidad and distancia[arista.salida] + arista.costo < distancia[arista.llegada]: 
						distancia[arista.llegada] = distancia[arista.salida] + arista.costo
						padre[arista.llegada] = arista.indice
						capa_nueva.add(arista.llegada)
			capa_actual = set()
			capa_actual,capa_nueva = capa_nueva,capa_actual
				
		if distancia[self.sumidero] < INFINITO:
			valor_critico = self.buscar_valor_critico(padre)
			costo_actual,hay_camino = self.actualizar_camino(padre,valor_critico)
			return valor_critico,costo_actual,hay_camino
		else:
			return -1,-1,False
			
			
	def max_flow_min_cost(self):
		flujo_total = 0
		costo_total = 0
		hay_camino = True
		while hay_camino:
			#~ for x in self.lista_aristas:
				#~ print(x)
			
			flujo_actual,costo_actual,hay_camino = self.camino_de_aumento()
			if hay_camino:
				flujo_total += flujo_actual
				costo_total += costo_actual
		return flujo_total,costo_total
		
	
INFINITO = 10000000000000	
n,q = list(map(int,input().split()))
maxi = [n for i in range(n)]
mini = [1 for i in range(n)]
R = Red(0,2*n+1)
prohibidos = {i:set() for i in range(n)}
for i in range(n):
	for k in range(n+1):
		R.agregar_arista(Arista(R.fuente,i+1,1,0,2*k+1,len(R.lista_aristas)))
		R.agregar_arista(Arista(i+1,R.fuente,0,0,-2*k-1,len(R.lista_aristas)))

for j in range(n):
	R.agregar_arista(Arista(n+j+1,R.sumidero,1,0,0,len(R.lista_aristas)))
	R.agregar_arista(Arista(R.sumidero,n+j+1,0,0,0,len(R.lista_aristas)))

for z in range(q):
	t,l,r,v = list(map(int,input().split()))
	if t == 1:
		for i in range(v-1):
			for j in range(l,r+1):
				prohibidos[i].add(j)
	else:
		for i in range(v,n):
			for j in range(l,r+1):
				prohibidos[i].add(j)
		
		

for i in range(n):
	for j in range(mini[i],maxi[i]+1):
		if j not in prohibidos[i]:
			R.agregar_arista(Arista(i+1,n+j,1,0,0,len(R.lista_aristas)))
			R.agregar_arista(Arista(n+j,i+1,0,0,0,len(R.lista_aristas)))		
		
flujo_total,costo_total = R.max_flow_min_cost()
#~ print(flujo_total,costo_total)
if flujo_total < n:
	print("-1")
else:
	print(costo_total)