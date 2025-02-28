'''
Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"

- - - - - - - - - - - - - - - - - - - - - -

frase: ho vinto!
Output: Wow!
'''

caso_lettura:str = input("SCRIVI una frase:")

match caso_lettura:
    case caso_lettura if caso_lettura[-1]=="?" and len(caso_lettura) %2==0:
        print(f"{caso_lettura} Si")
    case caso_lettura if caso_lettura[-1]=="?" and len(caso_lettura) %2!=0:
        print(f"{caso_lettura} No")
    case caso_lettura if caso_lettura[-1]=="!":
        print(f"{caso_lettura} Wow!")
    case _:
        print(f'Tu dici "{caso_lettura}"')
