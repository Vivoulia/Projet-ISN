from threading import Thread
import winsound
import time


class SonManager():
    def __init__(self):
        self.sonFond = Son()

    def playSonFond(self):
        self.sonFond.start()
    
    def playSonCliqueVille(self):
        pass
    

class Son(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        winsound.PlaySound('son.wav',winsound.SND_FILENAME)