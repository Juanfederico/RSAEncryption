import math
import sys
import os
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
	#print(int(codigo**d))
	#print("Cifras del codigo encriptado elevado a la clave privada: " + str(len(str(codigo**d))))
	return int(((codigo**d) % n)) #El ** es para elevar a la potencia pero con precision exacta, a diferencia de math.pow

def encriptarString(mensaje, e, n): #Devuelve un array de longitud igual a la del string, pero encriptado con los enteros que correspondan a cada letra
	mensajeEncriptado = []
	for caracter in mensaje:
		#print("El caracter es: " +str(caracter))
		if(caracter.upper()=='A'): mensajeEncriptado.append(encriptarMensaje(677, e, n))
		elif(caracter.upper()=='B'): mensajeEncriptado.append(encriptarMensaje(578, e, n))
		elif(caracter.upper()=='C'): mensajeEncriptado.append(encriptarMensaje(670, e, n))
		elif(caracter.upper()=='D'): mensajeEncriptado.append(encriptarMensaje(200, e, n))
		elif(caracter.upper()=='E'): mensajeEncriptado.append(encriptarMensaje(55, e, n))
		elif(caracter.upper()=='F'): mensajeEncriptado.append(encriptarMensaje(79, e, n))
		elif(caracter.upper()=='G'): mensajeEncriptado.append(encriptarMensaje(44, e, n))
		elif(caracter.upper()=='H'): mensajeEncriptado.append(encriptarMensaje(88, e, n))
		elif(caracter.upper()=='I'): mensajeEncriptado.append(encriptarMensaje(99, e, n))
		elif(caracter.upper()=='J'): mensajeEncriptado.append(encriptarMensaje(111, e, n))
		elif(caracter.upper()=='K'): mensajeEncriptado.append(encriptarMensaje(222, e, n))
		elif(caracter.upper()=='L'): mensajeEncriptado.append(encriptarMensaje(333, e, n))
		elif(caracter.upper()=='M'): mensajeEncriptado.append(encriptarMensaje(444, e, n))
		elif(caracter.upper()=='N'): mensajeEncriptado.append(encriptarMensaje(555, e, n))
		elif(caracter.upper()=='O'): mensajeEncriptado.append(encriptarMensaje(666, e, n))
		elif(caracter.upper()=='P'): mensajeEncriptado.append(encriptarMensaje(777, e, n))
		elif(caracter.upper()=='Q'): mensajeEncriptado.append(encriptarMensaje(888, e, n))
		elif(caracter.upper()=='R'): mensajeEncriptado.append(encriptarMensaje(999, e, n))
		elif(caracter.upper()=='S'): mensajeEncriptado.append(encriptarMensaje(123, e, n))
		elif(caracter.upper()=='T'): mensajeEncriptado.append(encriptarMensaje(456, e, n))
		elif(caracter.upper()=='U'): mensajeEncriptado.append(encriptarMensaje(789, e, n))
		elif(caracter.upper()=='V'): mensajeEncriptado.append(encriptarMensaje(234, e, n))
		elif(caracter.upper()=='W'): mensajeEncriptado.append(encriptarMensaje(345, e, n))
		elif(caracter.upper()=='X'): mensajeEncriptado.append(encriptarMensaje(456, e, n))
		elif(caracter.upper()=='Y'): mensajeEncriptado.append(encriptarMensaje(567, e, n))
		elif(caracter.upper()=='Z'): mensajeEncriptado.append(encriptarMensaje(961, e, n))
	return mensajeEncriptado

def desencriptarString(mensaje, d, n):
	mensajeDesencriptado = []
	for numeroEncriptado in mensaje:
		numero = desencriptarMensaje(numeroEncriptado, d, n)
		if(numero==677): mensajeDesencriptado.append('A')
		elif(numero==578): mensajeDesencriptado.append('B')
		elif(numero==670): mensajeDesencriptado.append('C')
		elif(numero==200): mensajeDesencriptado.append('D')
		elif(numero==55): mensajeDesencriptado.append('E')
		elif(numero==79): mensajeDesencriptado.append('F')
		elif(numero==44): mensajeDesencriptado.append('G')
		elif(numero==88): mensajeDesencriptado.append('H')
		elif(numero==99): mensajeDesencriptado.append('I')
		elif(numero==111): mensajeDesencriptado.append('J')
		elif(numero==222): mensajeDesencriptado.append('K')
		elif(numero==333): mensajeDesencriptado.append('L')
		elif(numero==444): mensajeDesencriptado.append('M')
		elif(numero==555): mensajeDesencriptado.append('N')
		elif(numero==666): mensajeDesencriptado.append('O')
		elif(numero==777): mensajeDesencriptado.append('P')
		elif(numero==888): mensajeDesencriptado.append('Q')
		elif(numero==999): mensajeDesencriptado.append('R')
		elif(numero==123): mensajeDesencriptado.append('S')
		elif(numero==456): mensajeDesencriptado.append('T')
		elif(numero==789): mensajeDesencriptado.append('U')
		elif(numero==234): mensajeDesencriptado.append('V')
		elif(numero==345): mensajeDesencriptado.append('W')
		elif(numero==456): mensajeDesencriptado.append('X')
		elif(numero==567): mensajeDesencriptado.append('Y')
		elif(numero==961): mensajeDesencriptado.append('Z')
	return mensajeDesencriptado



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

#Datos que se usaran para encriptar

print("Datos de entrada: ")
print("Numero primo p: " + str(p))
print("Numero primo q: " + str(q))
print("Numero n (producto de p y q): " + str(n))
print("Funcion Fi de Euler generada con esos numeros: " + str(fi_n))
print("-----------------------------------------------------------")
print("Exponente publico: " + str(e))
print("Exponente privado: " + str(d))
print("Es decir, la clave publica queda establecida como: (" +str(n)+", "+str(e)+")")
print("Y la clave privada queda establecida como: (" +str(n)+", "+str(d)+")")

os.system('pause')
os.system('cls')

#Empezando la encriptacion

print("Escriba un mensaje para ser encriptado:")
mensaje=input() #Mensaje de la A a la Z
mensajeEncriptado=encriptarString(mensaje, e, n) #Envio el mensaje, el exponente publico y el n
print("Encriptamos el mensaje y da lo siguiente: " +str(mensajeEncriptado))

print("Ahora vamos a desencriptar el mensaje escrito anteriormente:")
os.system('pause')

mensajeDesencriptado=desencriptarString(mensajeEncriptado, d, n) #Envio el mensaje encriptado y la clave privada
print("Desencriptamos el mensaje y da lo siguiente: " +str(mensajeDesencriptado))