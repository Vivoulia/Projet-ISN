from . import elementGraphique

class Terrain(ElementGraphique):
   def __init__(self,x, y, parent, texture="erreur.gif"):
      ElementGraphique.__init__(self,x, y, texture, parent)
      self.cout = 0
      self.nom = "Terrain neutre"
   
   def getNom(self):
      return self.nom

class TerrainForet(Terrain):
   def __init__(self,x, y, parent, texture="terrain_foret.gif"):
      Terrain.__init__(self,x, y, parent, texture)
      self.cout = 0
      self.nom = "Foret"
      
class TerrainPlaine(Terrain):
   def __init__(self,x, y, parent, texture="plaine.gif"):
      Terrain.__init__(self,x, y, parent, texture)
      self.cout = 0
      self.nom = "Plaine"
      
class TerrainMontagne(Terrain):
   def __init__(self,x, y, parent, texture="montagne.gif"):
      Terrain.__init__(self,x, y, parent, texture)
      self.cout = 2
      self.nom = "Montagne"