#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
def analisisTrafico():
	crearArchivo()
	insInicial=time.time()
	print("Procesando...")
	ComandoTshark="tshark -r "+sys.argv[2]+" -Y urlencoded-form -w salida"
	os.system(ComandoTshark)
	comandoLess="less salida>result.txt"
	os.system(comandoLess)
	archivo = open("result.txt", "r")
	for linea in archivo.readlines():
		lineasplit=linea.split("=")
		if (lineasplit[0]=="user"):
			user=lineasplit[1].split("&")[0]
			password=lineasplit[2].split("&")[0]
			print("User: "+user+"  Password: "+password)
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)

def crearArchivo():
	os.system("rm result.txt")
	f = open ("result.txt",'w')
	f.close()
