import random

random.seed()

status = {
    "won" : 0,
    "verloren" : 0
}

won = False
temperatuur = 0
raadGetal = 0
getal = 0
geradenGetallen = 0
flag = True
raadNr = 0

while flag:
    raadGetal = random.randint(1, 100)

    while raadNr < 10:
        try:
            getal = int(input("Raad een getal tussen 1-100.\n"))
        except:
            print("Vul alstublieft een geheel getal in.")
            continue
        raadNr += 1
        temperatuur = raadGetal - getal
        if temperatuur < 0:
            print("Iets lager")
        elif temperatuur != 0:
            print("Iets hoger")

        temperatuur = abs(temperatuur)
        if temperatuur == 0:
            print("Gefeliciteerd!")
            won = True
            break
        elif temperatuur <= 20:
            print("Je bent heel warm.")
        elif temperatuur <= 50:
            print("Je bent warm.")
    raadNr = 0
    geradenGetallen += 1    
    if won:
        status["won"] += 1
        won = False
    else:
        status["verloren"] += 1

    print("Gewonnen:",status["won"],"\nVerloren:",status["verloren"])
    
    if geradenGetallen >= 20:
        flag = False

    while True:
        woord = input("Nog een ronde spelen? [y/n]")
        if woord != "y" and woord != "n":
            print("Vul A.U.B. \"y\" of \"n\" in.")
            continue
        elif woord == "n":
            flag = False
        break

print("Eindscore:",status["won"],"/",status["verloren"]+status["won"],"gewonnen")