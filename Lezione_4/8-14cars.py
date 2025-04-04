def car(manufacturer, model, color:None):
    manufacturer = {productor:"name_of_p", model:"model_name", none:"color"}
    return manufacturer

while True:
    productor = input("Scrivere nome del produttore")
    model = input("Scrivere nome modelo machina")
    none = input("Inserisci colore ")
    costructor = car(productor,model,none)

    if productor == "benz":
        break

print(costructor)




