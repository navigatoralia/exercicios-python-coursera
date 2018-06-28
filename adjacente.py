#Dígito adjacente

def main():
    dig = dig2 = cond = 0
    num = int(input("Digite um número inteiro: "))
    while (num != 0):
        
        dig = num % 10
        num = num // 10

        if (dig2 == dig):
            cond = 1

        dig2 = dig

    if (cond == 1):
        print("sim")
    else:
        print("não")


#----
main()
