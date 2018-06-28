#Distância entre dois pontos
import math
def main():

     x1 = int(input("Informe a coordenada x do ponto 1: "))
     y1 = int(input("Informe a coordenada y do ponto 1: "))
     x2 = int(input("Informe a coordenada x do ponto 2: "))
     y2 = int(input("Informe a coordenada y do ponto 2: "))
     
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     if (dist >= 10):
        print("longe")
     else:
        print("perto")

#------
main()
