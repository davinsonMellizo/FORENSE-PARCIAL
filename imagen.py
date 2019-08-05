#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
def obtenerImagen():
	insInicial=time.time()
	print("Procesando...")
	comandoDD="dd if="+sys.argv[2]+" of="+sys.argv[3]
	os.system(comandoDD)
	print("HASH: ")
	comandoMD5imagen="md5sum "+sys.argv[3]
	os.system(comandoMD5imagen)
	print("HASH: ")
	comandoMD5disco="md5sum "+sys.argv[2]
	os.system(comandoMD5disco)
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def montarimagen():
	insInicial=time.time()
	print("Procesando...")
	comandoMount="mount -o ro,loop "+sys.argv[2] +" "+sys.argv[3]+">result.txt"
	os.system(comandoMount)
	f = open ("result.txt",'r')
	result = f.read()
	f.close()
	if(result!=""):
		print("No se ha podido montar la imagen, Utilice fdisk -l para obetener sector de inicio")
		print("Luego, Ejecute: python main.py -mi NombreImagen PointMount start")
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def montarimagenOffSet():
	insInicial=time.time()
	print("Procesando...")
	offset=int(sys.argv[4])*512
	comandoMount="mount -o ro,loop,offset="+str(offset)+" "+sys.argv[2] +" "+sys.argv[3]+">result.txt"
	os.system(comandoMount)
	f = open ("result.txt",'r')
	result = f.read()
	f.close()
	if(result!=""):
		print("No se ha podido montar la imagen, Utilice fdisk -l para obetener sector de inicio")
		print("Luego, Ejecute: python main.py -mi NombreImagen PointMount start")
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
	
