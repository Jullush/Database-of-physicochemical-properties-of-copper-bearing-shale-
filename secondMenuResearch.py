from tkinter import *


class SecondMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("350x250+700+400")
        self.title("Badania")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=350, height=250, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="GEOLOGICZNO-PETROGFRAFICZNE", font="arial 12")
        first_button.place(x=25, y=25)

        second_button = Button(self.mainFrame, text="BIOLOGICZNE", font="arial 12")
        second_button.place(x=115, y=75)

        fourth_button = Button(self.mainFrame, text="FIZYCZNE", font="arial 12")
        fourth_button.place(x=130, y=125)

        fifth_button = Button(self.mainFrame, text="WYTRZYMAŁOŚCIOWE", font="arial 12")
        fifth_button.place(x=80, y=175)