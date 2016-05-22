from random import randint
from . import tuile

COLONNE = 32
LIGNE = 32
TUILE_X = 124
TUILE_Y = 62
marge = 5
"COORDS DES VILLES"
x1 = 6
y1 = 23
x2 = 22
y2 = 7
x1 = 10
y1 = 21
x2 = 21
y2 = 10
class Carte():

   def __init__(self):
      #GENERATION MAP
      self.terrain = [[0] * COLONNE for _ in range(LIGNE)]
      self.fenetre = None
      self.joueur1 = None
      self.joueur2 = None

   def load(self):
      """GENERE LA CARTE DE JEU ET L'AFFICHE"""
      x = 0
      y = 0
      texture = ""
      for i in range(LIGNE):
         for j in range(COLONNE):
            x = 590 + (i - (j+1)) * (TUILE_X/2)
            y = 100 + (i + (j+1)) * (TUILE_Y/2)
            self.terrain[i][j] = tuile.Tuile(x, y, i ,j)
            if i<=2 or j<=2 or i>=LIGNE-3 or j>=COLONNE-3 or i + j > COLONNE+15  or i + j < COLONNE-20:
               self.terrain[i][j].setTerrainVide()
            elif i < marge or j < marge or i >= LIGNE-marge or j >= COLONNE-marge or (i+j > COLONNE+14-marge) or (i + j < COLONNE-19+marge):
               self.terrain[i][j].setTerrainMontagne()
            elif i == marge or j == marge or i == LIGNE-marge-1 or j == COLONNE-marge-1 or (i+j == COLONNE+14-marge) or i + j == COLONNE-19+marge:
               alea = randint(1,4)
               if alea != 1:
                  self.terrain[i][j].setTerrainMontagneBasse()
               elif alea == 3:
                  self.terrain[i][j].setTerrainForet()
               else:
                  self.terrain[i][j].setTerrainPlaine()
            else:
               alea = randint(0,5)
               if alea <= 4:
                  self.terrain[i][j].setTerrainPlaine()
               else:
                  self.terrain[i][j].setTerrainForet()


            self.fenetre.gameZone.afficherElement(self.terrain[i][j].terrain)
            if self.terrain[i][j].getTerrain().getNom() == "Foret":
               self.terrain[i][j].addDecorForet()
               self.fenetre.gameZone.afficherElement(self.terrain[i][j].decor[len(self.terrain[i][j].decor)-1])
      
            #self.fenetre.can.update()
      #On définit les deux villes de depart et on les assignent au joueur:
      self.terrain[x1][y1].addBatimentMairieRessource(self.joueur1)
      self.joueur1.setVilleDepart(self.terrain[x1][y1].getBatiment())
      self.fenetre.gameZone.afficherElementIndex(self.terrain[x1][y1].getBatiment())

      self.terrain[x2][y2].addBatimentMairieRessource(self.joueur2)
      self.joueur2.setVilleDepart(self.terrain[x2][y2].getBatiment())  
      self.fenetre.gameZone.afficherElementIndex(self.terrain[x2][y2].getBatiment())
   
      #self.fenetre.afficherElement(self.terrain[i][j])
   def setFenetre(self, fenetre):
      self.fenetre = fenetre

   def setJoueur(self, joueur1, joueur2):
      self.joueur1 = joueur1
      self.joueur2 = joueur2

   def getNbColonne(self):
      return COLONNE

   def getNbLigne(self):
      return LIGNE