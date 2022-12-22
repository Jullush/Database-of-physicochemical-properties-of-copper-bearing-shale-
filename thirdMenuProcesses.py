from tkinter import *
import fourthMenuFragmentation
import fifthMenuFragmentation


def fifth_menu_fragmentation():
    fifthMenuFragmentation.FifthMenu()


def fourth_menu_fragmentation():
    fourthMenuFragmentation.FourthMenu()


class ThirdMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("300x350+700+400")
        self.title("Procesy Mineralurgiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=450, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="ROZDRABNIANIE CHEMICZNE", font="arial 12",
                              command=fifth_menu_fragmentation)
        first_button.place(x=30, y=25)

        second_button = Button(self.mainFrame, text="FLOKULACJA", font="arial 12")
        second_button.place(x=85, y=75)

        third_button = Button(self.mainFrame, text="SEPARACJA ELEKTRYCZNA", font="arial 12")
        third_button.place(x=35, y=125)

        fourth_button = Button(self.mainFrame, text="AGLOMERACJA OLEJOWA", font="arial 12")
        fourth_button.place(x=40, y=175)

        fifth_button = Button(self.mainFrame, text="KOAGULACJA", font="arial 12")
        fifth_button.place(x=85, y=225)

        sixth_button = Button(self.mainFrame, text="FLOTACJA", font="arial 12", command=fourth_menu_fragmentation)
        sixth_button.place(x=95, y=275)