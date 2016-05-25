from threading import Thread
import winsound
import time
import wave


class SonManager():
    def __init__(self):
        self.sonFond = Son('musique fond.wav')
        self.playingSound = None

    def playSonFond(self):
        self.sonFond.start()
    
    def playSound(self):
        pass
    def closeAll(self):
        print("On stop")
        self.sonFond.stop()
        self.sonFond.deamon = True
        if self.playingSound != None:
            self.playingSound.deamon = True
    

class Son(Thread):
    def __init__(self, file):
        Thread.__init__(self)
        self.stopped = False
        self.file = file
    def run(self):
        while not self.stopped:       
            winsound.PlaySound(self.file,winsound.SND_FILENAME)
            
    def stop(self):
        winsound.PlaySound(None, winsound.SND_FILENAME)
        self.stopped = True
    
    
    
    
