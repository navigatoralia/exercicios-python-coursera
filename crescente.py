#Exercício 5

def main():
    nSeries = int(input("Digite o número de séries que vai perguntar: "))
    
    for i in range(nSeries):
        n1 = int(input("Digite um número inteiro: "))
        n2 = int(input("Digite um número inteiro: "))
        n3 = int(input("Digite um número inteiro: "))

        if(n3 > n2 > n1):
            print("crescente")
        else:
            print("não está em ordem crescente")

#-----
main()
