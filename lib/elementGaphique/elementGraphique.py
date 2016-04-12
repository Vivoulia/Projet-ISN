class ElementGraphique():
   def __init__(self, x, y, texture, parent):
      self.x = x
      self.y = y
      self.zindex = 0
      self.fileName="texture/"+texture
      self.photo = PhotoImage(file = self.fileName)
      self.tkId = 0
      self.parent = parent
   def setTkId(self, identifiant):
      self.tkId = identifiant