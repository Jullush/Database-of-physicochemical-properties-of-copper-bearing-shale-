from tkinter import *
import listingSortedArticles
import secondMenuResearch
from PIL import ImageTk, Image

global image_to_show_monograph

Researches = {
    1: "GEOLOGICZNO-PETROGFRAFICZNE",
    2: "BIOLOGICZNE",
    3: "FIZYCZNE",
    4: "WYTRZYMAŁOŚCIOWE"
}


def listing_articles(x, y):
    listingSortedArticles.chosen_article = x
    listingSortedArticles.chosen_article_menu_id = y
    listingSortedArticles.ListingSortedArticles()


class SecondMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        secondMenuResearch.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = secondMenuResearch.image_to_show_monograph.resize((25, 25))
        secondMenuResearch.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        secondMenuResearch.image_to_show_monograph.image = secondMenuResearch.image_to_show_monograph
        # class
        self.geometry("380x270+700+400")
        self.title("Badania podstawowe")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=380, height=270, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()
        # buttons
        first_button = Button(self.mainFrame, text=Researches[1], font="arial 12",
                              command=lambda: listing_articles(Researches[1], 1), cursor="hand2")
        first_button.place(x=45, y=45)

        second_button = Button(self.mainFrame, text=Researches[2], font="arial 12",
                               command=lambda: listing_articles(Researches[2], 2), cursor="hand2")
        second_button.place(x=130, y=95)

        fourth_button = Button(self.mainFrame, text=Researches[3], font="arial 12",
                               command=lambda: listing_articles(Researches[3], 5), cursor="hand2")
        fourth_button.place(x=145, y=145)

        fifth_button = Button(self.mainFrame, text=Researches[4], font="arial 12",
                              command=lambda: listing_articles(Researches[4], 4), cursor="hand2")
        fifth_button.place(x=95, y=195)

        button_exit = Button(self.mainFrame, image=secondMenuResearch.image_to_show_monograph, command=self.destroy,
                             cursor="hand2")
        button_exit.place(x=10, y=10)
