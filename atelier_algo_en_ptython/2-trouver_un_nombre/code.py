from random import*
i= randint(1,20)
asked=int(input("donnez un nombre:"))
if asked<i:
  print("Plus petit!")
if asked>i:
  print("Plus grand!")