import time
import py_primos
import cy_primos
import random

formato_datos = "{:.5f},{:5f}\n"

nPrimos = random.randint(2,10000)

for i in range(30):

	iniciopy = time.time()
	print("python: ")
	py_primos.primes(nPrimos)
	finalpy = time.time() - iniciopy



	iniciocy = time.time()
	print("cython: ")
	cy_primos.primes(nPrimos)
	finalycy = time.time()  - iniciocy
	
	with open("datos.csv","a") as archivo:
		archivo.write(formato_datos.format(finalpy, finalycy))
