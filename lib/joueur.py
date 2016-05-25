class Joueur():
    
    def __init__(self, identifiant):
        self.identifiant = identifiant
        self.xp = 0
        self.nbRessource = 50000
        self.nbMaxRessource = 100
        self.villeDepart = None
        self.listAmelioration =[]
        self.champs = 0
        self.mines = 0
        self.scieries = 0
        self.chemins = 0
        self.coutChemin = 10
        self.nbOuvrier = 1
        self.entiteResetDeplacement = list()
        self.entiteResetCombat = list()
        self.batimentConstruction = list()
        self.batimentAnimation = list()

    def setVilleDepart(self, ville):
        self.villeDepart = ville

    def addEntiteResetDeplacement(self, entite):
        self.entiteResetDeplacement.append(entite)

    def addEntiteResetCombat(self, entite):
        self.entiteResetCombat.append(entite)

    def addBatimentAnimation(self, batiment):
        self.batimentAnimation.append(batiment)

    def removeBatimentAnimation(self, batiment):
        self.batimentAnimation.remove(batiment)    

    def getNbRessourceTour(self):
        nbRessource = 0
        nbRessource += self.champs*5
        nbRessource += self.mines*10
        nbRessource += self.scieries*5 
        return nbRessource + 10

    def getNbRessource(self):
        return self.nbRessource    