from . import fenetre
from . import carte

class GameController():
   def __init__(self):
      self.nbTour = 0
      self.etat = None
      self.joueurActif = None
      self.joueur1 = None
      self.joueur2 = None
   def finTour(self):
      print("fin du tour")
      self.etat = "Fin"
      self.joueurActif.nbRessource += 30
      if "technologie" in self.joueurActif.listAmelioration:
         self.joueurActif.nbRessource += self.joueurActif.champs*15
      else:
         self.joueurActif.nbRessource += self.joueurActif.champs*10
      self.joueurActif.nbRessource += self.joueurActif.mines*20
      self.joueurActif.nbRessource += self.joueurActif.scieries*30
      print(self.joueurActif.nbRessource)
      if self.joueurActif == self.joueur1:
         self.joueurActif = self.joueur2
         print("Au joueur 2 de jouer")
      else:
         self.joueurActif = self.joueur1
         print("Au joueur 1 de jouer")
      self.etat = "En jeu"
   
   def setJoueur(self, joueur1, joueur2):
      self.joueur1 = joueur1
      self.joueur2 = joueur2
      #le joueur 1 commence a jouer
      self.joueurActif = joueur1
      self.etat= "En jeu"
   def getJoueurActif(self):
      return self.joueurActif
      