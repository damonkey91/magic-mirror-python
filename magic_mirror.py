import tkinter as tk
from tkinter import *
from screens.standard import Standard
from screens.time_is_money import TimeIsMoney
from screens.all_widgets_screen import AllWidgets

class MagicMirror:
    def __init__(self):
        self._startup_screen()

        root = tk.Tk()
        root.title('Mirror')

        self._add_screen(root)

        root.attributes("-fullscreen", True)
        root.configure(background='black')
        self.startupscreen.destroy()
        root.mainloop()

    def _startup_screen(self):
        self.startupscreen = tk.Tk()
        self.startupscreen.title('Magic Mirror Python')
        welcometext = tk.Label(self.startupscreen, font=('caviar dreams', 40), bg='black', fg='white')
        self.startupscreen.configure(background='black')
        self.startupscreen.overrideredirect(True)
        welcometext.config(text='Magic mirror!')
        welcometext.pack(side=LEFT, padx=120, pady=80)
        # Gets the requested values of the height and widht.
        windowWidth = self.startupscreen.winfo_reqwidth()
        windowHeight = self.startupscreen.winfo_reqheight()
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.startupscreen.winfo_screenwidth() / 3 - windowWidth / 2)
        positionDown = int(self.startupscreen.winfo_screenheight() / 2 - windowHeight / 2)

        # Positions the window in the center of the page.
        self.startupscreen.geometry("+{}+{}".format(positionRight, positionDown))
        self.startupscreen.update()

    def _add_screen(self, root):
        Standard(root)
        #TimeIsMoney(root)
        #AllWidgets(root)

