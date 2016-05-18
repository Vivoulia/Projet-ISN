from tkinter import *
from . import elementGraphique
from . import joueur
from random import *

MARGE_Y = 50
MARGE_X = 10 

TUILE_X = 124
TUILE_Y = 62

class ZoneAffichage(Canvas):
   def __init__(self, widgetParent, fenetre, background, width, height):
      Canvas.__init__(self, widgetParent, bg=background, width=width, height=height)
      self.parent = widgetParent
      self.fenetre = fenetre      

   def afficherElement(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE ENVOYE EN PARAMETRE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW) 
      element.setTkId(tkId)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onTuileClick)  
      self.update()

   def afficherElementIndex(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE EN GERANT L'AFFICHAGE DEVANT/DESSUS"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW) 
      element.setTkId(tkId)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onTuileClick)
      i, j = self.translateToIso(element.x, element.y)
      #il faut verifier si terrain[i][j] existe (A FAIRE)
      self.tag_lower(tkId, self.fenetre.carte.terrain[i][j].terrain.tkId)
      self.update()   

class GameZone(ZoneAffichage):
   
   def __init__(self, widgetParent, fenetre, background, width, height):
      ZoneAffichage.__init__(self, widgetParent, fenetre, background, width, height)
      self.parent = widgetParent
      self.fenetre = fenetre
      self.currentCity = None
      self.currentTuile = None
      self.selectedTuile = list() #List contenant les tuiles selectionné par un clique
      self.selectedTkId = list() #List contenant les TkId selectionné par un clique 
      
      
   def afficherElement(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE ENVOYE EN PARAMETRE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW)
      element.setTkId(tkId)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onTuileClick)
      self.update()
   
   def afficherElementIndex(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE EN GERANT L'AFFICHAGE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW) 
      element.setTkId(tkId)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onTuileClick)
      i, j = self.translateToIso(element.x, element.y)
      #il faut verifier si terrain[i][j] existe (A FAIRE)
      self.tag_lower(tkId, self.fenetre.carte.terrain[i][j].terrain.tkId)
      self.update()
   
   def selectTuile(self, selection):
      """AFFICHE LES TUILES ENVOYE DANS UNE LIST EN PARAMETRE"""
      fileName="texture/case selection.gif"
      self.photo = PhotoImage(file = fileName)
      for iTuile in range(len(selection)):
         i, j = self.translateToIso(selection[iTuile].x, selection[iTuile].y)
<<<<<<< HEAD
=======
         print("i :",i, "j :", j )
>>>>>>> origin/master
         tkId = self.create_image(selection[iTuile].x, selection[iTuile].y, image=self.photo,  anchor=SW)
         self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onTuileClick)
         if selection[iTuile].getBatiment() != None:
            self.tag_lower(tkId, self.fenetre.carte.terrain[i][j].getBatiment().tkId)
         elif len(selection[iTuile].getDecor()) != 0:
            decor = selection[iTuile].getDecor()
            self.tag_lower(tkId, decor[0].tkId)
         else:
            self.tag_lower(tkId, self.fenetre.carte.terrain[i][j].getTerrain().tkId)
         self.selectedTkId.append(tkId)
         self.update()
   
   def deselect(self):
      """DESAFFICHE ET DESELECTIONNE LES TUILES SELECTIONNE"""
      for iTkId in range(len(self.selectedTkId)):
         self.delete(self.selectedTkId[iTkId])
      self.selectedTuile = list()
      
   def getSelectedTuile(self):
      return self.selectedTuile
   
   def addSelectedTuile(self, tuile):
      self.selectedTuile.append(tuile)
   
   def currentTuile(self):
      return self.currentTuile

   def selectTerritoire(self, tuile):
      pass

   def selectTerritoireMairie(self, tuile):
      """SELECTIONNE LES TERRITOIRES D'UNE MAIRIE ET AFFICHE A LA FENETRE LA ZONE DE SELECTION"""
      self.deselect()
      for territoire in tuile.getBatiment().getTerritoire():
         territoireVoisin = self.getVoisin(territoire)
         for iVoisin in territoireVoisin:
            if iVoisin.getBatiment() == None:
               self.selectedTuile.append(iVoisin)
      self.selectTuile(self.selectedTuile)

   def selectTerritoireEntite(self, tuile):
      """SELECTIONNE LES TERRITOIRES Q'UNE ENTITE PEUT PARCOURIR ET AFFICHE A LA FENETRE LA ZONE DE SELECTION"""
      self.deselect()
