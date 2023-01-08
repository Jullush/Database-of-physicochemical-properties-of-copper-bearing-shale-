from tkinter import *
import secondMenuResearch
import thirdMenuProcesses
import firstMenu
from PIL import ImageTk, Image

global image_to_show_monograph

def second_menu_research():
    secondMenuResearch.SecondMenu()


def third_menu_processes():
    thirdMenuProcesses.ThirdMenu()


class FirstMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        firstMenu.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = firstMenu.image_to_show_monograph.resize((25, 25))
        firstMenu.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        firstMenu.image_to_show_monograph.image = firstMenu.image_to_show_monograph
        # class
        self.geometry("300x170+800+400")
        self.title("Menu wyboru badań")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=170, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()
        # buttons
        self.first_button = Button(self.mainFrame, text="BADANIA PODSTAWOWE", font="arial 12",
                                   command=second_menu_research, cursor="hand2")
        self.first_button.place(x=47, y=45)

        self.second_button = Button(self.mainFrame, text="PROCESY PRZERÓBCZE",
                                    font="arial 12", command=third_menu_processes, cursor="hand2")
        self.second_button.place(x=50, y=95)

        self.Button_exit = Button(self.mainFrame, image=firstMenu.image_to_show_monograph, command=self.destroy,
                                  cursor="hand2")
        self.Button_exit.place(x=10, y=10)

