from tkinter import *
import listingSortedArticles
import fourthMenuFragmentation
from PIL import ImageTk, Image

global image_to_show_monograph

Researches = {
    1: "FLOTACJA SOLNA",
    2: "FLOTACJA PIANOWA",
    4: "FLOTACJA WZGLĘDEM INNYCH PARAMETRÓW",
}


def listing_articles(x, y):
    listingSortedArticles.chosen_article = x
    listingSortedArticles.chosen_article_menu_id = y
    listingSortedArticles.ListingSortedArticles()


class FourthMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        fourthMenuFragmentation.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = fourthMenuFragmentation.image_to_show_monograph.resize((25, 25))
        fourthMenuFragmentation.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        fourthMenuFragmentation.image_to_show_monograph.image = fourthMenuFragmentation.image_to_show_monograph
        # class
        self.geometry("240x200+630+400")
        self.title("Procesy Mineralurgiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=240, height=200, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        second_button = Button(self.mainFrame, text="PIANOWA", font="arial 12",
                               command=lambda: listing_articles(Researches[2], 14), cursor="hand2" )
        second_button.place(x=70, y=25)

        first_button = Button(self.mainFrame, text="SOLNA", font="arial 12",
                              command=lambda: listing_articles(Researches[1], 13), cursor="hand2")
        first_button.place(x=80, y=75)

        fourth_button = Button(self.mainFrame, text="INNE PARAMETRY", font="arial 12",
                               command=lambda: listing_articles(Researches[4], 16), cursor="hand2")
        fourth_button.place(x=40, y=125)

        button_exit = Button(self.mainFrame, image=fourthMenuFragmentation.image_to_show_monograph,
                             command=self.destroy, cursor="hand2")
        button_exit.place(x=10, y=10)

