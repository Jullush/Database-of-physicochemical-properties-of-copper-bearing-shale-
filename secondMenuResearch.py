from tkinter import *
import listingSortedArticles


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

        self.geometry("350x250+700+400")
        self.title("Badania")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=350, height=250, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text=Researches[1], font="arial 12",
                              command=lambda: listing_articles(Researches[1], 1))
        first_button.place(x=25, y=25)

        second_button = Button(self.mainFrame, text=Researches[2], font="arial 12",
                               command=lambda: listing_articles(Researches[2], 2))
        second_button.place(x=115, y=75)

        fourth_button = Button(self.mainFrame, text=Researches[3], font="arial 12",
                               command=lambda: listing_articles(Researches[3], 5))
        fourth_button.place(x=130, y=125)

        fifth_button = Button(self.mainFrame, text=Researches[4], font="arial 12",
                              command=lambda: listing_articles(Researches[4], 4))
        fifth_button.place(x=80, y=175)
