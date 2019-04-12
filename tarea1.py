import csv
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  



def Pearson(aux):
    print("hello")
Pearson(1)
with open('Movie_ratings.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(len(row))