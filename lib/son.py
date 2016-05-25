from threading import Thread
from random import randint
import winsound
import time
import wave


class SonManager():
    def __init__(self):
        self.sonFond = SonFond()
        self.playingSound = None

    def playSonFond(self):
        self.sonFond.start()
    
    def playSound(self, file, repeat):
        if self.playingSound != None:
            if self.playingSound.playing == False:
                self.playingSound = Son(file, repeat)
                self.playingSound.start()
        else:
            self.playingSound = Son(file, repeat)
            self.playingSound.start()            
    def closeAll(self):
        self.sonFond.stop()
        self.sonFond.deamon = True
        if self.playingSound != None:
            self.playingSound.deamon = True
    

class Son(Thread):
    def __init__(self, file, repeat):
        Thread.__init__(self)
        self.playing = False
        self.repeat = repeat
        self.file = file
    def run(self):
        print("On joue un son")
        self.playing = True
        while self.playing:
            winsound.PlaySound(self.file,winsound.SND_FILENAME)
            if self.repeat == False:
                self.playing = False
            
    def stop(self):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        self.playing = False
        
class SonFond(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.playing = False
        self.repeat = True
        self.file = list()
        self.file.append("son/musique fond celte")
        self.file.append("son/musique fond epic")
        self.file.append("son/musique fond greensleeves")
        self.file.append("son/musique fond sad")
    def run(self):
        musiqueAleatoire = randint(0, len(self.file)-1)
        self.playing = True
        while self.playing:
            winsound.PlaySound(self.file[musiqueAleatoire],winsound.SND_FILENAME)
            if self.repeat == False:
                self.playing = False
            
    def stop(self):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        self.playing = False
    
    
    
    