<<<<<<< HEAD
      Q = list()
      Q.append(tuile)
      entite = tuile.getEntite()
      self.deselect()

      for _ in range(entite[0].pa):
         for iTuile in Q:
            n = Q.pop()
            voisin = self.getVoisin(n)
            for iVoisin in voisin:
               self.selectedTuile.append(iVoisin)
               Q.append(iVoisin)
      self.selectTuile(self.selectedTuile)
=======
      entite = tuile.getEntite()
      if entite[0].canMoove():
         Q = Queue()
         Q.put(tuile)
         i = 0
         closed = list()
         closed.append(tuile)
         print("nb Tuile a parcourir:", entite[0].pa*(2*(entite[0].pa + 1)))
         while not(Q.empty()) and i < entite[0].pa*(2*(entite[0].pa + 1)):
            n = Q.get()
            territoireVoisin, nbVoisin = self.getVoisinComptage(n)
            print("On incremente i de : ", nbVoisin)
            i += nbVoisin
            for iVoisin in territoireVoisin:
               if not(iVoisin in closed):
                  Q.put(iVoisin)
                  self.selectedTuile.append(iVoisin)
                  closed.append(iVoisin)
                  #i += 1
               else:
                  i-=1
         self.selectTuile(self.selectedTuile, "case selection entite.gif")
         self.selectionType = "Entite"
         print("nbTuileParcouru :", i)
>>>>>>> origin/master

   def translateToIsoScroll(self, x, y):
      """TRANSLATE DES COORDONNEES X, Y EN COORDS ISOMETRIQUE"""
      sreenX = self.canvasx(x) - 590
      sreenY  = self.canvasy(y) - 100
      x = (sreenY / TUILE_Y) + (sreenX/TUILE_X)
      y = (sreenY / TUILE_Y) - (sreenX/TUILE_X)
      return round(x), round(y)+1

   def translateToIso(self, x, y):
      """TRANSLATE DES COORDONNEES X, Y EN COORDS ISOMETRIQUE"""
      sreenX = x - 590 
      sreenY  = y - 100         
      x = (sreenY / TUILE_Y) + (sreenX/TUILE_X)
      y = (sreenY / TUILE_Y) - (sreenX/TUILE_X)
      return round(x), round(y)+1  
      
   def getVoisin(self, tuile):
      """RENVOIE LES VOISINS D'UNE TUILE"""
      voisin = list()
      colonne = self.fenetre.carte.getNbColonne()
      ligne = self.fenetre.carte.getNbLigne()
      for i in range(-1, 2, 1):
         if i != 0:
            if (tuile.i+i <= ligne and tuile.i+i >= 0) and (tuile.j+i <= colonne and tuile.j+i >= 0):
               voisin.append(self.fenetre.carte.terrain[tuile.i+i][tuile.j])
               voisin.append(self.fenetre.carte.terrain[tuile.i][tuile.j+i])
      return voisin
   
<<<<<<< HEAD
=======
   def getVoisinComptage(self, tuile):
      """RENVOIE LES VOISINS D'UNE TUILE EN COMPTANT LES VOISINS THEORIQUENT"""
      voisin = list()
      colonne = self.fenetre.carte.getNbColonne()
      ligne = self.fenetre.carte.getNbLigne()
      nbVoisin = 0
      for i in range(-1, 2, 1):
         if i != 0:
            if (tuile.i+i < ligne and tuile.i+i >= 0) and (tuile.j+i < colonne and tuile.j+i >= 0):
               voisin.append(self.fenetre.carte.terrain[tuile.i+i][tuile.j])
               voisin.append(self.fenetre.carte.terrain[tuile.i][tuile.j+i])
               nbVoisin += 2
            else:
               nbVoisin += 2
               print("on passe ici")
      return voisin, nbVoisin
   
   def moveUnitTo(self, tuile):
      self.coords(self.currentEntite.tkId, tuile.x, tuile.y)
      i, j = self.translateToIso(tuile.x, tuile.y)
      self.tag_lower(self.currentEntite.tkId, self.fenetre.carte.terrain[i][j].terrain.tkId)
      self.update()
      self.currentEntite.parent.removeEntite(self.currentEntite)
      tuile.addEntite(self.currentEntite)
      self.currentEntite.parent = tuile
      self.currentEntite.setMoove(False)
      
   def tuileExiste(self, tuile):
      if (tuile.i < ligne and tuile.i > 0) and (tuile.j < colonne and tuile.j > 0):
         return True
      else:
         return False
   
>>>>>>> origin/master

