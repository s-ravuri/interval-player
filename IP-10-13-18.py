import time
from pygame import mixer
from tkinter import filedialog, Tk, BOTH
from tkinter.ttk import Frame, Button
from tkinter import *


def playFile(filePath, interval = 5, playTime = 60):
    playCount = int(playTime//interval)
    for play in range(0, playCount):
        mixer.init()
        mixer.music.load(filePath)
        mixer.music.play()
        time.sleep(interval*60)
        
global clicked
clicked = False


def findFile():
    global clicked
    clicked = True
    fileLocation = filedialog.askopenfilename(initialdir = "C:/", title = "Select file", filetypes = (("mp3 files","*.mp3"), ("m4a files", ".m4a"), ("all files","*.*")))
    return fileLocation
        

file = ''


class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
        
        self.master.title("Interval Player")
        self.pack(fill=BOTH, expand = 1)

        openButton = Button(self, text = "Open", command=findFile)
        openButton.place(x=0, y=0)
        
def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    if clicked == True:
            file = str(openButton.invoke())
            playFile(file)      
    app = Example()   
    root.mainloop()  
    
if __name__ == '__main__':
    main()   
        

        


        
