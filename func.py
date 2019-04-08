word=input("enter language: ")
def sayhi(lang):
    if(lang=="es"):
        return("Hola")
    elif(lang=="French"):
        return("Bonjour")
    elif(lang=="Eng"):
        return("Hello")
if(word=="es"):
    print(sayhi(word),"Amigo")
elif(word=="French"):
    print(sayhi(word),"Monsieur")
elif(word=="Eng"):
    print(sayhi(word),"Mr")
