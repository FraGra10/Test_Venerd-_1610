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
        
        
class Gestore:
    def __init__(self,tickets=[]):
        self.__tickets=tickets
    
    def crea():
        pass
    def leggi():
        pass
    def modifica():
        pass
    def rimuovi():
        pass
         