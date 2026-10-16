
#utente1 = Utente()
#admin1 = Admin()

while True:
    print("Sei un utente o admin? [u] / [a]")
    match input().lower:
        case 'u':
            print("Inserisci l'azione da svolgere")
            print("[C] Crea   [L] Leggi")
            match input().lower:
                case 'c':
                    testoticket = input("Inserisci il messaggio del ticket: ")
                    utente1.crea(testoticket)
                case 'l':
                    numticket = int(input("Inserisci il numero del ticket: "))
                    utente1.leggi(numticket)
                
        case 'a':
            print("[C] Crea   [L] Leggi   [M] Modifica   [R] Rimuovi")
            match input().lower:
                case 'c':
                    testoticket = input("Inserisci il messaggio del ticket: ")
                    utente1.crea(testoticket)
                case 'l':
                    numticket = int(input())
                    utente1.leggi(numticket)
                case 'm':
                    numticket = int(input("Inserisci il numero del ticket da modificare: "))
                    testoticket = input("Inserisci il messaggio del ticket: ")
                    admin1.modifica(numticket, testoticket)
                    
        






            
    