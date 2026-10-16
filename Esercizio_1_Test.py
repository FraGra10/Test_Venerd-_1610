#Classe Admin 

class Admin(Ticket):
    
    def __init__(self,ID,titolo,descrizione,stato,nome):
        
        super().__init__(ID,titolo,descrizione,stato)
        
        self.__nome = nome
        self.__password = ""
        
    def get_nome(self):
        
        return self.__nome 
    
    def set_password(self,pwd):
        
        if(len(pwd) <  0 ):
            print("Password non valida!")
        else:
            self.__password = pwd 
    
    def modifica_ticket(self):
        
        new_ID = input("Inserisci nuovo ID del ticket: ")
        
        
        