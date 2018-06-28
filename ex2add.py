#Questão 2 - Ex adicional
def main():
    segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))
    dia = segs // 86400
    restosegsdia = segs % 86400
    hora = restosegsdia // 3600
    restosegshora = restosegsdia % 3600
    minuto = restosegshora // 60
    segundo = restosegshora % 60
    print(dia, "dias,", hora, "horas,", minuto, "minutos e", segundo, "segundos.")

#-------
main()
