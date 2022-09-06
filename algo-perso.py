from random import *
import statistics
from math import*
max=int(input("le maximum des tirages sera de?"))
min=int(input("le minimum des tirages sera de?"))
tab=[]
x=int(input("entrez le nombre de tour de boucle:"))
for loop in range(x):
  n = randint(min,max)
   
  print("le nombre tiré est :"+str(n))
  tab.append(n)
x = statistics.mean(tab)
print("la moyenne des tirages est de : "+str(x)+"avec un minimum de: "+str(min)+"et un maximum de : "+str(max))