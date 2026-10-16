
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
                    utente1.crea()
                case 'l':
                    utente1.leggi()
                case _:
                    pass
                
        case 'a':
            passinput = "?"
            login = False
            while passinput != "":
                passinput=input("Inserisci la password: ")
                if passinput == admin1.get_password():
                    login = True

            if login:
                print("[C] Crea   [L] Leggi   [M] Modifica   [R] Rimuovi")
                match input().lower:
                    case 'c':
                        admin1.crea()
                    case 'l':
                        admin1.leggi()
                    case 'm':
                        admin1.modifica()
                    case 'r':
                        admin1.rimuovi()
                    case _:
                        pass





            
    