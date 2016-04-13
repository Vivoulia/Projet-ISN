from tkinter import *

class ElementGraphique():
   def __init__(self, x, y, parent, textureName = "erreur.gif", cheminTexture = "texture/"):
      self.x = x
      self.y = y
      self.zindex = 0
      self.cheminTexture = cheminTexture
      self.textureName = textureName
      self.fileNameTexture=self.cheminTexture + self.textureName
      self.texture = PhotoImage(file = self.fileNameTexture)    
      self.tkId = 0
      self.parent = parent
      
   def setTkId(self, identifiant):
      self.tkId = identifiant
   
   def getTexture(self):
      return self.texture

class ElementJouable(ElementGraphique):
   def __init__(self, x, y, parent, textureName, textureDesc="testTuile2D.gif" , cheminTexture = "texture/", cheminDesc = "texture/"):
      ElementGraphique.__init__(self, x, y, parent, textureName, cheminTexture)
      self.cheminDesc = cheminDesc
      self.textureDesc = textureDesc
      self.fileNameDesc= self.cheminDesc + self.textureDesc
      self.descImage = PhotoImage(file = self.fileNameDesc)
	  
class Terrain(ElementJouable):
   def __init__(self,x, y, parent, textureName, textureDesc="testTuile2D.gif", cheminTexture = "texture/Terrain/", cheminDesc = "texture/Terrain/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
      self.cout = 0
      self.nom = "Terrain neutre"
      self.description = "Je ne suis rien"
   
   def getNom(self):
      return self.nom
   
   def getDescription(self):
      return self.description

class TerrainForet(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "terrain_foret.gif")
      self.cout = 0
      self.nom = "Foret"
      self.description = "Foret dense, a eviter si vous etes une petite fille a capuche rouge"
      
class TerrainPlaine(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "plaine.gif")
      self.cout = 0
      self.nom = "Plaine"
      self.description = "Seimblable aux grandes steppes de Russie"
      
class TerrainMontagne(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "montagne.gif")
      self.cout = 2
      self.nom = "Montagne"
      self.description = "Grande montagne, zone de subduction"

class Entite(ElementJouable):
   def __init__(self,x, y, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif", cheminTexture = "texture/Entite/", cheminDesc = "texture/Entite/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
      self.vie = vie
      self.camp = camp #0: neutre / 1: Joueur 1 / 2: Joueur 2
      self.pa #Point d'action
      self.attaque 
      self.defense
      self.portee 
      self.bonusTerrain
      self.typeDegat 
      self.level

      
class Batiment(ElementJouable):
   def __init__(self,x, y, camp, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif", cheminTexture = "texture/Batiment/", cheminDesc = "texture/Batiment/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
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
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "ville de base.gif", textureDesc="testTuile2D.gif")
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "Petit village"
      self.nom = "Mairie"      
   def getTerritoire(self):
      return self.territoire
   def addTerritoire(self, tuile):
      self.territoire.append(tuile)
      
class MairieRessource(Mairie):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "ville_ressource.gif", textureDesc="testTuile2D.gif")
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "Pour exploiter sans vergogne toutes les ressources disponibles"
      self.nom = "Mairie Ressource"      
   def upgrade(self):
      if self.nom == "Mairie":
         self.nom = "Palais"

class Champ(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "champ.gif", textureDesc="testTuile2D.gif")
      self.production = 10
      self.description = "Cool pour planter du ble, des bettraves, des carottes ou de la beuh"
      self.nom = "Champ"

class Mine(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "mine.gif", textureDesc="testTuile2D.gif")
      self.production = 10
      self.description = "Vous appelez ca une mine ? UNE MINE ?"
      self.nom = "Mine"
      
class Entrepot(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "entrepot.gif", textureDesc="testTuile2D.gif")
      self.stockage = 10
      self.description = "Pour ranger des trucs qui prennent trop de place"
      self.nom = "Entrepot"

class Reservoir(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "reservoir.gif", textureDesc="testTuile2D.gif")
      self.stockage = 10
      self.description = "Pour ranger des trucs qui prennent trop de place"
      self.nom = "Entrepot"

class Scierie(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "bucheron.gif", textureDesc="testTuile2D.gif")
      self.production = 10
      self.description = "Un nouveau pouvoir grandit"
      self.nom = "Scierie"
      
class Tour(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "tour.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."

class TourMage(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "tour mage.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."

class Forge(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "forge.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."

class Caserne(Batiment):
   def __init__(self, x, y, camp, parent):
      Batiment.__init__(self, x, y, camp, parent, textureName = "caserne.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."


class Decor(ElementJouable):
   def __init__(self,x, y, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif", cheminTexture = "texture/Decor/", cheminDesc = "texture/Decor/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
      
class Foret(Decor):
   def __init__(self, x, y, parent):
      Decor.__init__(self, x, y, parent,  "foret.gif", "testTuile2D.gif")
      
      
""" ELEMENT INTERFACE UTILISASATEUR """

class Bouton(ElementGraphique):
   def __init__(self, textureName, cheminTexture = "texture/GUI/"):
      parent = None #a supprimers
      self.x = 20
      self.y = 350
      self.indice = 0
      ElementGraphique.__init__(self, self.x, self.y, parent, textureName, cheminTexture)
      self.nom = "Bouton"
      self.description = "Description Au survol de la souris"
      self.tkId = None
      
   def event(self):
      pass
   
   def getTexture(self):
      return self.texture
   
   def setTkId(self, identifiant):
      self.tkId = identifiant
      
   def setIndice(self, indice):
      """DONNE DES COORDONNEES EN FONCTION DE L'INDICE"""
      self.y = 350 + indice*100

class BoutonChamp(Bouton):
   def __init__(self, textureName="bouton_illustration_champ.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentChamp(camp)
      

class BoutonEntrepot(Bouton):
   def __init__(self, textureName="bouton_illustration_entrepot.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentEntrepot(camp)
      
      
class BoutonMine(Bouton):
   def __init__(self, textureName="bouton_illustration_mine.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentMine(camp)

      
class BoutonScierie(Bouton):
   def __init__(self, textureName="bouton_illustration_scierie.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentScierie(camp)


class BoutonTour(Bouton):
   def __init__(self, textureName="bouton_illustration_tour.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentTour(camp)


class BoutonCaserne(Bouton):
   def __init__(self, textureName="bouton_illustration_caserne.gif"):
      Bouton.__init__(self, textureName)
   
   def event(self, tuile, camp):
      tuile.addBatimentCaserne(camp)


class ImageAmelioration(ElementGraphique):
   def __init__(self, x, y, parent, textureName, cheminTexture = "texture/amelioration/"):  
      ElementGraphique.__init__(self, x, y, parent, textureName, cheminTexture)

class Fond(ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "fond.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture)

class Cadre(ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "cadre bis.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture)
      
class Technologie(ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "technologie.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture)
      self.effet = "vroum"
      
class Militaire (ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "militaire.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture)
      self.effet = "panpan"

class Magie (ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "magie.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture) 
      self.effet = "abracadabra"