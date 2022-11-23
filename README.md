# parcial_3er_Corte

## Autor: Sebastian Andres Ruiz Garcia

Se realizará una medida de rendimiento entre las ejecuciones de dos programas, estos para comparar los tiempos de ejecución de los programas tanto en Python como en Cython y con esto analizar los datos y observar que lenguaje de programación es más eficaz en términos de rendimiento.


Ahora, en el siguiente repositorio se podrá encontrar, dos carpetas, uno seria Montecarlo, el cual contiene los ficheros .py, .pyx, y el .csv del programa de Montecarlo, el cual se encarga de estimar el valor de pi,  ahora, la otra carpeta, llamada números primos, contiene igualmente sus ficheros correspondientes, pero estos se encargan de encontrar los números primarios dependiendo del valor que se seleccione, este valor es aleatorio.


Para poder ejecutar estos programas, es necesario tener un archivo llamado setup.py el cual convierte un archivo Python a un archivo Cython, y para tomar las medidas de rendimientos, tenemos un fichero llamado performance.py, el cual importa los dos programas, el de Python y Cython, para poder tomar el tiempo de ejecución de cada uno, ahora, para tomar una medida relevante se realizan 30 ejecuciones por programa, y este se encarga de crear un archivo .csv y guardar los datos ahí-


Para analizar los datos se usó un cuaderno, el cual se llama Parcial3.ipynb, este tiene dos secciones, el primero ejercicio1, el cual se trae los datos .csv guardados del programa de los números primos, y se realiza un análisis sacando el promedio, y generando tablas. Así mismo mas abajo se encuentra el apartado ejercicio2, que toma los datos .csv del ejercicio de Montecarlo, y al igual modo se analizan comparando el promedio y con gráficas, ahí mismo se encuentra la conclusión de cada problema.


La ejecución de este seria, en cada archivo tener un Makefile, así como un setup.py y un performance.py, en Linux (Ubuntu), se realiza el make all, para que cree todos los archivos necesarios, y luego se realiza el siguiente comando: python3 performance.py, con esto ya creara el archivo .csv con los tiempos guardados.
