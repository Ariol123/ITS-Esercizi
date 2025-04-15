'''#def even_odd_pattern(numbers:list[int]) -> list[int]:
'''

    for i in numbers:
        if i % 2 == 0:
            numero=numbers.append(i)
            return numero
        elif i % 2 !=0:
            numero=numbers.append(i)
            return numero
        
'''

#print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    for i in x and y:
        sum = 0
        sum = x[i] + y[i]

        somma_elementi = sum
        return somma_elementi
    
    
print(somma_elementi([1,1,1],[1,1,1]))

'''

def blackjack_hand_total(cards: list[int]) -> int:
