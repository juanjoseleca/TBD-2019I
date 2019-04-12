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
        self.nombres=matriz[0]
        peliculas=[]
        matriz=matriz[1:]
        for i in range (len(matriz)):
            peliculas.append(matriz[i][0])
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
    def recommendar(self,nombre,pelicula):
        print("here")
##################
miSistema=SistemaDeRecomendacion()
miSistema.imprimir()
"""
for i in range(len(matriz)):
    matriz[i]=matriz[1:]
    print (matriz[i])
   """     