class UserInterface(Canvas):
   def __init__(self, widgetParent, fenetre, background, width, height):
      Canvas.__init__(self, widgetParent, bg=background, width=width, height=height)
      self.parent = widgetParent
      self.fenetre = fenetre
      
      """ CREATION DE LA ZONE D'INFORMATION """
      
      self.descriptionTexte = StringVar()
      self.descriptionTexte.set("Aucune Tuile")
      self.description = Label(self.parent, textvariable=self.descriptionTexte)
      #self.description.pack()
      self.create_text(50,50, text="Test")
      fileName="texture/GUI/fond descritpion.gif"
      self.fondDescription = PhotoImage(file = fileName)
      self.create_image(0,996, image=self.fondDescription, anchor=SW)

      """ BOUTON """
      
      self.boutonListe = list()
      self.boutonTour = elementGraphique.BoutonTour()
      self.boutonChamp = elementGraphique.BoutonChamp()
      self.boutonEntrepot = elementGraphique.BoutonEntrepot()
      self.boutonMine = elementGraphique.BoutonMine()
      self.boutonScierie = elementGraphique.BoutonScierie()
      self.boutonCaserne = elementGraphique.BoutonCaserne()
      self.boutonChemin = elementGraphique.BoutonChemin()
      self.boutonOuvrier = elementGraphique.BoutonOuvrier()
      self.boutonRecrutementEpeiste = elementGraphique.BoutonRecrutementEpeiste()
      self.boutonListe.append(self.boutonTour)
      self.boutonListe.append(self.boutonChamp)
      self.boutonListe.append(self.boutonEntrepot)
      self.boutonListe.append(self.boutonMine)
      self.boutonListe.append(self.boutonScierie)
      self.boutonListe.append(self.boutonCaserne)
      self.boutonListe.append(self.boutonChemin)
      self.boutonListe.append(self.boutonRecrutementEpeiste)
      self.boutonListe.append(self.boutonOuvrier)
      
   def afficherBouton(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE ENVOYE EN PARAMETRE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW)
      tkIdText = self.create_text(element.x, element.y+10, text=element.description, anchor=SW)
      element.setTkId(tkId)
      element.setTkIdText(tkIdText)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onBoutonClique)  
      self.update()
   
   def affichegeBoutonMairie(self, tuile):
      self.boutonOuvrier.setIndice(0)
      self.afficherBouton(self.boutonOuvrier)  
   
   def affichageBoutonChantier(self, tuile):
      if tuile.getBatiment() == None:
         if tuile.getTerrain().getNom() == "Foret":
            self.boutonScierie.setIndice(0)
            self.afficherBouton(self.boutonScierie)
         elif tuile.getTerrain().getNom() == "Montagne":
            self.boutonMine.setIndice(0)
            self.afficherBouton(self.boutonMine)
         elif tuile.getTerrain().getNom() == "Plaine":
            self.boutonTour.setIndice(0)
            self.boutonChamp.setIndice(1)
            self.boutonEntrepot.setIndice(2)
<<<<<<< HEAD
            self.boutonChemin.setIndice(3)
            self.boutonCaserne.setIndice(4)
=======
            if "militaire" in self.fenetre.gameController.getJoueurActif().listAmelioration :
               self.boutonCaserne.setIndice(3)
               self.boutonChemin.setIndice(4)
            else:
               self.boutonChemin.setIndice(3)
               self.boutonCaserne.setIndice(4)
               self.afficherBouton(self.boutonCaserne)
>>>>>>> origin/master
            self.afficherBouton(self.boutonTour)
            self.afficherBouton(self.boutonChamp)
            self.afficherBouton(self.boutonEntrepot)
            self.afficherBouton(self.boutonChemin)
            joueurActif = self.fenetre.gameController.getJoueurActif()
            if "militaire" in joueurActif.listAmelioration :
               self.afficherBouton(self.boutonCaserne)
      else:
         if tuile.getBatiment().getNom() == "Caserne":
            self.boutonRecrutementEpeiste.setIndice(0)
            self.afficherBouton(self.boutonRecrutementEpeiste)
         pass
      
   
   def affichageInformation(self):
      """ METHODE QUI AFFICHE LES INFORMATION SUR UNE CASE """
      pass
   
   def clear(self):
      for iBouton in self.boutonListe:
         self.delete(iBouton.tkId)
         self.delete(iBouton.tkIdText)

