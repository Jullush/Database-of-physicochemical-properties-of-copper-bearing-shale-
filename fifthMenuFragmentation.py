from tkinter import *


class FifthMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("300x200+630+400")
        self.title("Rozdrabnianie Chemiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=200, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="ROZTWARZANIE", font="arial 12")
        first_button.place(x=85, y=25)

        second_button = Button(self.mainFrame, text="ROZPUSZCZANIE", font="arial 12")
        second_button.place(x=80, y=75)

        third_button = Button(self.mainFrame, text="ŁUGOWANIE", font="arial 12")
        third_button.place(x=95, y=125)

