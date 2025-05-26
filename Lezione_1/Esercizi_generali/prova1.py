'''
1. Cambio Valore
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

''''''
x:int = 6




if x % 2 == 0:
    x / 2
    print(x)
else:
    x * 3 -1
    print(x)'''
'''
a = 1
b = 1
number = int(input("numero: "))
while a < number:
    print(f"{a} x {b} = {a * b}")
    b+=1
    if b == number:
        pass

    while b <= number:
        a +=1
        print(f"{a} x {b} = {a * b}")
        b +=1
        if a and b == number:
            break
'''
'''

numero = int(input("Give a number"))
             
    
for i in range(1, numero + 1):
    for j in range (1, numero + 1):
     print (f"{i} x{j} = {i * j}")
    

'''
'''
letter = input("give me a series of strings ") 

for i in letter:
    for element in i:
        print(element[:1])'''

'''def seven_brothers():
    print("Aapo \nEero\nJuhani\nLauri\nSimeoni\nTimo\nTuomos")
if __name__ == "__main__":
    seven_brothers()'''

'''
def first_character(text):
    print(f"{text[0]}")

#
# testing the function:
if __name__ == "__main__":
    first_character('python')
   first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')'''
'''
def mean(a,b,c):
    sum = a+b+c
    mean_x = sum / 3
    print(mean_x)
# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)'''
'''
def print_many_times(text: str, times: int):
    for i in range(times):
        print(text)
   

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)

def hash_square(length):
    for i in range(length ):
        print(length * "#")
   
if __name__ == "__main__":
    hash_square(7)'''
'''

def squared (ab ,intero):
   '''
'''
    for i in range(intero):
        if len(ab) < intero:
            ab += ab[0]
        
        

        print (ab)'''