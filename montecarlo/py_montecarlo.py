# Autor: Sebastian Andres Ruiz Garcia
# Fecha: 20-11-2022
# Tema : metodo montecarlo para estimar el valor de pi

import random

def montecarlo(rand_x,rand_y, intervalo):
	puntosCir  = 0
	puntosCuad = 0
	
	for i in range (intervalo**2):
	
		distanciaOrigen = (rand_x**2 + rand_y**2)**0.5

		if distanciaOrigen<=1:
			puntosCir+=1
		puntosCuad+=1
		pi = 4* puntosCir/puntosCuad
	

