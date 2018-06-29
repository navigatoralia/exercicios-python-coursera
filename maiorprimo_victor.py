import math

def ePrimo(x):

    for i in range(2, int(math.sqrt(x))):
        if (x % i == 0):
            return False

    return True
    
#-----------

def main():

    n = int(input("Informe o número para o qual deseja analisar o maior primo: "))

    for i in range(n,1,-1):
        if ePrimo(i):
            print("O maior primo é", i)
            break

#------------
main()

