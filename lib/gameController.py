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
      """FONCTION QUI ORGANISE LA FIN DU TOUR"""
      print("fin du tour")
      self.etat = "Fin"
      if self.joueurActif.nbRessource + self.joueurActif.getNbRessourceTour() <= self.joueurActif.nbMaxRessource :
         self.joueurActif.nbRessource += self.joueurActif.getNbRessourceTour()
      else:
         self.joueurActif.nbRessource = self.joueurActif.nbMaxRessource
      print(self.joueurActif.nbRessource)
      if self.joueurActif == self.joueur1:
         self.joueurActif = self.joueur2
         print("Au joueur 2 de jouer")
      else:
         self.joueurActif = self.joueur1
         print("Au joueur 1 de jouer")
      for iEntite in self.joueurActif.entiteResetDeplacement:
         iEntite.setMoove(True)
      for iEntite in self.joueurActif.entiteResetCombat:
         iEntite.setCanAttack(True)             
         
      self.etat = "En jeu"
   
   def setJoueur(self, joueur1, joueur2):
      self.joueur1 = joueur1
      self.joueur2 = joueur2
      #le joueur 1 commence a jouer
      self.joueurActif = joueur1
      self.etat= "En jeu"
      
   def getJoueurActif(self):
      """RENVOIE LE JOUEUR ACTIF"""
      return self.joueurActif
   
   def combat(self, entite1, entite2, gameZone):
      """FONCTION QUI GERE LE COMBAT DE L'ENTITE 1 QUI ATTAQUE L'ENTITE 2"""
      degat = entite1.attaque*(entite1.vie//10)
      degatContrAttaque = entite2.attaque*(entite2.vie//30)
      entite1.setCanAttack(False)
      if entite2.vie - degat <= 0:
         #entite2 contre attaque et meurt
         entite2.parent.removeEntite(entite2)
         gameZone.supprimerEntite(entite2)
      else:
         #entite2 contre attaque et survie
         entite2.vie -= degat
         pass
      #contre attaque
      if entite1.vie - degatContrAttaque <= 0:
         #entite1 meurt
         entite1.parent.removeEntite(entite1)
         gameZone.supprimerEntite(entite1)         
         pass
      else:
         #entite1 un prend des degats et survie
         entite1.vie -= degatContrAttaque
         pass
   