class ArbreCompetence(Canvas):
  
   def __init__(self, widgetParent, fenetre, background, width, height):
      Canvas.__init__(self, widgetParent, bg=background, width=width, height=height)
      self.fenetre = fenetre
      self.availableList = list()
      self.unlockedList = list()
      self.fond = elementGraphique.Fond(30, 3000, self)
      self.technologie = elementGraphique.Technologie(210, 330, self)
      self.militaire = elementGraphique.Militaire(450, 190, self)
      self.magie = elementGraphique.Magie(710, 330, self)
      self.availableList.append(self.militaire)
      self.availableList.append(self.technologie)
      self.availableList.append(self.magie)
      self.afficherArbre()

   def afficherArbre(self):
      print("affichage arbre de competence")
      self.croll = 0
      self.create_image(self.fond.x, self.fond.y, image = self.fond.getTexture(), anchor=SW)
      for amelioration in self.availableList :
         self.afficherElement(amelioration)
      #for cadre in self.unlockedList:
      #   self.afficherElement(cadre)

   def afficherElement(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE ENVOYE EN PARAMETRE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW) 
      element.setTkId(tkId)
      self.tag_bind(tkId, '<ButtonPress-1>', self.fenetre.onArbreClick)
      self.update()

class RessourceInterFace(Canvas):
   def __init__(self, widgetParent, fenetre, background, width, height):
      Canvas.__init__(self, widgetParent, bg=background, width=width, height=height)
      self.parent = widgetParent
      self.fenetre = fenetre
      self.ressource = self.create_text(30,10, text="Ressource")
      fondRessource = elementGraphique.FondRessource(30, 10, self)
      print("affichage de la barre de ressources")
      self.afficherElement(fondRessource)
      
   def afficherElement(self, element):
      """AFFICHE UN OBJET DE TYPE ELEMENT GRAPHIQUE ENVOYE EN PARAMETRE"""
      tkId = self.create_image(element.x, element.y, image=element.getTexture(), anchor=SW) 
      element.setTkId(tkId)
      self.update()

