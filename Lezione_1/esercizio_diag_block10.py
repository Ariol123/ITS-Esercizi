reddito = int(input("reddito:"))
media_voti = int(input("media"))

if reddito < 20000 and media_voti > 27:
    print("Borsa di studio approvata!")
else:
    print("Borsa di studio rifiutata.Motivo reddito alto o media insufficente!")



#match reddito:
#    case reddito if reddito < 20000 and media_voti > 27:
#        print("Borsa di studio approvata!")
#   case _:
#       print("Borsa di studio rifiutata.Motivo reddito alto o media insufficente!")

