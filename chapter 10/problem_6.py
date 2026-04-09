''' Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.'''




from random import randint

class train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
        
    def book(slf,fro,to):
        print(f"The ticket is booked in train no. {slf.trainNo} from {fro} to {to}")
    def getStatus(slf):
        print(f"The Train No. {slf.trainNo} is running on time ")
    
    def getfare(slf,fro,to):
        print(f"Ticket fare in train no. {slf.trainNo} from {fro} to {to} is {randint(100,999)}")
        
t=train(15935)
t.book("Goa","Delhi")
t.getStatus()
t.getfare("Goa","Delhi")