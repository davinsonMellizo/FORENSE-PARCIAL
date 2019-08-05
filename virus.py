#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from hashlib import md5
from virus_total_apis import PublicApi
import time
def analizar():
	insInicial=time.time()
	print("Procesando...")
	API_KEY = "a9089095456a6c812626239b837c894abcea66938853813118ebf16a5fff1690"
	api = PublicApi(API_KEY)
	with open(sys.argv[2], "rb") as f:
		file_hash = md5(f.read()).hexdigest()
	response = api.get_file_report(file_hash)
	if response["response_code"] == 200:
		try:
			if response["results"]["positives"] > 0:
				print("Archivo malicioso.")
			else:
				print("Archivo seguro.")
		except:
			print("No ha podido obtenerse el análisis del archivo.")
	else:
		print("No ha podido obtenerse el análisis del archivo.")
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)

def analizarRe(carpeta):
	API_KEY = "a9089095456a6c812626239b837c894abcea66938853813118ebf16a5fff1690"
	api = PublicApi(API_KEY)

	archivos=carpetas=0
	for i in os.listdir(carpeta):
		if os.path.isfile(os.path.join(carpeta,i)):
			print(i+": ")
			with open(os.path.join(carpeta,i), "rb") as f:
				file_hash = md5(f.read()).hexdigest()
			response = api.get_file_report(file_hash)
			if response["response_code"] == 200:
				try:
					if response["results"]["positives"] > 0:
						print("Archivo malicioso.")
					else:
						print("Archivo seguro.")
				except:
					print("No ha podido obtenerse el análisis del archivo.")
			else:
				print("No ha podido obtenerse el análisis del archivo.")
			print("==================================================")
		if os.path.isdir(os.path.join(carpeta,i)):
			carpetas+=1
	for i in os.listdir(carpeta):
		if os.path.isdir(os.path.join(carpeta,i)):
			analizarRe(os.path.join(carpeta,i))
	