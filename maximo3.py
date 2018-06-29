#tentativa de função

def maximo(x,y,z):

    if (x > y > z or x > z > y):
        return x
    elif (y > x > z or y > z > x):
        return y
    else:
        return z


def main():

    x = int(input("Digite um número: "))
    y = int(input("Digite um número: "))
    z = int(input("Digite um número: "))
    print(maximo (x,y,z))

#----------------
main()
