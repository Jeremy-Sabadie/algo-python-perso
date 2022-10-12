startPierre=int(input("arrivée de Pierre :"))
endPierre=int(input("départ de Pierre :"))
startPaul=int(input("arrivée de Paul :"))
endPaul=int(input("départ de Paul :"))
condition= (startPierre>=startPaul) and (startPierre<=endPaul) or(endPierre>=startPaul) and (endPierre<=endPaul)
if condition:
  print("Pierre et Paul sont amis.")
else:
  print("Pierre et Paul ne sont pas amis.")