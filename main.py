# PROGETTO DI GRUPPO
# Andiamo a creare un sistema che permetta di gestire l'inserimento di ticket di richieste che possono essere gestiti in CRUD (create, read, update, delete)
# Inoltre ci deve essere una classe utente che può inserire e vedere, e una admin che può modificare ed eliminare oltreché risolvere i ticket ovvero chiuderli e salvarli in una lista ticket chiusi, è obbligatorio usare le tre regole fondamentali
# Una repository per gruppo. Presentazione 15 min a gruppo.

class Ticket:
    def __init__(self,id:int, titolo:str, descrizione:str):
        self.__id=id
        self.__titolo=titolo
        self.__descrizione=descrizione
        self.__stato="Aperto"
        
    def get_id(self):
    
        return self.__id
    
    def set_id(self,id):
    
          self.__id=id
    
    def get_titolo(self):
    
        return self.__titolo
    
    def set_titolo(self,titolo):
    
          self.__titolo=titolo
    
    def get_descrizione(self):
    
        return self.__descrizione
    
    def set_descrizione(self,descrizione):
    
          self.__descrizione=descrizione
    
    def get_stato(self):
    
        return self.__stato
    
    def set_stato(self,stato):            
    
          self.__stato=stato            

class Utente():

    #METTI AGGIUNGI TICKET E LEGGI TICKET

    
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

    def aggiungi_ticket(self,Gestore_Ticket,Ticket):
        print("Aggiunta del ticket tramite gestore: ")
        ID =  int(input("Inserisci l'ID del ticket da aggiungere: "))
        Gestore_Ticket.aggticket(ID,Ticket)
        
class Admin(Utente):

    #METTI ELIMINA TICKET
    
    def __init__(self,nome,password):
                
        self.__nome = nome
        self.__password = password
    
            
    #Funzione per modificare l'ID del ticket
    def modifica_ID_ticket(self,Ticket_1,Gestore_Ticket):
        
        num_ticket = int(input("Inserisci il numero del ticket: "))
        
        Gestore_Ticket.modificaidticket(num_ticket)
    
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
            
    def elimina_ticket(self,Gestore_Ticket):
        print("Eliminazione del ticket tramite gestore: ")
        ID =  int(input("Inserisci l'ID del ticket da aggiungere: "))
        Gestore_Ticket.aggticket(ID,Ticket)
        
        





#######

Ticket_1 = Ticket(1023,"posto_1","check in posto A14")

Admin_1  = Admin("Filippo","ABCD")
Admin_1.modifica_stato(Ticket_1)
Utente_1 = Utente("Mario", "200")


while True:
    print("Sei un utente o admin? [u] / [a]")
    match input().lower:
        # SCELTA UTENTE
        case 'u':
            print("Inserisci l'azione da svolgere")
            print("[C] Crea   [L] Leggi")
            match input().lower:
                case 'c':
                    Utente_1.crea()
                case 'l':
                    Utente_1.leggi()
                case _:
                    pass
                
        # SCELTA ADMIN
        case 'a':
            passinput = "?"
            login = False
            while passinput != "":
                passinput= input("Inserisci la password: ")
                if passinput == Admin_1.get_password():
                    login = True

            if login:
                print("[C] Crea   [L] Leggi   [M] Modifica   [R] Rimuovi")
                match input().lower:
                    case 'c':
                        Admin_1.crea()
                    case 'l':
                        Admin_1.leggi()
                    case 'm':
                        Admin_1.modifica()
                    case 'r':
                        Admin_1.rimuovi()
                    case _:
                        pass

                    