#bhaskara.cpp digivolve para bhaskara.py
import math
def main():
   a = int(input("Digite o valor de a: "))
   b = int(input("Digite o valor de b: "))
   c = int(input("Digite o valor de c: "))
   d = b ** 2 - 4 * a * c

   if (d == 0):
       x1 = - b / (2 * a)
       print("a raiz desta equação é", x1)

   if (d > 0):
       x1 = (- b + math.sqrt(d)) / (2 * a)
       x2 = (- b - math.sqrt(d)) / (2 * a)
       if (x1 < x2):
           print("as raízes da equação são", x1, "e", x2)
       else:
           print("as raízes da equação são", x2, "e", x1)

   if (d < 0):
       print("esta equação não possui raízes reais")

#-------
main()
