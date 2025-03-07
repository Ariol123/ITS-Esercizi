
def show_messages(listArg):
    for i in listArg:
        print(i)

listArg = ["Bella ciao!", "Come va!", "Ciao Roma!"]

show_messages(listArg)

def end_messages(listArg):
    sent_messages=[]

    for i in listArg:
        print(i)

        sent_messages.append(i)
        print(sent_messages)

end_messages(listArg)

