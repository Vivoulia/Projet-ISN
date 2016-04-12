from . import elementGraphique

class Batiment(ElementGraphique):
   def __init__(self, x, y, camp, parent, texture = "erreur.gif"):
      ElementGraphique.__init__(self,x, y, texture, parent)
      self.vie = 0
      self.attaque = 0
      self.camp = camp
      self.description = "Je suis une structure"
      self.nom = "Je m'apelle rien"
   def getNom(self):
      return self.nom
   def getDescription(self):
      return self.description

      
class Mairie(Batiment):
   def __init__(self, x, y, camp, parent, texture = "ville_ressource.gif"):
      Batiment.__init__(self, x, y, camp, parent, texture)
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "Ville de production de ressource"
      self.nom = "Mairie"      
   def upgrade(self):
      if self.nom == "Mairie":
         self.nom = "Palais"
   def getTerritoire(self):
      return self.territoire
   def addTerritoire(self, tuile):
      self.territoire.append(tuile)

  
class Champ(Batiment):
   def __init__(self, x, y, camp, parent, texture = "champ.gif"):
      Batiment.__init__(self, x, y, camp, parent, texture)
      self.description = ""
      self.nom = "Champ"
      

class Mine(Batiment):
   def __init__(self, x, y, camp, parent, texture = "mine.gif"):
      Batiment.__init__(self, x, y, camp, parent, texture)
      self.description = ""
      self.nom = "Mine"


class Scierie(Batiment):
   def __init__(self, x, y, camp, parent, texture = "bucheron.gif"):
      Batiment.__init__(self, x, y, camp, parent, texture)
      self.description = ""
      self.nom = "Scierie"


class Decor(ElementGraphique):
   def __init__(self, x, y, texture, parent):
      ElementGraphique.__init__(self,x, y, texture, parent)