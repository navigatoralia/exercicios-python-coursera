#exercício adicional

def main():

    x = int(input("Digite um número inteiro: "))
    cont = 0
    
    for i in range(2, x):
        if (x % i == 0):
            cont += 1
            
    if (cont == 0):
        print("primo")
    else:
        print("não primo")

#------
main()


