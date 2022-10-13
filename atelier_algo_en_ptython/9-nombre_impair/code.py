import random#importation du module random qui sera utilisé plus bas ligne 7.
nb=int (input("donnez le nombre de nombres à générer!"))

list=[]
vérif=0#cette variable servira pour comter le nombre de fois que la condition sera validée.
for loop in range(nb):
  a=random.randint(0,100)#On génère des nombred compris entre 0 et 100 de manière aléatoire 
  if a%2==0:#On vérifie à l'aide du modulo si le nombre généré est pair. 
    vérif=vérif+1#On fait tourner la boucle.
  list.append(a)#On range le nombre dans le tableau s'il est pair
if vérif>0:#On vérifie que le tableau contient des nombres forcément pairs.
  print("il y a au moins un nombre pair dans la liste!")
  print(list)
else:
  print("il n'y a pas de nombre pair dans la     liste!")
 # list= list.split("|")
  print(list)
