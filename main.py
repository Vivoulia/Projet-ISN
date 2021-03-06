from lib import carte
from lib import fenetre
from lib import gameController
from lib import joueur
from lib import son

class Game():
   def __init__(self):
      self.sonManager = son.SonManager()
      #self.sonManager.playSonFond()      
      self.carte = carte.Carte()
      self.gameController = gameController.GameController()
      self.joueur1 = joueur.Joueur(1)
      self.joueur2 = joueur.Joueur(2)
      self.gameController.setJoueur(self.joueur1, self.joueur2)
      self.carte.setJoueur(self.joueur1, self.joueur2)
      self.fenetre = fenetre.Fenetre(self.gameController, self.sonManager)
      self.carte.setFenetre(self.fenetre)
      self.fenetre.setCarte(self.carte)

   def loadMap(self):
      self.carte.load()
   def loadFenetre(self):
      self.fenetre.load()

if __name__ == "__main__":
      game = Game()
      game.loadMap()
      game.loadFenetre()
      
      game.sonManager.closeAll()