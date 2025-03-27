'''

def count_isolated(list) -> int:
    while n in range(count_isolated(+1(n) != -1(n))) :
        n +=1
        if n in range(0 or -1):
            pass
        return(n)
    
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
For example:

Test	Result
print(remove_elements({5, 6, 7}, [7, 8, 9]))
{5, 6}

'''

'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

    for element  in elements_to_remove:
        if element in original_set:
            original_set.remove(element)

    return original_set

print(remove_elements({5, 6, 7}, [7, 8, 9]))

'''
'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:

Test	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}
'''
'''
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key,value in dict1.items():
        if key in dict2:
            dict2[key] +=value
        else:
            dict2[key] = value
        
    return dict2 


    for key,value in dict1 + key,value in dict2:
        return key,value
    


print(merge_dictionaries({'x': 5}, {'x': -5}))




Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e 
viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri
opzionali per il parametro to_fahrenheit.

print(convert_temperature(0))
32.0
print(convert_temperature(32, False))
0.0


def convert_temperature(temp: int, to_fahrenheit=True) -> float:
    if to_fahrenheit:
        return(temp * 9/ 5) + 32
    else:
        return (temp - 32) * 5 / 9
'''
'''
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
For example:

Test	Result
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
2
print(count_isolated([1, 2, 3, 4, 5]))
5
'''
'''
def count_isolated(lst) -> int:
    cont = 0
    for n in range(len(list)):
        if n ==0:
            if lst[n]!=lst[n+1]:
                cont +=1
        elif n == len(lst)-1:
            if lst[n]!=lst[n-1]:
                cont +=1
        

        else:
            if lst[n]!=lst[n-1] and lst[n]!=lst[n+1]:
                cont+=1
    return cont 
        
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
'''
'''

def list_statistics(numbers: list[int]) ->list:
    media = sum(numbers) / len(numbers)
    max1 = max(numbers)
    
    min1 = min(numbers)
    return ( max1, min1,media)
print(list_statistics([1, 2, 3, 4, 5]))

'''

'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' 
sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
For example:

Test	Result
print(check_parentheses("()()"))
True
print(check_parentheses("(()))("))
False
'''

'''
def check_parentheses(expression: str) -> bool:
    for i in range(len(expression)):
        if expression[i]=="(":
            expression.find(i) ==")"
            
            return True
    else:
        return False
print(check_parentheses("()()"))

 la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
'''

def rotate_left(elements: list, k: int) -> list:
    if range(elements)| k :
        k == range(elements.remove())
        range(elements.pop())
        return elements


print(rotate_left([1, 2, 3, 4, 5], 2))

        


