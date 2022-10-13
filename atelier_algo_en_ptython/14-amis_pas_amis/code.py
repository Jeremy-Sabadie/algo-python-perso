startPierre=int(input("arrivée de Pierre :"))
endPierre=int(input("départ de Pierre :"))
startPaul=int(input("arrivée de Paul :"))
endPaul=int(input("départ de Paul :"))
condition= (startPierre>=startPaul) and (startPierre<=endPaul) or(endPierre>=startPaul) and (endPierre<=endPaul)#O déclare comme condition que si l'arrivée de Pierre est comprise entre l'arrivée de Paul et le départ de Paul, alors ils sont ammis.

if condition:#Si la condition est remplie alors on affiche qu'ils sont amis.
  print("Pierre et Paul sont amis.")
else:#Sinon on dit qu'ils ne sont pas amis.
  print("Pierre et Paul ne sont pas amis.")