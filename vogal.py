def vogal(l):
    
    if (l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u'):
        
        return True
        
    else:
    
        return False
#----------------

def main():

    letra = input("Digite a letra a se analisar: ")
    print (vogal(letra))
    
#----------------
main()
