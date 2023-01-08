from tkinter import *
import listingSortedArticles
import fifthMenuFragmentation
from PIL import ImageTk, Image

Researches = {
    1: "ROZTWARZANIE",
    2: "ROZPUSZCZANIE",
    3: "ŁUGOWANIE",
}
global image_to_show_monograph


def listing_articles(x, y):
    listingSortedArticles.chosen_article = x
    listingSortedArticles.chosen_article_menu_id = y
    listingSortedArticles.ListingSortedArticles()


class FifthMenu(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        fifthMenuFragmentation.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = fifthMenuFragmentation.image_to_show_monograph.resize((25, 25))
        fifthMenuFragmentation.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        fifthMenuFragmentation.image_to_show_monograph.image = fifthMenuFragmentation.image_to_show_monograph

        # class
        self.geometry("300x200+630+400")
        self.title("Rozdrabnianie Chemiczne")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        self.mainFrame = Frame(self, width=300, height=200, bg='#FAFAFA', relief='sunken')
        self.mainFrame.pack()

        first_button = Button(self.mainFrame, text="ROZTWARZANIE", font="arial 12",
                              command=lambda: listing_articles(Researches[1], 6), cursor="hand2")
        first_button.place(x=85, y=25)

        second_button = Button(self.mainFrame, text="ROZPUSZCZANIE", font="arial 12",
                               command=lambda: listing_articles(Researches[2], 7), cursor="hand2")
        second_button.place(x=80, y=75)

        third_button = Button(self.mainFrame, text="ŁUGOWANIE", font="arial 12",
                              command=lambda: listing_articles(Researches[3], 8), cursor="hand2")
        third_button.place(x=95, y=125)

        button_exit = Button(self.mainFrame, image=fifthMenuFragmentation.image_to_show_monograph,
                             command=self.destroy, cursor="hand2")
        button_exit.place(x=10, y=10)
