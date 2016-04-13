from random import randint
from . import tuile

COLONNE = 30
LIGNE = 30
TUILE_X = 124
TUILE_Y = 62

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
            alea = randint(0,5)
            x = 590 + (i - j) * (TUILE_X/2)
            y = 100 + (i + j) * (TUILE_Y/2)
            self.terrain[i][j] = tuile.Tuile(x, y, i ,j)
            if alea == 0:
               self.terrain[i][j].setTerrainPlaine()
            elif alea == 1:
               self.terrain[i][j].setTerrainForet()
            elif alea == 2:
               self.terrain[i][j].setTerrainMontagne()
            elif alea == 3:
               self.terrain[i][j].setTerrainPlaine()
            elif alea == 4:
               self.terrain[i][j].setTerrainPlaine()
            elif alea == 5:
               self.terrain[i][j].setTerrainPlaine()


            self.fenetre.gameZone.afficherElement(self.terrain[i][j].terrain)
            if self.terrain[i][j].getTerrain().getNom() == "Foret":
               self.terrain[i][j].addDecorForet()
               self.fenetre.gameZone.afficherElement(self.terrain[i][j].decor[len(self.terrain[i][j].decor)-1])   
            #self.fenetre.can.update()
      #On définit les deux villes de depart et on les assignent au joueur:
      self.terrain[1][1].addBatimentMairieRessource(self.joueur1)
      self.joueur1.setVilleDepart(self.terrain[1][1].getBatiment())
      self.fenetre.gameZone.afficherElementIndex(self.terrain[1][1].getBatiment())
      
      self.terrain[20][20].addBatimentMairieRessource(self.joueur2)
      self.joueur2.setVilleDepart(self.terrain[20][20].getBatiment())  
      self.fenetre.gameZone.afficherElementIndex(self.terrain[20][20].getBatiment())
      
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