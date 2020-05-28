from tkinter import *
from numpy.random import choice

from spwts import spies, weights # List of spies and probability weights.

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text='QUIT', fg='red', command=frame.quit
        )
        self.button.pack(side=LEFT)

        self.spybutton = Button(
            frame, text='Gimme a spy!', fg='blue',
            command=self.choose_spy
        )
        self.spybutton.pack(side=LEFT)

    def choose_spy(self):
        spy = choice(spies, p=weights)
        print(f'Your spy is {spy}')

root = Tk()

app = App(root)

root.mainloop()






