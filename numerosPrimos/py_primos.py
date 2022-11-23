# Autor: Sebastian Andres Ruiz Garcia
# Fecha: 20-11-2022
# Tema : Encontrar números primos

def primes(nb_primes):
	p = []
	n = 2
	while len(p) < nb_primes:
        
		for i in p:
			if n % i == 0:
				break

        
		else:
			p.append(n)
		n += 1
	return p
	
	
	
	
