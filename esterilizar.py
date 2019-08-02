#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
def esterilizar():	
	insInicial=time.time()
	vuelta=0
	print("====running the process for disinfecting hard disks====")
	while vuelta<int(sys.argv[5]):
		porcentaje=vuelta+1
		print("==========Completed "+str(porcentaje)+"/"+sys.argv[5])
		ValorIF="if=/dev/zero"
		ValorOF=" of="+sys.argv[2]
		ValorBS=" bs="+sys.argv[3]
		ComandoDDZERO="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDZERO)
		ValorIF="if=/dev/urandom"
		ComandoDDRANDOM="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDRANDOM)
		ValorIF="if=/dev/zero"
		ComandoDDZERO="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDZERO)
		vuelta=vuelta+1
	print("====End of the disinfection process of hard disks====")
	print("")
	print("======checking the disinfection with grep command=====")
	CoGrep="dd if="+sys.argv[2]+" | xxd | grep -v "+"'0000 0000 0000 0000 0000 0000 0000 0000'"
	os.system(CoGrep)
	formatear()
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)

def formatear():
	print("====Formatting====")
	UNMOUNT="umount "+sys.argv[2]
	os.system(UNMOUNT)
	FORMATEAR="sudo mkfs.vfat -F 32 -n "+sys.argv[4]+" "+sys.argv[2]
	os.system(FORMATEAR)
	print("====End...====")
