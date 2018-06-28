def main(): 
   
    pot = 0
    n = int(input("Digite a base da potência:"))
    k = int(input("Digite o expoente da potência:"))
    if (k < 0): print ("Você não possui saldo para completar esta chamada")      
    pot = n ** k
    print ("o resultado desta grande bosta é", pot)
    
#--------
main()
