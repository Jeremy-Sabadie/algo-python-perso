R=int(input(" entrez le rayon du cercle en cm:"))
π=3.14#on stock la valeur arrondie de oi dans une variable
aire=π*R*R#formule de l'aire d'un cercle: piXle rayon au carré.and
aire= float(aire)#on transforme l'a valeur de l'aire en float pour pouvoir le manipuler ensuite et l'afficher.
aire= int(aire)#on transforme l'a valeur de l'aire en entier pour pouvoir le manipuler ensuite et l'afficher.
aire= str(aire)#on transforme l'a valeur de l'aire en chaîne de caractères pour pouvoir la concaténer.
#Ici on fait les mêmes manipulations avec la variable contenant la valeur de la circonférence qu'avec  celle de l'aire
circ=2*π*R
circ= float(circ)
circ= int(circ)
circ= str(circ)
aire=str(aire)


print("la surface du cercle est de: "+aire+" cm .")
print("le périmètre du cercle est de: "+circ+" cm .")