#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
def obtenerHash():
	insInicial=time.time()
	print("Procesando...")
	ComandoHash="md5sum "+sys.argv[2]
	print("HASH:")
	os.system(ComandoHash)
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def compararHash():
	insInicial=time.time()
	print("Procesando...")
	f = open (sys.argv[3],'r')
	hashVerificacion = f.read()
	hashVerificacion=hashVerificacion.rstrip('\n')
	f.close()
	ComandoHash="md5sum "+sys.argv[2]+">result.txt"
	os.system(ComandoHash)
	f = open ("result.txt",'r')
	hashObtenido = f.read()
	f.close()
	hashObtenido=hashObtenido.split(" ")[0].rstrip('\n')
	print("HASH verificación:"+hashVerificacion)
	print("HASH obtenido    :"+hashObtenido.rstrip('\n'))
	if(hashObtenido==hashVerificacion):
		print("!!!IGUALES!!!")
	else:
		print("!!!DIFIERENTES!!!")
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def buscarCadenas():
	insInicial=time.time()
	print("Procesando...")
	crearArchivo()
	archivo = open(sys.argv[2], "r")
	for linea in archivo.readlines():
		ComandoGrep="grep -ir "+"'"+linea.rstrip('\n')+"' "+sys.argv[3]+">resultaux.txt"
		os.system(ComandoGrep)
		comandoCAT="cat resultaux.txt >> result.txt"
		os.system(comandoCAT)
	archivo.close()
	insFinal=time.time()
	tiempo=insFinal-insInicial
	print("Resultado en result.txt")
	print("Tiempo de Ejecucion", tiempo)

def buscarCadenasRe(carpeta):
	insInicial=time.time()
	print("Procesando...")
	crearArchivo()
	archivos=carpetas=0
	for i in os.listdir(carpeta):
		if os.path.isfile(os.path.join(carpeta,i)):
			archivo = open(sys.argv[2], "r")
			for linea in archivo.readlines():
				ComandoGrep="grep -ir "+"'"+linea.rstrip('\n')+"' "+os.path.join(carpeta,i)+">resultaux.txt"
				os.system(ComandoGrep)
				comandoCAT="cat resultaux.txt >> result.txt"
				os.system(comandoCAT)
			archivo.close()
		if os.path.isdir(os.path.join(carpeta,i)):
			carpetas+=1
	for i in os.listdir(carpeta):
		if os.path.isdir(os.path.join(carpeta,i)):
			analizarRe(os.path.join(carpeta,i))
	insFinal=time.time()
	tiempo=insFinal-insInicial
	print("Resultado en result.txt")
	print("Tiempo de Ejecucion", tiempo)	

def buscarArchivos():
	insInicial=time.time()
	print("Procesando...")
	crearArchivo()
	archivo = open(sys.argv[3], "r")
	for linea in archivo.readlines():
		ComandoGrep="find "+sys.argv[2]+" -iname "+linea.rstrip('\n')+">resultaux.txt"
		os.system(ComandoGrep)
		comandoCAT="cat resultaux.txt >> result.txt"
		os.system(comandoCAT)
		
	archivo.close()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Resultado en result.txt")
	print("Tiempo de Ejecucion", tiempo)	
	
def crearArchivo():
	os.system("rm result.txt")
	f = open ("result.txt",'w')
	f.close()

def hashRe(carpeta):
	
	insInicial=time.time()
	print("Procesando...")
		
	archivos=carpetas=0
	for i in os.listdir(carpeta):
		if os.path.isfile(os.path.join(carpeta,i)):
			ComandoHash="md5sum "+os.path.join(carpeta,i)
			print("================================================================================")
			print("HASH de "+i+" : ")
			os.system(ComandoHash)
		if os.path.isdir(os.path.join(carpeta,i)):
			carpetas+=1
	for i in os.listdir(carpeta):
		if os.path.isdir(os.path.join(carpeta,i)):
			analizarRe(os.path.join(carpeta,i))
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
