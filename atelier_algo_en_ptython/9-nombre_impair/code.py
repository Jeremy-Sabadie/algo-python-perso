import random
nb=int (input("donnez le nombre de nombres à générer!"))

list=[]
vérif=0
for loop in range(nb):
  a=random.randint(0,100)
  if a%2==0:
    vérif=vérif+1
  list.append(a)
if vérif>0:
  print("il y a au moins un nombre pair dans la liste!")
  print(list)
else:
  print("il n'y a pas de nombre pair dans la     liste!")
 # list= list.split("|")
  print(list)