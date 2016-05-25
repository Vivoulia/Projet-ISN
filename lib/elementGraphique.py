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
      
class TerrainVide(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "vide.gif")
      self.cout = 0
      self.nom = "vide"
      self.description = "Semblable aux grandes steppes de Russie"

class TerrainPlaine(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "plaine.gif")
      self.cout = 0
      self.nom = "Plaine"
      self.description = "Semblable aux grandes steppes de Russie"
      
class TerrainPlaine2(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "plaine2.gif")
      self.cout = 0
      self.nom = "Plaine"
      self.description = "Semblable aux grandes steppes de Russie"
      
class TerrainMontagne(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "montagne.gif")
      self.cout = 2
      self.nom = "Montagne"
      self.description = "Grande montagne, zone de subduction"

class TerrainMontagneBasse(Terrain):
   def __init__(self,x, y, parent):
      Terrain.__init__(self,x, y, parent, "montagneBasse.gif")
      self.cout = 2
      self.nom = "Montagne"
      self.description = "Petite montagne, facile a creuser"

class Entite(ElementJouable):
   def __init__(self, x, y, joueur, parent, textureName, textureDesc="testTuile2D.gif" , cheminTexture = "texture/Entite/", cheminDesc = "texture/Entite/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
      self.vie = 0
      self.joueur = joueur #0: neutre / 1: Joueur 1 / 2: Joueur 2
      self.pa = 0 #Point d'action
      self.attaque = 0
      self.attaqueBatiment = 0
      self.defense = 0
      self.portee = 0
      self.bonusTerrain = 0
      self.typeDegat = 0
      self.level = 0
      self.moove = True
      self.canAttack = True
      self.barreVieContourTkId = None
      self.barreVieTkId = None
      self.soundFile = "son/combat.wave"
      
   def canMoove(self):
      return self.moove

   def setCanAttack(self, canAttack):
      if canAttack:
         self.canAttack = True
      else:
         self.canAttack = False
         self.joueur.addEntiteResetCombat(self)
   
   def setMoove(self, canMoove):
      if canMoove:
         self.moove = True
      else:
         self.moove = False
         self.joueur.addEntiteResetDeplacement(self)
      
   def getSound(self):
      return self.soundFile
         
      
class Epeiste(Entite):
   def __init__(self, x, y, joueur, parent, textureName = "epeiste.gif", textureDesc="testTuile2D.gif"):
      Entite.__init__(self,x, y, joueur, parent, textureName, textureDesc)
      self.vieDepart = 100
      self.vie = self.vieDepart
      self.pa = 4
      self.attaque = 3
      self.attaqueBatiment = 1


class Cavalier(Entite):
   def __init__(self, x, y, joueur, parent, textureName = "epeiste.gif", textureDesc="testTuile2D.gif"):
      Entite.__init__(self,x, y, joueur, parent, textureName, textureDesc)
      self.vieDepart = 100
      self.vie = self.vieDepart
      self.pa = 6
      self.attaque = 3
      self.attaqueBatiment = 1


class Archet(Entite):
   def __init__(self, x, y, joueur, parent, textureName = "epeiste.gif", textureDesc="testTuile2D.gif"):
      Entite.__init__(self,x, y, joueur, parent, textureName, textureDesc)
      self.vieDepart = 100
      self.vie = self.vieDepart
      self.pa = 3
      self.attaque = 3
      self.attaqueBatiment = 1
      

class Batiment(ElementJouable):
   def __init__(self,x, y, joueur, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif", cheminTexture = "texture/Batiment/", cheminDesc = "texture/Batiment/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)
      self.vie = 0
      self.attaque = 0
      self.joueur = joueur
      self.description = "Je suis une structure"
      self.nom = "Je m'apelle rien"
      self.soundFile = None
      
   def getNom(self):
      return self.nom
   
   def getDescription(self):
      return self.description
   
   def getSound(self):
      return self.soundFile   
   
class BatimentSpecial(Batiment):
   #BATIMENT QUI SONT RELIE A DES TUILES (APPELEES TERRITOIRE)
   def __init__(self,x, y, joueur, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif"):
      Batiment.__init__(self, x, y, joueur, parent, textureName, textureDesc)
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
   def getTerritoire(self):
      return self.territoire
   def addTerritoire(self, tuile):
      self.territoire.append(tuile)   

class Mairie(BatimentSpecial):
   def __init__(self, x, y, joueur, parent):
      BatimentSpecial.__init__(self, x, y, joueur, parent, textureName = "ville de base.gif", textureDesc="testTuile2D.gif")
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "Petit village"
      self.nom = "Mairie"
      
   def getTerritoire(self):
      return self.territoire
   
   def addTerritoire(self, tuile):
      self.territoire.append(tuile)
      
class MairieRessource(Mairie):
   def __init__(self, x, y, joueur, parent):
      Batiment.__init__(self, x, y, joueur, parent, textureName = "ville_ressource.gif", textureDesc="testTuile2D.gif")
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "Pour exploiter sans vergogne toutes les ressources disponibles"
      self.nom = "Mairie Ressource"
      self.soundFile = "son/mairie.wav"

class Ferme(BatimentSpecial):
   def __init__(self, x, y, joueur, parent):
      BatimentSpecial.__init__(self, x, y, joueur, parent, textureName = "ferme.gif", textureDesc="testTuile2D.gif")
      self.production = 10
      self.territoire = list() #Tableau contenant les tuiles qui sont reliées a la ville
      self.territoire.append(parent)
      self.description = "100% bio"
      self.nom = "Ferme"
      
class Moulin(Batiment):
   def __init__(self, x, y, joueur, parent):
      Batiment.__init__(self, x, y, joueur, parent, textureName = "moulin.gif", textureDesc="testTuile2D.gif")
      self.production = 0
      self.description = "meunieeeeeer, tu dooooors"
      self.nom = "Moulin"

class Champ(Batiment):
   def __init__(self, x, y, joueur, parent):
      joueur.champs += 1
      Batiment.__init__(self, x, y, joueur, parent, textureName = "champ.gif", textureDesc="testTuile2D.gif")
      self.production = 30
      self.description = "Cool pour planter du ble, des bettraves, des carottes ou de la beuh"
      self.nom = "Champ"
      self.etatAnimation = 0
   
   def etatAvance(self):
      self.etatAnimation += 1
      if self.etatAnimation == 3:
         self.etatAnimation = 0

class Mine(Batiment):
   def __init__(self, x, y, joueur, parent):
      joueur.mines += 1
      Batiment.__init__(self, x, y, joueur, parent, textureName = "mine.gif", textureDesc="testTuile2D.gif")
      self.production = 20
      self.description = "Vous appelez ca une mine ? UNE MINE ?"
      self.nom = "Mine"
      
class Entrepot(Batiment):
   def __init__(self, x, y, joueur, parent):  
      Batiment.__init__(self, x, y, joueur, parent, textureName = "entrepot.gif", textureDesc="testTuile2D.gif")
      joueur.nbMaxRessource += 100
      print(joueur.nbMaxRessource)
      self.description = "Pour ranger des trucs qui prennent trop de place"
      self.nom = "Entrepot"


class Scierie(Batiment):
   def __init__(self, x, y, joueur, parent):
      Batiment.__init__(self, x, y, joueur, parent, textureName = "bucheron.gif", textureDesc="testTuile2D.gif")
      self.production = 10
      self.description = "Un nouveau pouvoir grandit"
      self.nom = "Scierie"
      
class Tour(Batiment):
   def __init__(self, x, y, joueur, parent):
      Batiment.__init__(self, x, y, joueur, parent, textureName = "tour.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."
      self.nom = "Tour"

class TourMage(Batiment):
   def __init__(self, x, y, joueur, parent):
      Batiment.__init__(self, x, y, joueur, parent, textureName = "tour mage.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."
      self.nom = "Tour de Mage"

class Forge(Batiment):
   def __init__(self, x, y, joueur, parent):     
      Batiment.__init__(self, x, y, joueur, parent, textureName = "forge.gif", textureDesc="testTuile2D.gif")
      self.description = "BLING BLING"
      self.nom = "Forge"

class Caserne(Batiment):
   def __init__(self, x, y, joueur, parent):   
      Batiment.__init__(self, x, y, joueur, parent, textureName = "caserne.gif", textureDesc="testTuile2D.gif")
      self.description = "Imposant, mais c'est juste un tas de planches..."
      self.nom = "Caserne"

class Chemin(Batiment):
   def __init__(self, x, y, joueur, parent):
         Batiment.__init__(self, x, y, joueur, parent, textureName = "chemin.gif", textureDesc="testTuile2D.gif")
         joueur.coutChemin += 5
         self.description = "alignement de petits cailloux pour retrouver son chemin"
         self.nom = "Chemin"


class Decor(ElementJouable):
   def __init__(self, x, y, parent, textureName="erreur.gif", textureDesc="testTuile2D.gif", cheminTexture = "texture/Decor/", cheminDesc = "texture/Decor/"):
      ElementJouable.__init__(self, x, y, parent, textureName, textureDesc, cheminTexture, cheminDesc)

class Foret(Decor):
   def __init__(self, x, y, parent):
      Decor.__init__(self, x, y, parent,  "foret.gif", "testTuile2D.gif")

class Ble(Decor):
   def __init__(self, x, y, parent):
      Decor.__init__(self, x, y, parent,  "ble1.gif", "testTuile2D.gif")

class Ble2(Decor):
   def __init__(self, x, y, parent):
      Decor.__init__(self, x, y, parent,  "ble2.gif", "testTuile2D.gif")
      
class CaseSelectionConstruction(ElementGraphique):
   def __init__(self, x, y, parent, textureName, textureDesc="case selection.gif" , cheminTexture = "texture/"):
      ElementGraphique.__init__(self, x, y, parent, textureName, cheminTexture)
   
      
   
"""
class Chemin(Decor):
   def __init__(self, x, y, parent):
      joueur.chemins += 1
      Decor.__init__(self, x, y, parent)
"""
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
      self.tkIdText = None
      
   def event(self):
      pass
   
   def getTexture(self):
      return self.texture
   
   def setTkId(self, identifiant):
      self.tkId = identifiant
      
   def setTkIdText(self, tkId):
      self.tkIdText = tkId
      
   def setIndice(self, indice):
      """DONNE DES COORDONNEES EN FONCTION DE L'INDICE"""
      self.y = 350 + indice*100


class BoutonOuvrier(Bouton):
   def __init__(self, textureName="bouton_ouvrier.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 20
      self.categorie = "amelioration"
      self.description = "recruter un ouvrier"

class BoutonFerme(Bouton):
   def __init__(self, textureName="bouton_ferme.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 30
      self.categorie = "construction"
      self.description = "Construire une ferme"
   def event(self, tuile, joueur):
      ferme = tuile.addBatimentFerme(joueur)
      return ferme

class BoutonForge(Bouton):
   def __init__(self, textureName="bouton_forge.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 20
      self.categorie = "construction"
      self.description = "Construire une forge"
   def event(self, tuile, joueur):
      forge = tuile.addBatimentForge(joueur)
      return forge
   
class BoutonMoulin(Bouton):
   def __init__(self, textureName="bouton_moulin.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 10
      self.categorie = "construction"
      self.description = "Construire un moulin"
   def event(self, tuile, joueur):
      moulin = tuile.addBatimentMoulin(joueur)
      return moulin

class BoutonChemin(Bouton):
   def __init__(self, textureName="bouton_chemin.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 5
      self.categorie = "construction"
      self.description = "Construire un chemin"
   def event(self, tuile, joueur):
      chemin = tuile.addBatimentChemin(joueur)
      return chemin


class BoutonChamp(Bouton):
   def __init__(self, textureName="bouton_champ.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 30
      self.categorie = "construction"
      self.description = "Construire un champ"
   def event(self, tuile, joueur):
      champ = tuile.addBatimentChamp(joueur)
      return champ
   

class BoutonEntrepot(Bouton):
   def __init__(self, textureName="bouton_entrepot.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 20
      self.categorie = "construction"
      self.description = "Construire un entrepot"
   def event(self, tuile, joueur):
      entrepot = tuile.addBatimentEntrepot(joueur)
      return entrepot
      
      
class BoutonMine(Bouton):
   def __init__(self, textureName="bouton_mine.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 40
      self.categorie = "construction"
      self.description = "Construire une mine"
      
   def event(self, tuile, joueur):
      mine = tuile.addBatimentMine(joueur)
      return mine
      
class BoutonScierie(Bouton):
   def __init__(self, textureName="bouton_scierie.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 5
      self.categorie = "construction"
      self.description = "Construire une scierie"
   
   def event(self, tuile, joueur):
      scierie = tuile.addBatimentScierie(joueur)
      return scierie


class BoutonTour(Bouton):
   def __init__(self, textureName="bouton_tour.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 50
      self.categorie = "construction"
      self.description = "Construire une tour"
   
   def event(self, tuile, joueur):
      tour = tuile.addBatimentTour(joueur)
      return tour


class BoutonCaserne(Bouton):
   def __init__(self, textureName="bouton_caserne.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 50
      self.categorie = "construction"
      self.description = "Construire une caserne"

   def event(self, tuile, joueur):
      caserne = tuile.addBatimentCaserne(joueur)
      return caserne

class BoutonRecrutementEpeiste(Bouton):
   def __init__(self, textureName="bouton_recrutement_epeiste.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 60
      self.categorie = "recrutement"
      self.description = "Recruter un epeiste"

   def event(self, tuile, joueur):
      entite = tuile.addEntiteEpeiste(joueur)
      return entite

class BoutonAmeliorationCaserne(Bouton):
   def __init__(self, textureName="bouton_amelioration_caserne.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 100
      self.categorie = "amelioration"
      self.description = "Debloque la caserne"

class boutonAmeliorationTour(Bouton):
   def __init__(self, textureName="bouton_amelioration_tour.gif"):
      Bouton.__init__(self, textureName)
      self.cout = 20
      self.categorie = "amelioration"
      self.description = "Debloque les tours"


class FondRessource(ElementGraphique):
   def __init__(self, x, y, parent, textureName = "barre_ressources.gif", cheminTexture = "texture/GUI/"):  
      ElementGraphique.__init__(self, x, y, parent, textureName, cheminTexture)   

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
      self.effet = "technologie"
      
class Militaire (ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "militaire.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture)
      self.effet = "militaire"

class Magie (ImageAmelioration):
   def __init__(self, x, y, parent, textureName = "magie.gif", cheminTexture = "texture/amelioration/"):
      ImageAmelioration.__init__(self, x, y, parent, textureName, cheminTexture) 
      self.effet = "magie"
