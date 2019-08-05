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
			if sys.argv[1]=="-em":
				if (len(sys.argv)==6):
					try:
						num = int(sys.argv[5])
						esterilizar.esterilizar()
					except ValueError:
						menu.ayudaesterilizar()
				else:
					menu.ayudaesterilizar()
			if (sys.argv[1]=="-oi"):
				if (len(sys.argv)==4):
					imagen.obtenerImagen()
				else:
					menu.ayudaObtenerImagen()
			if sys.argv[1]=="-mi":
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
				if (len(sys.argv)==3):
					hashBusqueda.obtenerHash()
				else:
					menu.ayudaObtenerHash()
			if sys.argv[1]=="-ch":
				if (len(sys.argv)==4):
					hashBusqueda.compararHash()	
				else:
					menu.ayudaCompararHash()
			if sys.argv[1]=="-ba":
				if (len(sys.argv)==6):
					print("TODO")	
				else:
					menu.ayudaBuscarArchivos()
			if sys.argv[1]=="-bc":
				if (len(sys.argv)==4):
					hashBusqueda.buscarCadenas()	
				else:
					menu.ayudaBuscarCadenas()
			if sys.argv[1]=="-ra":
				if (len(sys.argv)==5):
					carving.carvingFile(sys.argv)
				else:
					menu.ayudaRecuperarArchivos()
			if sys.argv[1]=="-raa":
				if (len(sys.argv)==4):
					carving.carvingAll(sys.argv)
				else:
					menu.ayudaRecuperarArchivos()
			if sys.argv[1]=="-at":
				if (len(sys.argv)==3):
					analisisTrafico.analisisTrafico()		
				else:
					menu.ayudaAnalisisTrafico()
			if sys.argv[1]=="-ai":
				if (len(sys.argv)==3):
					virus.analizar()
				else:
					menu.ayudaAnalisisInfectados()
			if sys.argv[1]=="-air":
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
				if (len(sys.argv)==3):
					cadena_custodia.cadenaCustodia(sys.argv[2])	
				else:
					menu.ayudaDiligenicarCadena()
			if sys.argv[1]=="-dcv":
				if (len(sys.argv)==3):
					cadena_custodia.cadenaCustodiaVacia(sys.argv[2])	
				else:
					menu.ayudaDiligenicarCadena()
