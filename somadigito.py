#somadigitos.py

def main():

    num = int(input("Digite um número inteiro: "))
    soma = 0
    while (num != 0):
        dig = num % 10
        num = num // 10
        soma = soma + dig
        
    print(soma)
    
#----
main()
