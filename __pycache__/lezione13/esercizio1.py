'''def recorsiv_power(base:int, exponent:int)-> int:

    if exponent == 0:
        return 1
    
    elif base ==0:
        return 0
    
    else:
        return int(base *recorsiv_power(base,exponent -1))
    
print(f"3,4: {recorsiv_power(3,4)}")
'''

def vowelsCounter(s:str)->int:
    if not s:
        return 0
    
    if s[0].lower() in ["a","e","i","o","u"]:
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])
    


print(f"La stringa \"Ciao\" ha {vowelsCounter('Ciao')} vocali")
