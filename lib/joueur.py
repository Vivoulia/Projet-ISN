class Joueur():
    
    def __init__(self, identifiant):
        self.identifiant = identifiant
        self.nbRessource = 10
        self.expTechnologie = 0
        self.expMilitaire = 0
        self.villeDepart = None
    def setVilleDepart(self, ville):
        self.villeDepart = ville