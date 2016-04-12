from . import elementGraphique

class Entite(ElementGraphique):
   def __init__(self):
      ElementGraphique.__init_(self, x, y, texture, parent)
      self.vie = vie
      self.camp = camp #0: neutre / 1: Joueur 1 / 2: Joueur 2
      self.pa #Point d'action
      self.attaque 
      self.defense
      self.portee 
      self.bonusTerrain
      self.typeDegat 
      self.level