'''
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"
Expected Output:
Inserisci il voto di laurea: 110
Output: GPA 4.0
Inserisci il voto di laurea: 65
Output: Voto non valido

'''

voto: int = int(input("Si inserisca un numero compreso tra 66 e 110: "))


match voto:

    case 110|109|108|107|106:
        print(4.0)

    case 105|104|103|102|101:
        print(3.7)

    case 100|99|98|97|96:
        print(3.3)

    case 95|94|93|92|91:
        print(3.0)

    case 90|89|88|87|86:
        print(2.7)

    case 85|84|83|82|81:
        print(2.3)

    case 80|79|78|77|76:
        print(2.0)

    case 75|74|73|72|71|70:
        print(1.7)
        
    case 69|68|67|66:
        print(1.0)
    case _:

        print("Voto non valido")