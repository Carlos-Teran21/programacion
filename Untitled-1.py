print("elija una opcion del menu: \n1-crear persona\n2-eliminar persona\n3-listar personas\n4-buscar personas")
l=int(input())
while(m! =0 or l!=5):

 if(l == 1):
   print("digite el valor a agregar: ")
   lista1 = list()
   lista1.append(input())
   print("agregaste: ",lista1)

 if(l == 2):
  lista2 = list()
  lista2.append(lista1)   
  lista2.append("maria")   
  lista2.append("carlos")
  print("elija a la persona que desea eliminar",lista2) 
  
