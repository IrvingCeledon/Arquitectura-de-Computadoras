Este proyecto final consta de 2 partes:
  - Decodificador de instrucciones MIPS 32 (tipo R, I y J) a binario.
  - MIPS pipeline con sus 5 etapas clásicas.

La primera parte cuenta con una estructura modulada, y una interfaz gráfica; todo hecho con el lenguaje de programación de Python.

Por otro lado, el pipeline fue diseñado y simulado en ModelSim; con el lenguage de Verilog.

La relación entre estas dos partes del proyecto, se encuentra en como el decodificador recibe un conjunto de instrucciones que emulan el algortimo de Bubble Sort, para transformarlo en binario en un formato Big Endian de 8 bits. Esto para que el pipeline, pueda interpretar las instrucciones y llevar a cabo el algoritmo.
