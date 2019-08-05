#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	import os
	import sys
	from hashlib import md5
	import menu
	import esterilizar
	import virus
	import hashBusqueda
	import imagen
	import time
	import cadena_custodia
	import analisisTrafico
	import carving
except :
	menu.ayudaMenu()
	
if __name__ == "__main__":
	if len(sys.argv)==1:
		menu.algoritmos()
	else:
		if(len(sys.argv)>1):
			mostrarmenu=0
			if sys.argv[1]=="-em":
				mostrarmenu=1
				if (len(sys.argv)==6):
					try:
						num = int(sys.argv[5])
						esterilizar.esterilizar()
					except ValueError:
						menu.ayudaesterilizar()
				else:
					menu.ayudaesterilizar()
			if (sys.argv[1]=="-oi"):
				mostrarmenu=1
				if (len(sys.argv)==4):
					imagen.obtenerImagen()
				else:
					menu.ayudaObtenerImagen()
			if sys.argv[1]=="-mi":
				mostrarmenu=1
				if (len(sys.argv)==5):
					try:
						num = int(sys.argv[4])
						imagen.montarimagenOffSet()	
					except ValueError:
						menu.ayudaMontarImagen()
				else:
					if (len(sys.argv)==4):
						imagen.montarimagen()		
					else:
						menu.ayudaMontarImagen()
			if sys.argv[1]=="-oh":
				mostrarmenu=1
				if (len(sys.argv)==3):
					hashBusqueda.obtenerHash()
				else:
					menu.ayudaObtenerHash()
			if sys.argv[1]=="-ohr":
				mostrarmenu=1
				if (len(sys.argv)==3):
					hashBusqueda.hashRe(sys.argv[2])
				else:
					menu.ayudaObtenerHash()
			if sys.argv[1]=="-ch":
				mostrarmenu=1
				if (len(sys.argv)==4):
					hashBusqueda.compararHash()	
				else:
					menu.ayudaCompararHash()
			if sys.argv[1]=="-ba":
				mostrarmenu=1
				if (len(sys.argv)==4):
					hashBusqueda.buscarArchivos()	
				else:
					menu.ayudaBuscarArchivos()
			if sys.argv[1]=="-bc":
				mostrarmenu=1
				if (len(sys.argv)==4):
					hashBusqueda.buscarCadenas()	
				else:
					menu.ayudaBuscarCadenas()
			if sys.argv[1]=="-bcr":
				mostrarmenu=1
				if (len(sys.argv)==4):
					hashBusqueda.buscarCadenasRe(sys.argv[3])	
				else:
					menu.ayudaBuscarCadenas()
			if sys.argv[1]=="-ra":
				mostrarmenu=1
				if (len(sys.argv)==5):
					carving.carvingFile(sys.argv)
				else:
					menu.ayudaRecuperarArchivos()
			if sys.argv[1]=="-raa":
				mostrarmenu=1
				if (len(sys.argv)==4):
					carving.carvingAll(sys.argv)
				else:
					menu.ayudaRecuperarArchivos()
			if sys.argv[1]=="-at":
				mostrarmenu=1
				if (len(sys.argv)==3):
					analisisTrafico.analisisTrafico()		
				else:
					menu.ayudaAnalisisTrafico()
			if sys.argv[1]=="-ai":
				mostrarmenu=1
				if (len(sys.argv)==3):
					virus.analizar()
				else:
					menu.ayudaAnalisisInfectados()
			if sys.argv[1]=="-air":
				mostrarmenu=1
				if (len(sys.argv)==3):
					insInicial=time.time()
					print("Procesando...")
					virus.analizarRe(sys.argv[2])
					insFinal=time.time()
					tiempo=insFinal- insInicial
					print("Tiempo de Ejecucion", tiempo)
				else:
					menu.ayudaAnalisisInfectados()
			if sys.argv[1]=="-dc":
				mostrarmenu=1
				if (len(sys.argv)==3):
					cadena_custodia.cadenaCustodia(sys.argv[2])	
				else:
					menu.ayudaDiligenicarCadena()
			if sys.argv[1]=="-dcv":
				mostrarmenu=1
				if (len(sys.argv)==3):
					cadena_custodia.cadenaCustodiaVacia(sys.argv[2])	
				else:
					menu.ayudaDiligenicarCadena()
			if (mostrarmenu==0):
				menu.algoritmos()
