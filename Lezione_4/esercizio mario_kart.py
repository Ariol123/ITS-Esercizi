






numero: int = int(input("Inserisci numero:"))

match numero:
    case 1:
        print("1st")
    case 2:
        print("2nd")
    case 3:
        print("3rd")
    case _:
        print(f"{numero}th")

