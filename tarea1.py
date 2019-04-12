import csv
import math
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  



def Pearson(x,y):
    if(len(x)!=len(y)):
        print("error de tamaño")
        return
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    n=len(x)  #longitud del array
    for i in range(n):
        sum1+=x[i]*y[i]
        sum2+=x[i]
        sum3+=y[i]
        sum4+=x[i]**2
        sum5+=y[i]**2
    return (sum1-((sum2*sum3)/n))/(math.sqrt(sum4-((sum2**2)/n))*math.sqrt(sum5-((sum3**2)/n)))
def Coseno(x,y):
    if(len(x)!=len(y)):
        print("error de tamaño")
        return
    sum1=0
    sum2=0
    sum3=0
    n=len(x)
    for i in range(n):
        sum1+=x[i]**2
        sum2+=y[i]**2
        sum3+=x[i]*y[i]
    return sum3/(math.sqrt(sum1)*math.sqrt(sum2))
class SistemaDeRecomendacion:
    def __init__(self):
        self.matriz=[]
        self.peliculas=[]
        self.preprocesamiento()
    def preprocesamiento(self,archivo="Movie_ratings.csv"):
        documento = open("Movie_ratings.csv", "r")
        ####Preprocesamiento
        matriz=[]
        for x in documento:
            x=x.rstrip('\n')
            matriz.append(x.split(","))
        self.nombres=matriz[0][1:]
        for ix in range(len(self.nombres)): 
            self.nombres[ix]=self.nombres[ix].replace('"','')
        matriz=matriz[1:]
        for i in range (len(matriz)):
            self.peliculas.append(matriz[i][0].replace('"',''))
            matriz[i]=matriz[i][1:]
            for ix in range(len(matriz[i])):
                if(matriz[i][ix]==''):
                    matriz[i][ix]=0
                else:
                    matriz[i][ix]=int(matriz[i][ix])
        self.matriz_t=[[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    def imprimir(self):
        print("Distancia entre dos: ",Pearson(self.matriz_t[0],self.matriz_t[1]))
        print("Distancia entre dos: ",Coseno(self.matriz_t[0],self.matriz_t[1]))
    def recomendar(self,nombre,pelicula,k):
        i_nombre=self.nombres.index(nombre)
        i_pelicula=self.peliculas.index(pelicula)
        distancias=[0]*len(self.matriz_t)
        for i in range(len(self.matriz_t)):
            if(self.matriz_t[i][i_pelicula]!=0 and i!=i_nombre):
                distancias[i]=Pearson(self.matriz_t[i],self.matriz_t[i_nombre])
            else:
                distancias[i]=0
        pos_sorted=sorted(range(len(distancias)), key=lambda k: distancias[k],reverse=True)
        pos_sorted=pos_sorted[:k]
        ponderado=0
        print("Vecinos mas cercanos de",nombre,": ")
        for i in pos_sorted:
            print(self.nombres[i]," : ",self.matriz_t[i])
            ponderado+=self.matriz_t[i][i_pelicula]
        print("El puntaje recomendado para ",nombre," en la pelicula ",pelicula," es: ",ponderado/k)
        return ponderado/k

##################
miSistema=SistemaDeRecomendacion()
miSistema.recomendar("Patrick C","Village",3)
"""
for i in range(len(matriz)):
    matriz[i]=matriz[1:]
    print (matriz[i])
   """     