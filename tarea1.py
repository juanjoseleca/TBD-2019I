import csv
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
    return (sum1-((sum2*sum3)/n))/(sqrt(sum4-((sum2**2)/n))*sqrt(sum5-((sum3**2)/n)))
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
    return sum3/(sqrt(sum1)*sqrt(sum2))

documento = open("Movie_ratings.csv", "r")
####Preprocesamiento
matriz=[]
for x in documento:
    x=x.rstrip('\n')
    matriz.append(x.split(","))
nombres=matriz[0]
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
matriz_t=[[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
##################
print(matriz)
print("")
print(matriz_t)
transpuesta=[[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(peliculas)
print(nombres)
"""
for i in range(len(matriz)):
    matriz[i]=matriz[1:]
    print (matriz[i])
   """     