class Fenetre():
   def __init__(self):
      self.windows = Tk()
      width, height = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
      self.windows.bind('<KeyPress>', self.onKeyPress)
      self.windows.bind('<MouseWheel>', self.onKeyPress)
      
      """CREATTION DE LA ZONE DE JEU (canvas)"""

      self.zone_jeu = Frame(self.windows)
      self.gameZone = GameZone(self.zone_jeu, self, "blue",width-300, height-100)
      self.gameZone.scale("all", 0, 0, 3 ,3)
      self.gameZone.grid(column=0, row=0)
      #self.zone_jeu.pack(side=LEFT,fill=Y)
      self.zone_jeu.grid(column=0, row=0)

      """CREATION DE L'INTERFACE UTILISATEUR"""
      
      self.zone_description = Frame(self.windows)
      self.userInterface = UserInterface(self.zone_description, self, "brown", width=250, height=height-100)
      self.userInterface.grid(column=0, row=0)
      self.zone_description.grid(column=2, row=0)
      self.finTour = Button(self.zone_description, text="Fin du Tour")
      self.finTour.grid(column=0, row=1)
      
      """CREATION DE LA ZONE RESSOURCE"""
      
      self.zone_ressource = Frame(self.windows)
      self.ressourceInterFace = RessourceInterFace(self.zone_ressource, self, "white", width=TUILE_X*9+MARGE_X, height=80)
      self.ressourceInterFace.grid(column=0, row=0)
      self.zone_ressource.grid(column=0, row=2)

      """CREATION DE L'ARBRE DE COMPETENCE"""
      
      self.arbre_competence = Frame(self.zone_jeu)
      self.arbreCompetence = ArbreCompetence(self.arbre_competence, self, "brown",width-300, height-100)
      self.arbreCompetence.grid(column=0, row=0)
      self.arbre_competence.grid(column=0, row=0)
      self.arbre_competence.grid_forget()
      self.afficherArbre = False
      
      """VARIABLE"""
      
      self.carte = None
      self.gameController = None
      self.currentTuile = None
      self.selectedTuile = list() #List contenant les tuiles selectionné par un clique
      self.selectedTkId = list() #List contenant les TkId selectionné par un clique
      
   def load(self):
      self.windows.mainloop()

   def setCarte(self, carte):
      self.carte = carte

   def setGameController(self, gameController):
      self.gameController = gameController
      self.finTour.config(command=self.gameController.finTour)
      
   """   EVENT  """
   
   def onTuileClick(self, event):
      x, y = self.gameZone.translateToIsoScroll(event.x, event.y)
      self.userInterface.clear()
      self.gameZone.currentTuile = self.carte.terrain[x][y]
      if len(self.carte.terrain[x][y].getEntite()) > 0  :
         #Il y a des entités sur la tuile
         entite = self.carte.terrain[x][y].getEntite()
         self.gameZone.selectTerritoireEntite(self.carte.terrain[x][y])
         print(entite[0].pa)
         pass
      
      elif self.carte.terrain[x][y].getBatiment() != None:
         #Il y a un batiment sur la tuile
         if self.gameController.getJoueurActif() == self.carte.terrain[x][y].getBatiment().joueur:
            if self.carte.terrain[x][y].getBatiment().getNom() == "Mairie Ressource":
               #si le batiment est une mairie
               self.userInterface.affichegeBoutonMairie(self.carte.terrain[x][y])
               self.gameZone.currentCity = self.carte.terrain[x][y]
               #on met en selection les zones constructibles
               self.gameZone.selectTerritoireMairie(self.carte.terrain[x][y])
            else:
               self.userInterface.clear()
               self.userInterface.affichageBoutonChantier
         else:
            pass
            
            pass
      else:
         #Il y a juste un terrain sur la tuile
         if self.carte.terrain[x][y] in self.gameZone.selectedTuile:
            #Affichage des boutons 
            self.userInterface.clear()
            self.userInterface.affichageBoutonChantier(self.carte.terrain[x][y])
         elif len(self.gameZone.selectedTkId) != 0:
            self.gameZone.deselect()
            self.userInterface.clear()
            #self.description
            
   def onArbreClick(self, event):
      """ CLIC DANS L'ARBRE DES COMPETENCES """
      item = event.widget.find_closest(event.x, event.y)
      for iAmelioration in self.arbreCompetence.availableList:
         if iAmelioration.tkId == item[0]:
            x = iAmelioration.x
            y = iAmelioration.y
            self.arbreCompetence.cadre = elementGraphique.Cadre(x, y, ArbreCompetence)
            self.arbreCompetence.unlockedList.append(self.arbreCompetence.cadre)
            self.arbreCompetence.afficherElement(self.arbreCompetence.cadre)
            print (self.arbreCompetence.unlockedList)
            print (iAmelioration.effet)
            #Debloquer les ameliorations suivantes
            upgrade = iAmelioration.effet
            joueurActif = self.gameController.getJoueurActif()
            joueurActif.listAmelioration.append(upgrade)
            print(joueurActif.listAmelioration)
      self.gameZone.update()
   
   def onBoutonClique(self, event):
      """ EVENEMENT CLIQUE D'UNE IMAGE SUR LE CANVAS USERINTERFACE """
      screenX = self.userInterface.canvasx(event.x)
      screenY  = self.userInterface.canvasy(event.y)
      item = event.widget.find_closest(screenX, screenY)
      for iBouton in self.userInterface.boutonListe:
         if iBouton == self.userInterface.boutonOuvrier:
            self.gameController.getJoueurActif().nbOuvrier += 1
            print (self.gameController.getJoueurActif().nbOuvrier)
         elif iBouton.tkId == item[0]:
            element = iBouton.event(self.gameZone.currentTuile, self.gameController.getJoueurActif())
            print(element)
            if element != None:
               self.gameZone.afficherElementIndex(element)
            self.gameZone.currentCity.getBatiment().addTerritoire(self.gameZone.currentTuile)
            self.gameZone.selectTerritoire(self.gameZone.currentCity)
            self.gameZone.selectTerritoireMairie(self.gameZone.currentCity)

   def onKeyPress(self, event):
      """METHODE APPELE QUAND UNE TOUCHE DU CLAVIER EST ENFONCE"""
      if event.char == "z":
         if self.afficherArbre:
            self.arbreCompetence.yview_scroll(-1,"unit")
         else:
            self.gameZone.yview_scroll(-1,"unit")
      elif event.char == "s":
         if self.afficherArbre:
            self.arbreCompetence.yview_scroll(1,"unit")
         else:
            self.gameZone.yview_scroll(1,"unit")
      elif event.char == "q":
         self.gameZone.xview_scroll(-1,"unit")
      elif event.char == "d":
         self.gameZone.xview_scroll(1,"unit")
      elif event.char == "e":
         if self.afficherArbre:
            self.arbre_competence.grid_forget()
            self.afficherArbre = False
         else:
            self.arbre_competence.grid(column=0, row=0)
            self.afficherArbre = True
      elif event.delta<0:
         self.userInterface.yview_scroll(1,"unit")
      elif event.delta>0:
         self.userInterface.yview_scroll(-1,"unit")  
