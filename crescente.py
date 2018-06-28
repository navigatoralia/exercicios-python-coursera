#Exercício 5

def main():
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um número inteiro: "))
    n3 = int(input("Digite um número inteiro: "))

    if(n3 > n2 > n1):
        print("crescente")
    elif(n3 < n2 < n1):
        print("decrescente")
    else:
        print("alternante")

#-----
main()
