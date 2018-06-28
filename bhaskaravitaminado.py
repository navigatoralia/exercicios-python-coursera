#bhaskara.cpp digivolve para bhaskara.py
import math
def main():
   a = int(input("Digite o valor de a: "))
   b = int(input("Digite o valor de b: "))
   c = int(input("Digite o valor de c: "))

   if (a != 0 and b == 0):
       x1 = (math.sqrt(c))/ a
       print("Por que ce tá calculando essa merda em um programa, seu animal? a raiz é", x1)


   if (a == 0 and b != 0):
       x1 = c / b
       print("ISSO É UMA EQUAÇÃO DO PRIMEIRO GRAU, SEU MERDA, O RESULTADO DESTA BOSTA É", x1)

   if (a == 0 and b == 0 and c == 0):
       print("O QUE CARALHOS EU VOU CALCULAR ENTÃO, SEU INÚTIL?")

   if ( a == 0 and b == 0 and c != 0):
       print("AH, ENTÃO QUER DIZER QUE", c, "É IGUAL A ZERO, NÉ, SEU BOSTA?")

   if (a != 0 and b != 0):
       d = b ** 2 - 4 * a * c

       if (d == 0):
           x1 = - b / (2 * a)
           print("A equação tem uma raiz real e ela é", x1)

       if (d > 0):
           x1 = (- b + math.sqrt(d)) / (2 * a)
           x2 = (- b - math.sqrt(d)) / (2 * a)
           print("A equação tem duas raízes reais, e elas são", x1, "e", x2)

       if (d < 0):
           z = d * (-1)
           x1 = - b / (2 * a)
           conj1 = z / (2 * a)
           x2 = - b / (2 * a)
           conj2 = - z / (2 * a)
           print("A Equação tem duas raízes reais e imaginárias, que são", x1, "+", conj1, "i", "e", x2, conj2, "i")

#-------
main()
