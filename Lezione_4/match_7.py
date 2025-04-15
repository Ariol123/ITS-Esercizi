'''
Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome,
 il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

'''


utente = {"nome":input("Inserisci il nome: "),"ruolo":input("Inserisci il ruolo: "),"età":int(input("Inserisci l'età: "))}

match utente:
    case {"ruolo":"admin"}:
        print("Accesso completo a tutte le funzionalità.")
    case {"ruolo":"moderatore"}:
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case utente if utente["età"] >= 18 and utente["ruolo"] == "utente" :
        print("Accesso limitato!  Accesso standard a tutti i servizi")
    case utente if utente["età"] < 18 and utente["ruolo"] == "utente" :
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"ruolo":"ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

