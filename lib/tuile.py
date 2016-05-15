from tkinter import *
from . import elementGraphique

class Tuile():
   def __init__(self,x ,y, i, j):
      self.x = x
      self.y = y
      self.i = i
      self.j = j
      self.tkId = 0
      self.batiment = None #Un seul batiment sur chaque tuile
      self.terrain = None #Un seul terrain sur chaque tuile
      self.decor = list() #Plusieurs decors sur chaque tuile
      self.entite = list()

   def setTkId(self, identifiant):
      self.tkId = identifiant

   def setTerrainForet(self):
      self.terrain = elementGraphique.TerrainForet(self.x, self.y, self)
      return self.terrain
   
   def setTerrainPlaine(self):
      self.terrain = elementGraphique.TerrainPlaine(self.x, self.y, self)
      return self.terrain
      
   def setTerrainMontagne(self):
      self.terrain = elementGraphique.TerrainMontagne(self.x, self.y, self)
      return self.terrain

   def addBatimentMairie(self, camp):
      self.batiment = elementGraphique.Mairie(self.x, self.y, camp, self)
      return self.batiment
   
   def addBatimentMairieRessource(self, camp):
      self.batiment = elementGraphique.MairieRessource(self.x, self.y, camp, self)
      return self.batiment
   
   def addBatimentChemin(self, camp):
         self.batiment = elementGraphique.Chemin(self.x, self.y, camp, self)
         return self.batiment   

   def addBatimentChamp(self, camp):
      self.batiment = elementGraphique.Champ(self.x, self.y, camp, self)
      return self.batiment

   def addBatimentScierie(self, camp):
      self.batiment = elementGraphique.Scierie(self.x, self.y, camp, self)
      return self.batiment

   def addBatimentReservoir(self, camp):
      self.batiment = elementGraphique.Reservoir(self.x, self.y, camp, self)
      return self.batiment

   def addBatimentMine(self, camp):
      self.batiment = elementGraphique.Mine(self.x, self.y, camp, self)
      return self.batiment
      
   def addBatimentEntrepot(self, camp):
      self.batiment = elementGraphique.Entrepot(self.x, self.y, camp, self)
      return self.batiment
      
   def addBatimentTour(self, camp):
      self.batiment = elementGraphique.Tour(self.x, self.y, camp, self)
      return self.batiment
      
   def addBatimentTourMage(self, camp):
      self.batiment = elementGraphique.TourMage(self.x, self.y, camp, self)
      return self.batiment
      
   def addBatimentForge(self, camp):
      self.batiment = elementGraphique.Forge(self.x, self.y, camp, self)
      return self.batiment
   
   def addBatimentCaserne(self, camp):
      self.batiment = elementGraphique.Caserne(self.x, self.y, camp, self) 
      return self.batiment

   def addDecorForet(self):
      self.decor.append(elementGraphique.Foret(self.x, self.y, self))
   
   def addEntiteEpeiste(self, camp):
      self.entite.append(elementGraphique.Epeiste(self.x, self.y, camp, self))
      return self.entite[0]
   
   def getBatiment(self):
      return self.batiment
   
   def getDecor(self):
      return self.decor
   
   def getTerrain(self):
      return self.terrain
   
   def getEntite(self):
      return self.entite
