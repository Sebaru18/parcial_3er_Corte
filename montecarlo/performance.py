import time
import cy_montecarlo
import py_montecarlo
import random

formato_datos = "{:.5f},{:5f}\n"


intervalo = random.randint(100,10000)
for i in range(30):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	
	print("Intervalo: ", intervalo)
	
	iniciopy = time.time()
	print("python: ")
	py_montecarlo.montecarlo(x,y, intervalo)
	finalpy = time.time() - iniciopy
	print("tiempo de ejecucion: ",finalpy)


	iniciocy = time.time()
	print("cython: ")
	cy_montecarlo.montecarlo(x,y,intervalo)
	finalycy = time.time()  - iniciocy
	print("tiempo de ejecucion: ",finalycy)
		
	with open("datosEjercicio2.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy, finalycy))
