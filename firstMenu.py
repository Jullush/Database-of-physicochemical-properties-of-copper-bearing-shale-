from tkinter import *
import secondMenuResearch
import thirdMenuProcesses


def second_menu_research():
    secondMenuResearch.SecondMenu()


def third_menu_processes():
    thirdMenuProcesses.ThirdMenu()


class FirstMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("300x150+800+400")
        self.title("Menu wyboru badań")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=150, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="BADANIA", font="arial 12",
                              command=second_menu_research)
        first_button.place(x=105, y=25)

        second_button = Button(self.mainFrame, text="PROCESY PRZERÓBCZE", font="arial 12",
                               command=third_menu_processes)
        second_button.place(x=50, y=75)

