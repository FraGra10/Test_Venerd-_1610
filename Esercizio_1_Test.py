class Utente():
    
    def __init__(self,nome,password):
                
        self.__nome = nome
        self.__password = password
    
    # Get functions   
    def get_nome(self):
        
        return self.__nome
    
    def get_password(self):
        return self.__password 
    
    #Set Functions
    def set_password(self,pwd):
        
        if(len(pwd) <  0 ):
            print("Password non valida!")
        else:
            self.__password = pwd
    
    def set_nome(self,nome):
        
        if(len(nome) < 0):
            print("Nome non valido!")
        else:
            self.__nome = nome 
            
    #Funzione per modificare l'ID del ticket
    def modifica_ID_ticket(self,Ticket_1):
        
        num_ticket = int(input("Inserisci il numero del ticket: "))
        
        Ticket_1.set_id(num_ticket)
    
    #Funzione che modifica la descrizione del ticket 
    def modifica_descrizione_ticket(self,Ticket_1):
        
        ticket_descr = input("Modifica la descrizione del ticket: ")
        
        if(len(ticket_descr) < 0 ):
            print("descrizione non valida")
        else:
            Ticket_1.set_descrizione(ticket_descr)

    #Funzione che modifica lo stato del ticket
    def modifica_stato(self,Ticket_1):
    
        ticket_state = input("Modifica lo stato del ticket: ")

        if(len(ticket_state) < 0 ):
            print("stato non valida")
        else:
            Ticket_1.set_stato(ticket_state)


class Admin(Utente):
    
    def __init__(self,nome,password):
                
        self.__nome = nome
        self.__password = password
    
    # Get functions   
    def get_nome(self):
        
        return self.__nome
    
    def get_password(self):
        return self.__password 
    
    #Set Functions
    def set_password(self,pwd):
        
        if(len(pwd) <  0 ):
            print("Password non valida!")
        else:
            self.__password = pwd
    
    def set_nome(self,nome):
        
        if(len(nome) < 0):
            print("Nome non valido!")
        else:
            self.__nome = nome 
            
    #Funzione per modificare l'ID del ticket
    def modifica_ID_ticket(self,Ticket_1):
        
        num_ticket = int(input("Inserisci il numero del ticket: "))
        
        Ticket_1.set_id(num_ticket)
    
    #Funzione che modifica la descrizione del ticket 
    def modifica_descrizione_ticket(self,Ticket_1):
        
        ticket_descr = input("Modifica la descrizione del ticket: ")
        
        if(len(ticket_descr) < 0 ):
            print("descrizione non valida")
        else:
            Ticket_1.set_descrizione(ticket_descr)

    #Funzione che modifica lo stato del ticket
    def modifica_stato(self,Ticket_1):
    
        ticket_state = input("Modifica lo stato del ticket: ")

        if(len(ticket_state) < 0 ):
            print("stato non valida")
        else:
            Ticket_1.set_stato(ticket_state)
    
    #Funzione elimina ticket
        
        
        