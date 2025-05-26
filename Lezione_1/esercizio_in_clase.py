'''

x = 2

if x % 2 == 0:
    a =x /2 
    print (a)
elif x % 2 !=0:
    b =(x * 3) - 1
    print(b)
'''

'''
#numero_input = int(input("Give a nr"))
x = 42.0

def collatz(x: float) -> float:
    if x % 2 == 0:
         
         return x /2
   
    elif x % 2 !=0:

        return(x * 3) - 1
    
risultato: float = collatz(x=x)
print(risultato)
        '''
''''''




dipendenti: dict = {
    "rgergg": 40.5,
    "DHGTH": 55.5,
    "YUJGHFGH":43.5
}

def calcola_stipendio_dipendenti(elenco_dipendenti: dict):

    stipendi_lordi_dipendenti: dict = {}

    PAGA_ORARIA: float = 10.0
    MOLTIPLICATORE: float = 1.5

    for key, value in elenco_dipendenti.items():

        if value <= 40:

            stipendi_lordi_dipendenti[key] = value * PAGA_ORARIA
        
        else:

            stipendi_lordi_dipendenti[key]  = ( 40 * PAGA_ORARIA) + ((value - 40) * PAGA_ORARIA * MOLTIPLICATORE)

    return stipendi_lordi_dipendenti

print(calcola_stipendio_dipendenti(elenco_dipendenti = dipendenti))







