'''
In questo problema ricreerete la classica gara tra la tartaruga e la lepre. 
Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. 
I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati.
 Ogni quadrato rappresenta una posizione lungo il percorso della corsa. 
 Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara.
 Durante la corsa, i contendenti possono occasionalmente perdere terreno. 
 C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, 
 il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.
- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. 
Usate delle variabili per tenere traccia delle posizioni degli animali 
(i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 
(cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.
Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, 
nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7,
 o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.
Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'
Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
 
'''
posizioniAnimali = [1,71,1]
import random





def tartarugaPassi(posizione):
    percentuali_delle_mosse = random.randint(1,10)

    if 1 <= percentuali_delle_mosse <= 5:
        posizione +=3
    elif 6 <= percentuali_delle_mosse <= 7:
        posizione -=6
        if posizione <=1:
            posizione == 1
    elif 8 <= percentuali_delle_mosse <= 10:
        posizione +=1
    

        
        



def __init__(self, mossa_tartaruga, mossa_lepre):
    self.mossa_tartaruga = mossa_tartaruga
    self.mossa_lepre = mossa_lepre
