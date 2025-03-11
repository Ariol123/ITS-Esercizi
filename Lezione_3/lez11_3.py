

'''
print(pi)
for n in pi :
    sum (pi)
    print(pi)
'''
'''
segno:int = -1
for i in range(10):
    segno*= -1
    print(segno)
'''

'''def cambia_segno():'''
'''
pi= 0
for i in range(15):
    if i ==0:
        pi+=3
    else:
        segno =(-1)**(i+1)

        de = 2*i

        demo = (de)*(de+1)*(de+2)

        pi +=(i)*(4/demo)

    print(pi)'''


targets:list = [3.14, 3.141, 3.1415, 3.14159]

for i in targets:
    pi:float = 0.0
    segno:int = 1
    denominatore: int = 1
    contatore: int = 0
    
    while True:
        pi += segno *(4/denominatore)
        segno *= -1
        denominatore += 2
        contatore += 1
        
        if str(pi)[:len(str(i))] == str(i):
            print(f"Numero di interazioni per otenere:{str(i)} è nr di Interazioni:{contatore}")
            break
