#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
import time
shouldquit = -1
tk = Tk()
tk.title("Video game");
tk.resizable(0,0);
canvas = Canvas(tk, width=640,height=480, bd=0, highlightthickness=0)
canvas.pack()
def key_pressed(event):
    if event.char == 'Q' or event.char == 'q':
        print("Recieved Quit")
        shouldquit = 1
        tk.destroy()

class a_little_thing:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(20,20,30,30,fill=color)
        self.canvas.move(self.id,300,100)
    def draw(self):
        self.canvas.move(self.id, 0, 1)
mine = a_little_thing(canvas, "blue")
tk.bind('<Key>',key_pressed)

while shouldquit == -1:
    mine.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
quit()