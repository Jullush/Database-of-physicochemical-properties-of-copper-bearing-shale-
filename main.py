from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import showMonografie
import openArticle
import firstMenu

co = sqlite3.connect('monograph_db.db')
c = co.cursor()

global searching_for_an_article

global no_highlight


def cleaning_the_author_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.author = str(db_data_2)


def cleaning_the_title_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.title = str(db_data_2)


def showMonograph():
    showMonografie.ShowMonografie()


def first_choice_Menu():
    firstMenu.FirstMenu()


class Main(object):
    def __init__(self, master):
        self.master = master
        main.no_highlight = 0
        # ______ rockImage variables
        rock_image = Image.open('app_icons/rocks.png')
        rock_image_resized = rock_image.resize((150, 150))
        rock_image_resized_rotated = rock_image_resized.rotate(180)

        rock_image_done = ImageTk.PhotoImage(rock_image_resized)
        rock_image_done_2 = ImageTk.PhotoImage(rock_image_resized_rotated)

        # _______ mainFrame
        master_frame = Frame(self.master)
        master_frame.pack()

        # _____ additional frame
        handy_frame_one = Frame(master_frame, width=1350, height=100)
        handy_frame_one.pack(side='top')

        # _______ searchFrame
        center_frame = Frame(master_frame, width=800, height=50, bg='#FAFAFA', borderwidth=4, relief='groove')
        center_frame.pack()

        self.searchLabel = Label(center_frame, text='Wpisz szukaną frazę :', font='arial 12', bg='#FAFAFA')
        self.searchLabel.grid(row=0, column=0, padx=20, pady=10)

        self.entrySearch = Entry(center_frame, width=30, bd=10)
        self.entrySearch.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.searchButton = Button(center_frame, text='WYSZUKAJ', font='arial 12', bg='white',
                                   command=self.article_searching)
        self.searchButton.grid(row=0, column=4, padx=20, pady=10)

        # _____ additional frames
        handy_frame_two = Frame(master_frame, width=800, height=300)
        handy_frame_two.pack(side='bottom')

        additional_frame = Frame(master_frame, width=800, height=50)
        additional_frame.pack(side='top')

        search_frame = Frame(master_frame, width=800, height=50, bg='#FAFAFA', borderwidth=4, relief='groove')
        search_frame.pack(side='top')

        # _______ HEADING Text
        label_heading = Label(master_frame, text="BAZA DANYCH WŁAŚCIWOŚCI FIZYKO-CHEMICZNYCH ŁUPKA MIEDZIONOŚNEGO",
                              font='arial 16')
        label_heading.place(x=290, y=25)

        abel_heading = Label(master_frame, text=" Wybierz artykuł poniżej ",
                             font='arial 12', background='white', fg='#5A5A5A', relief='solid')
        abel_heading.place(x=270, y=187)

        # ________ Rock1
        rock_label = Label(master_frame, image=rock_image_done)
        rock_label.image = rock_image_done
        rock_label.place(x=50, y=300)

        # ________ Rock1
        rock_label2 = Label(master_frame, image=rock_image_done_2)
        rock_label2.image = rock_image_done_2
        rock_label2.place(x=1150, y=300)

        # __________ SearchBox

        self.listOfArticles = Listbox(search_frame, height=10, width=100, font='times 12', bg='grey', fg='white',
                                      highlightthickness=2, highlightcolor='black', selectbackground='black')
        self.listOfArticles.grid(sticky=N, row=0, column=0, padx=(5, 21), pady=(5, 17))
        self.rightScrollbar = Scrollbar(search_frame, orient="vertical")
        self.downScrollbar = Scrollbar(search_frame, orient="horizontal")
        self.rightScrollbar.grid(row=0, column=0, pady=(0, 17), sticky=N + S + E)
        self.downScrollbar.grid(row=0, column=0, sticky=S + W + E)
        self.listOfArticles.config(yscrollcommand=self.rightScrollbar.set, xscrollcommand=self.downScrollbar.set)
        self.downScrollbar.config(command=self.listOfArticles.xview)
        self.rightScrollbar.config(command=self.listOfArticles.yview)

        # MONOGRAPH buttons within the main menu
        self.MonographButton = Button(handy_frame_two, text=' Monografie ', font='arial 12 bold',
                                      command=showMonograph)
        self.MonographButton.place(x=675, y=100)

        # Article MENU buttons
        self.ArticleMenuButton = Button(handy_frame_two, text=' Menu wyboru badań  ',
                                        font='arial 12 bold',
                                        command=first_choice_Menu)
        self.ArticleMenuButton.place(x=0, y=100)

        self.Button_exit = Button(handy_frame_two, text='Zamknij', font='arial 13 bold', command=quit)
        self.Button_exit.place(x=365, y=100)

    # _______ searching

    def article_searching(self):
        self.listOfArticles.delete(0, END)
        searching_for_an_article = self.entrySearch.get()
        searching = c.execute("SELECT article_id FROM full_text_search WHERE text_search LIKE ?",
                              ('%' + searching_for_an_article + '%',)).fetchall()
        article_tuple_to_list = [list[0] for list in searching]
        print(searching_for_an_article)
        i = 0
        count = 0
        for x in article_tuple_to_list:
            searched_article = article_tuple_to_list[i]
            searching_comparison = c.execute("SELECT authors, title FROM articles_1 WHERE key_id=? ",
                                             (searched_article,)).fetchall()
            for article in searching_comparison:
                self.listOfArticles.insert(count, str(article[0]) + " - " + str(article[1]))

            i = i+1

        # ------

        def showArticle_(x, y):
            openArticle.article_key_number = x
            openArticle.text_to_highlight = y
            openArticle.boolean_to_high = True
            openArticle.OpenArticle()

        # ------
        def display_the_art_with_highlight(evt):

            if self.listOfArticles.curselection() != ():
                value = str(self.listOfArticles.get(self.listOfArticles.curselection()))
                id = value.split(' - ')[1]
                # print(id)
                article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?", (id,))
                article_to_find_key_id = article_to_find.fetchall()
                article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
                article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(
                    ({ord(b): None for
                      b in "[(,)]"}))
                article_key_id = int(article_to_find_key_id_to_translate_2)
                title_of_article = c.execute("SELECT title FROM articles_1 WHERE key_id=?", (article_key_id,))
                title_of_article_ready = title_of_article.fetchall()
                cleaning_the_title_data(title_of_article_ready)

                if len(openArticle.title) > 30:
                    openArticle.title = openArticle.title.split(" ")
                    openArticle.title.insert(7, "\n")
                    openArticle.title = " ".join(openArticle.title)

                else:
                    pass

                openArticle.title = openArticle.title.translate(({ord(b): None for b in "',"}))
                # print(openArticle.title)
                author_of_article = c.execute("SELECT authors FROM articles_1 WHERE key_id=?", (article_key_id,))
                author_of_article_ready = author_of_article.fetchall()
                cleaning_the_author_data(author_of_article_ready)
                openArticle.author = openArticle.author.translate(({ord(b): None for b in "'"}))
                openArticle.author = openArticle.author[:-1]
                print(article_key_id)
                main.no_highlight = 1
                showArticle_(article_key_id, searching_for_an_article)

        self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_with_highlight)


def main():
    root = Tk()
    Main(root)
    root.title("Baza Danych Łupka Miedzionośnego")
    root.geometry("1350x750+350+200")
    root.iconbitmap('app_icons/mainicon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
