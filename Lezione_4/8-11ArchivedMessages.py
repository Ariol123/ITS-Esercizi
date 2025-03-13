

listArg = ["Bella ciao!", "Come va!", "Ciao Roma!"]


def end_messages(listArg):
    sent_messages=[]

    for i in listArg:
        print(i)

        sent_messages.append(i)
        print(sent_messages)

end_messages(listArg)

def send_messages(listArg):
    print(listArg)

send_messages(listArg)

