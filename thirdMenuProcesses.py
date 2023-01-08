from tkinter import *
import fourthMenuFragmentation
import fifthMenuFragmentation
import listingSortedArticles
import thirdMenuProcesses
from PIL import ImageTk, Image

global image_to_show_monograph
Researches = {
    1: "FLOKULACJA",
    2: "SEPARACJA ELEKTRYCZNA",
    3: "AGLOMERACJA OLEJOWA",
    4: "KOAGULACJA",
    5: "FLOTACJA",
    6: "ROZDRABNIANIE CHEMICZNE"
}


def listing_articles(x, y):
    listingSortedArticles.chosen_article = x
    listingSortedArticles.chosen_article_menu_id = y
    listingSortedArticles.ListingSortedArticles()


def fifth_menu_fragmentation():
    fifthMenuFragmentation.FifthMenu()


def fourth_menu_fragmentation():
    fourthMenuFragmentation.FourthMenu()


class ThirdMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        thirdMenuProcesses.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = thirdMenuProcesses.image_to_show_monograph.resize((25, 25))
        thirdMenuProcesses.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        thirdMenuProcesses.image_to_show_monograph.image = thirdMenuProcesses.image_to_show_monograph
        # class
        self.geometry("340x380+700+400")
        self.title("Procesy Mineralurgiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=340, height=480, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="ROZDRABNIANIE CHEMICZNE", font="arial 12",
                              command=fifth_menu_fragmentation, cursor="hand2")
        first_button.place(x=50, y=40)

        second_button = Button(self.mainFrame, text="FLOKULACJA", font="arial 12",
                               command=lambda: listing_articles(Researches[1], 9), cursor="hand2")
        second_button.place(x=105, y=90)

        third_button = Button(self.mainFrame, text="SEPARACJA ELEKTRYCZNA", font="arial 12",
                              command=lambda: listing_articles(Researches[2], 10), cursor="hand2")
        third_button.place(x=55, y=140)

        fourth_button = Button(self.mainFrame, text="AGLOMERACJA OLEJOWA", font="arial 12",
                               command=lambda: listing_articles(Researches[3], 11), cursor="hand2")
        fourth_button.place(x=60, y=190)

        fifth_button = Button(self.mainFrame, text="KOAGULACJA", font="arial 12",
                              command=lambda: listing_articles(Researches[4], 12), cursor="hand2")
        fifth_button.place(x=105, y=240)

        sixth_button = Button(self.mainFrame, text="FLOTACJA", font="arial 12", command=fourth_menu_fragmentation,
                              cursor="hand2")
        sixth_button.place(x=115, y=290)

        button_exit = Button(self.mainFrame, image=thirdMenuProcesses.image_to_show_monograph, command=self.destroy,
                             cursor="hand2")
        button_exit.place(x=10, y=10)
