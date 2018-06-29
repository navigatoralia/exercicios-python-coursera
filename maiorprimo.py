def ePrimo(x):

    cont = 0
    
    for i in range(2, x):
        if (x % i == 0):
            cont += 1
            
    if (cont == 0):
        return True
    else:
        return False

#-----------
def maior_primo(n):
    i = 0
    while (n >= i):
        test = ePrimo(i)
        if (test == True):
           p = i
        i = i + 1
    return p

#-----------
def main():
    #p = 0
    n = int(input("Informe o número para o qual deseja analisar o maior primo: "))
    p = maior_primo(n)
    print("O maior primo é", p)

#------------
main()

