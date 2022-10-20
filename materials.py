class materiel:
    X = 0
    T = []

    def __init__(self,code="",nom="",etat="",date=""):
        self.code = code
        self.nom = nom
        self.etat = etat
        self.date = date

    def ajouter(self):
        self.code = input("entrer le code\n")
        self.nom = input("entrer le nom\n")
        self.etat = input("entrer le l'etat de materiel\n")
        self.date = input("entrer la date d'achat\n")
        materiel().T.append(self.code)
        materiel().T.append(self.nom)
        materiel().T.append(self.etat)
        materiel().T.append(self.date)

    def afficher(self):
        if (len(materiel().T) == 0):
            print("n'a pas des materiel en panne")
        else:
            self.exists = False
            self.i = 0
            while(self.i<len(materiel().T)):
                if (materiel().T[self.i+2] == "en panne"):
                    print("le code est:" , materiel().T[self.i])
                    print("le nom est:" , materiel().T[self.i+1])
                    print("l'etat est:" , materiel().T[self.i+2])
                    print("la date d'achat est:" , materiel().T[self.i+3])
                    self.exists = True
                    materiel().X = input("-----------\n")
                self.i+=4
            if (self.exists == False):
                print("n'est pas une materiel en panne")
    
    def supprimer(self):
        if (len(materiel().T) == 0):
            print("n'a pas des materiel")
        else:
            self.que = input("voulez-vous vraiment supprimer tous les materiel en panne ? entrer 'oui' ou 'non'\n")
            if (self.que == "oui"):
                self.exists = False
                self.i = 0
                while(self.i<len(materiel().T)):
                    if (materiel().T[self.i+2] == "en panne"):
                        materiel().T.pop(self.i)
                        materiel().T.pop(self.i)
                        materiel().T.pop(self.i)
                        materiel().T.pop(self.i)
                        self.i-=4    
                        self.exists = True
                    self.i+=4
                
                if (self.exists == False):
                    print("n'est pas une materiel en panne")

                if (self.exists == True):
                    print("les materiel en panne est ete supprimer")


M = materiel()
while(True):
    ch = int(input("1 - ajouter d'une materiel\n2 - afficher la liste de materiel en panne\n3 - supprimer de tous materiel en panne\n4 - sortir\n"))
    if (ch == 1):
        M.ajouter()
    elif (ch == 2):
        M.afficher()
    elif (ch == 3):
        M.supprimer()
    elif (ch == 4):
        print("fin de programme")
        break
    else:
        print("ce choix n'est pas disponible")