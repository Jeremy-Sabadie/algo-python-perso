list=[]
items=1
result=0
len=int(input("donnez la longueur de la liste:"))
for loop in range(len):
  ask=int(input("entrez un nombre:"))
  list.append(ask)
for loop in range(len):
  a=list.index(items)
  result= items+ a
  items=items+1
print(result)
sum=sum(list)#La méthode sum est utilisée pour calculer la somme du tableau qui contient les valeur entrées.
print("la somme des valeurs de la liste est de: "+str(sum)+".")
