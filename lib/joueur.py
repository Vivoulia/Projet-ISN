class Joueur():
    
    def __init__(self, identifiant):
        self.identifiant = identifiant
        self.xp = 0
        self.nbRessource = 50
        self.villeDepart = None
        self.listAmelioration =[]
        self.champs = 0
        self.mines = 0
        self.scieries = 0
        self.chemins = 0
        self.coutChemins = 10
        self.nbOuvrier = 1
        self.entiteResetDeplacement = list()
        self.entiteResetCombat = list()

    def setVilleDepart(self, ville):
        self.villeDepart = ville
        
    def addEntiteResetDeplacement(self, entite):
        self.entiteResetDeplacement.append(entite)
        
    def addEntiteResetCombat(self, entite):
        self.entiteResetCombat.append(entite)
        
    def getNbRessourceTour(self):
        return 50