nb = int(input("entrez un nombre à vérifier:"))
array = []
condition = False
for a in range(1, nb):
  if nb % a == 0:
    array.append(a)  #On stocke les diviseurs du nombre testé dans un tableau.
  a += 1
sumArray = sum(
  array
)  #La méthode sum est utilisé pour calculer la somme des diviseurs du nombre passé qui étaient rangés dans le tableau.


#début de la fonction pour multiplier les items du tableau.
def product(array):
  global prod
  prod = 1
  for i in array:
    prod = prod * i


# Fin de la fonction product.
#Appel de la fonction product sur array.
product(array)
multArray = prod
if nb == sumArray and nb == multArray:
  condition = True
if condition:
  print("VOTRE NOMBRE EST UN NOMBRE PARFAIT CAR : ")
  print("_le produit ainsi que la somme des diviseurs de " + str(nb) +
        " sont éguaux à : " + str(sum(array)) + " .")
  print("_les diviseurs de " + str(nb) + " sont: " + str(array) + " .")
elif condition == False:
  if prod != nb:

    print("le produit des diviseurs de" + str(nb) + " n'est pas égal à: " +
          str(nb) + " mais est égal à : " + str(prod) + " .")
  elif sumArray != nb:
    print("_ la somme  des diviseurs de " + str(nb) + " n'est pas égal à:  " +
          str(nb) + " mais est égal à: " + str(sum(array)) + " .")
  print("DONC VOTRE NOMBRE N'EST PAS UN NOMBRE PARFAIT!")
  print("_les diviseurs de " + str(nb) + " sont: " + str(array) + " .")
