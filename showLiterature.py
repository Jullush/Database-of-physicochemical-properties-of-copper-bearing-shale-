from tkinter import *
import openArticle
import sqlite3
import showLiterature
from PIL import Image, ImageTk

global image_to_show_monograph
co = sqlite3.connect("monograph_db.db")
c = co.cursor()


class ShowLiterature(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        showLiterature.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = showLiterature.image_to_show_monograph.resize((25, 25))
        showLiterature.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        showLiterature.image_to_show_monograph.image = showLiterature.image_to_show_monograph
        # class
        self.geometry("500x600+500+200")
        self.title("Monografie")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        # Frames
        self.topFrame = Frame(self, height=75, width=500)
        self.topFrame.pack()

        self.downFrame = Frame(self, height=800, bg='white')
        self.downFrame.pack(fill=X)

        self.centerLabel = Frame(self, height=500, width=500, bg='#FAFAFA', borderwidth=4, relief='groove')
        self.centerLabel.place(x=20, y=100)

        # Headings
        heading1 = Label(self.topFrame, text="Literatura", font='arial 14')
        heading1.place(x=190, y=25)

        # lists and scrollbars
        self.listOfArticles = Listbox(self.centerLabel, height=22, width=52, font='times 12', bg='#FAFAFA')
        self.listOfArticles.grid(sticky=N, row=0, column=0, padx=(5, 21), pady=(5, 17))
        self.rightScrollbar = Scrollbar(self.centerLabel, orient="vertical")
        self.downScrollbar = Scrollbar(self.centerLabel, orient="horizontal")
        self.rightScrollbar.grid(row=0, column=0, pady=(0, 17), sticky=N+S+E)
        self.downScrollbar.grid(row=0, column=0, sticky=S+W+E)
        self.listOfArticles.config(yscrollcommand=self.rightScrollbar.set, xscrollcommand=self.downScrollbar.set)
        self.downScrollbar.config(command=self.listOfArticles.xview, cursor="hand2")
        self.rightScrollbar.config(command=self.listOfArticles.yview, cursor="hand2")

        button_exit = Button(self.topFrame, image=showLiterature.image_to_show_monograph, command=self.destroy,
                             cursor="hand2")
        button_exit.place(x=30, y=25)

        articles = c.execute(
            "SELECT *  FROM literature WHERE key_id=?", (openArticle.article_key_number,)).fetchall()
        count = 0
        self.listOfArticles.delete(0, END)
        self.listOfArticles.insert(END, "\n")

        for article in articles:
            self.listOfArticles.insert(count, str(article[1]))
            count = count + 1
        self.listOfArticles.config(activestyle=NONE)
