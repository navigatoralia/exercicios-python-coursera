#impares.py

def main():

    n = int(input("Digite o valor de n: "))
    cont = 0
    i = 0
    while (cont < n):
        if ( i % 2 != 0):
            print(i)
            cont = cont + 1
        i = i + 1    
#------

main()    
