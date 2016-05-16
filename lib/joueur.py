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
        nbOuvriers = 1

    def setVilleDepart(self, ville):
        self.villeDepart = ville