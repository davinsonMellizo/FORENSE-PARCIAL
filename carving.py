#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys 
import subprocess
import time

def install():
	try:
		subprocess.check_output('which -a foremost',shell=True)
	except :
		print("Instalando complemento foremost")
		os.system('apt-get install foremost')
		print("\n")

def carvingAll(argv):
	try:
		install()
		subprocess.check_output('which -a foremost',shell=True)
		insInicial=time.time()
		print("\nProceso de recuperacion iniciado .....")
		subprocess.check_output('foremost -t all -i '+argv[2]+' -o '+argv[3],shell=True)
		insFinal=time.time()
		tiempo=insFinal- insInicial
		print("Recuperacion finalizada resultados en: "+argv[3])
		print("Tiempo de Ejecucion", tiempo)
	except :
		print("error al ejecutar el comando, favor de revisar la documentación")

def carvingFile(argv):
	try:
		install()
		subprocess.check_output('which -a foremost',shell=True)
		insInicial=time.time()
		print("\nProceso de recuperacion iniciado .....")
		subprocess.check_output('foremost -t '+argv[2]+' -i '+argv[3]+' -o '+argv[4],shell=True)
		insFinal=time.time()
		tiempo=insFinal- insInicial
		print("Recuperacion finalizada resultados en: "+argv[4])
		print("Tiempo de Ejecucion", tiempo)
	except :
		print("error al ejecutar el comando, favor de revisar la documentación")