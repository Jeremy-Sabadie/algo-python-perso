list=[]
items=1
result=0
len=int(input("donnez la longueur de la liste:"))
for loop in range(len):
  ask=int(input("entrez un nombre:"))
  list.append(ask)
sum=sum(list)
mean=sum/len
print("la somme de la liste est de : "+str(sum)+".")
print("la moyenne est de: "+str(mean)+".")