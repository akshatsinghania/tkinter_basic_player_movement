from audioop import add
from tkinter import *

from numpy import rot90

"""
def create_player(self):
        self.player_rect = self.canvas.create_rectangle(10,10,40,40,fill="red")
"""

class App():
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.root.attributes('-fullscreen', True)
        self.initiate_canvas()
        
    def initiate_canvas(self):
        self.canvas = Canvas(self.root, bg='white', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.player_model()
        self.player_canvas_input()

    def player_model(self):
        self.player_rect = self.canvas.create_rectangle(60,60,100,100,fill='red')
        self.movement_value=10
    def player_canvas_input(self):
       self.canvas.bind("<Key>", self.player_movement)
       self.canvas.focus_set()
    def player_movement(self,event):
        movements = {'a':[-10,0],'w':[0,-10],'s':[0,10],'d':[10,0]}
        if(not event.char in movements):
            return
        self.canvas.move(self.player_rect,movements[event.char][0],movements[event.char][1])
    
        
       
    

        
        
       
    





        

        
        
        
        


app=App()
app.root.mainloop()




