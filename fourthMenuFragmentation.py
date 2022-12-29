from tkinter import *
import listingSortedArticles


Researches = {
    1: "FLOTACJA SOLNA",
    2: "FLOTACJA SPIENIACZOWA",
    3: "FLOTACJA TEMPERATUROWA",
    4: "FLOTACJA WZGLĘDEM INNYCH PARAMETRÓW",
}


def listing_articles(x, y):
    listingSortedArticles.chosen_article = x
    listingSortedArticles.chosen_article_menu_id = y
    listingSortedArticles.ListingSortedArticles()


class FourthMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("300x250+630+400")
        self.title("Procesy Mineralurgiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=250, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="SOLNA", font="arial 12",
                              command=lambda: listing_articles(Researches[1], 13))
        first_button.place(x=110, y=25)

        second_button = Button(self.mainFrame, text="SPIENIACZOWA", font="arial 12",
                               command=lambda: listing_articles(Researches[2], 14))
        second_button.place(x=80, y=75)

        third_button = Button(self.mainFrame, text="TEMPERATUROWA", font="arial 12",
                              command=lambda: listing_articles(Researches[3], 15))
        third_button.place(x=65, y=125)

        fourth_button = Button(self.mainFrame, text="INNE PARAMETRY", font="arial 12",
                               command=lambda: listing_articles(Researches[4], 16))
        fourth_button.place(x=70, y=175)

