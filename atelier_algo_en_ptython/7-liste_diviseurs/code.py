list=[]
number=int(input("donnez un nombre:"))
for i in range(1,number+1):
  if number%i==0:#Onteste à l'aide du modulo si la valeur du tour de boucle est un diviseur du nombre passé ou non.
    list.append(i)#si le nombre passé est un diviseur du nombre passé , il est rangé dans le tableau list.
len= len(list)#La valeur du nombre de diviseurs est atribué à la variable len pour êtr affichée plus bas.
print("les diviseurs de:"+str(number)+"sont:"+ str(list)+".")
print("il y en a donc "+str(len)+" au total.")