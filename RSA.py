import math
import sys
from decimal import Decimal

#Funciones
def modNumeroGrande(numero, mod):
	multiplicadorMax = math.floor(numero//mod) #Para volver al anterior
	#print(numero - multiplicadorMax*mod)
	#print(multiplicadorMax)
	return numero - multiplicadorMax*mod


#Cantidad de coprimos entre 1 y un numero expresado como factor de dos numeros primos
def calcularFiEulerFactores(numA, numB):
	return (numA-1)*(numB-1)

def calcularExponentePrivado(e, fi_n):
	multiplicador = 1
	d=1
	while(d % e != 0):
		d=fi_n*multiplicador + 1
		multiplicador+=1
	return d//e

def encriptarMensaje(mensaje, e, n):
	#print(len(str(mensaje**e)))
	#print(mensaje**e)
	return int(((mensaje**e) % n)) #El ** es para elevar a la potencia pero con precision exacta, a diferencia de math.pow

def desencriptarMensaje(codigo, d, n):
	print(int(codigo**d))
	print("Cifras del codigo encriptado elevado a la clave privada: " + str(len(str(codigo**d))))
	return int(((codigo**d) % n)) #El ** es para elevar a la potencia pero con precision exacta, a diferencia de math.pow





#Se eligen dos numeros primos relativamente chicos
p = 89
q = 97
#Se calcula el producto de los dos numeros primos
n = p*q
#Se calcula el valor fi de euler para el numero n (como ya tenemos los factores primos, los utilizamos)
fi_n = calcularFiEulerFactores(p, q)

print("Determine el exponente publico (debe ser un numero primo menor a n)")
e = int(input()) #Exponente publico, se usa raw_input para python 2.x

d = int(calcularExponentePrivado(e, fi_n)) #Exponente privado, calculado por fuerza bruta

print("Exponente publico: " + str(e))
print("Exponente privado: " + str(d))
print("Es decir, la clave publica queda establecida como: (" +str(n)+", "+str(e)+")")
print("Y la clave privada queda establecida como: (" +str(n)+", "+str(d)+")")

print("Escriba un mensaje numerico para ser encriptado:")
mensaje=int(input())

mensajeEncriptado=encriptarMensaje(mensaje, e, n) #Envio el mensaje, el exponente publico y el n
print("Encriptamos el mensaje y da lo siguiente: " +str(mensajeEncriptado))

mensajeDesencriptado=desencriptarMensaje(mensajeEncriptado, d, n) #Envio el mensaje encriptado y la clave privada
print("Desencriptamos el mensaje y da lo siguiente: " +str(mensajeDesencriptado))

