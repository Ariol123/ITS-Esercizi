



voto = int(input(f"Voto:"))

match voto:
    case (106|107|108|109|110):
        print(4.0)
    case (101|102|103|104|105):
        print(3.7)
    case (96|97|98|99|100):
        print(3.3)
    case vote if 91 <= voto <= 95:
        print (3.0)
    case vote if 86 <= voto <= 90:
        print(f"La votazione e:2.7")
    case vote if 81<= voto <= 85:
        print(f"La votazione e:2.3")
    case vote if 76 <= voto <= 80:
        print(f"La votazione e:2.0")
    case vote if 70 <= voto <= 75:
        print(f"La votazione e:1.5")
    case vote if 66 <= voto <= 69:
        print(f"La votazione e:1.0")
    case _:
        print(f"Voto non valido")
    
