list=[]
number=int(input("donnez un nombre:"))
for i in range(1,number+1):
  if number%i==0:
    list.append(i)
len= len(list)
print("lest diviseurs de:"+str(number)+"sont:"+ str(list)+".")
print("il y en a donc "+str(len)+" au total.")