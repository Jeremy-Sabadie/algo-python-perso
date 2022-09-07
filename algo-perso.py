from random import *
import statistics
from math import*
max=int(input("la valeur maximale des tirages sera de?"))
min=int(input("la valeur minimale des tirages sera de?"))
tab=[]
x=int(input("entrez le nombre d'items à stocker:"))
for loop in range(x):
  n = randint(min,max)
   
  
  tab.append(n)
mean = statistics.mean(tab)
size= len(tab)
print("la moyenne des tirages est de : "+str(mean)+"avec un minimum de: "+str(min)+"et un maximum de : "+str(max)+" dans une liste de: "+str(size)+" items.")