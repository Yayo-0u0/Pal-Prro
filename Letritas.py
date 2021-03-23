# Pal-Prro
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m


def Nueva_entrada(nombre):
	LetraA = cv.imread(nombre)
	LetraA = cv.cvtColor(LetraA,cv.COLOR_RGB2GRAY) #De COLOR a B/N
	print(LetraA)
	vector_ent=Convertir(LetraA,1)
	print(vector_ent)
	return vector_ent

def matriz_de_peso(matriz):
	M,N=np.shape(matriz)
	Peso=np.zeros((N,N),dtype=np.longdouble)
	for j in range(N):
		for i in range(N):
			if i!=j:
				for k in range(M):
					Peso[j][i]+=np.longdouble(matriz[k][j]*matriz[k][i])
	Peso=Peso/N
	print("\nMatriz de Peso:\n\n {}".format(Peso))
	return Peso

def calculo(matriz,MP,Peso):
	y,x=np.shape(MP)
	for j in range(y):
		U=np.zeros(x,int)
		ban=1
		for i in range(x):
			U[i]=MP[j][i]
			if U[i]<0: ban=-1
		print("\nCalculando convergencia con el vector C{}".format(j+1))
		convergencia(U,Peso,ban,matriz)

	
def convergencia(Entrada,Peso,ban,matriz):
	print("\n X={}\n Estado inicial U(0)={}\n".format(Entrada,Entrada))
	con=0
	time=0
	Y0=funcion_de_transferencia(Entrada,ban)
	while con==0:
		if time==0: 
			print("Aplicando funcion de tranferencia Y({})=fh(U({}))={}\n".format(time,time,Y0))
			letra=Convertir(Y0,2)
		else:
			print("Y({})={}\n".format(time,Y0))
			letra=Convertir(Y0,2)
		print("U({})=WY^T({})=\n {} {}^T".format(time+1,time,Peso,Y0))
		U1=multiplicacion(Peso,Y0)
		print("\n U({})={}".format(time+1,U1))
		Y1=funcion_de_transferencia(U1,ban)
		print("\n Y({})=fh(U({}))={}".format(time+1,time+1,Y1))
		letra=Convertir(Y1,2)
		print(letra)
		con=Compara(Y0,Y1)
		if con==0:
			print("\nY({})!=Y({})... No converge {} Iteracion\n\n".format(time,time+1,time+1))
			Y0=Y1
			time+=1
		else:
			if ban==-1:
				print("\nY({})==Y({})... Converge".format(time,time+1))
				Asocia(matriz,Y1)
			elif ban==1:
				print("\nY({})==Y({})... Converge y se acocia con C1".format(time,time+1))

			con=1

def Asocia(matriz,Y):
	j,i=np.shape(matriz)
	for y in range(j):
		val=0
		for x in range(i):
			if Y[x]!=matriz[y][x]:
			 val=1
		if val==0: print("Se asocia con C{}".format(y+1))

def funcion_de_transferencia(matriz,ban):
	i=np.shape(matriz)
	f0=matriz
	if ban==1:
		for x in range(i[0]):
			if matriz[x]<0: 
				f0[x]=0 
			else: 
				f0[x]=1
	else:
		for x in range(i[0]):
			if matriz[x]<0:
				f0[x]=-1
			else: 
				f0[x]=1
	return f0

def multiplicacion(Peso,Y0):
	y,x=np.shape(Peso)
	Y1=np.zeros(x,dtype=np.longdouble)
	for j in range(y):
		for i in range(x):
			Y1[j]+=np.longdouble(Peso[j][i]*Y0[i])
	return Y1

def Compara(x,y):
	largo=np.shape(x)
	val=1
	for i in range(largo[0]):
		if x[i]!=y[i]:
			val=0
	return val

def Convertir(matriz,tipo):
	coller=[]
	if tipo==1:
		y,x=np.shape(matriz)
		for j in range(y):
			for i in range(x):
				if matriz[i][j]<=0:
					coller.append(int(-1))
				else:
					coller.append(int(1))
	elif tipo==2:
		x=np.shape(matriz)
		print(x)
		N=int(m.sqrt(x[0]))
		coller=np.zeros((N,N),int)
		conta=0
		for j in range(N):
			for i in range(N):
				if matriz[conta]==-1:
					coller[i][j]=0
					conta+=1
				else:
					coller[i][j]=255
					conta+=1

		print(coller)
				
		
			
	return coller


ent=[]
ent.append(Nueva_entrada('A.png')) #C1
ent.append(Nueva_entrada('B.png')) #C2
ent.append(Nueva_entrada('C.png')) #C3
'''
ent.append(Nueva_entrada('F.png')) #C4
ent.append(Nueva_entrada('G.png')) #C5
ent.append(Nueva_entrada('H.png')) #C6
ent.append(Nueva_entrada('I.png')) #C7
ent.append(Nueva_entrada('J.png')) #C8
ent.append(Nueva_entrada('L.png')) #C9
ent.append(Nueva_entrada('P.png')) #C10
ent.append(Nueva_entrada('S.png')) #C11
'''
W = matriz_de_peso(ent)
calculo(ent,ent,W)
