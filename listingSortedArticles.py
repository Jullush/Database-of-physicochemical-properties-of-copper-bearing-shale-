from tkinter import *
import sqlite3
import openArticle
from PIL import ImageTk, Image
import time
import showMonografie
import listingSortedArticles

co = sqlite3.connect("monograph_db.db")
c = co.cursor()

global chosen_article
global chosen_article_menu_id
global return_image

def cleaning_the_author_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.author = str(db_data_2)


def cleaning_the_title_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.title = str(db_data_2)


class ListingSortedArticles(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        showMonografie.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = showMonografie.image_to_show_monograph.resize((25, 25))
        showMonografie.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        showMonografie.image_to_show_monograph.image = showMonografie.image_to_show_monograph
        # return arrow
        listingSortedArticles.return_image = Image.open('app_icons/arrow_2.png')
        arrow_image_resized = listingSortedArticles.return_image.resize((25, 25))
        listingSortedArticles.return_image = ImageTk.PhotoImage(arrow_image_resized)
        listingSortedArticles.return_image.image = listingSortedArticles.return_image
        # class
        self.geometry("900x550+500+200")
        self.title(f'Badania: {chosen_article.lower()}')
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        # Frames
        self.topFrame = Frame(self, height=110, width=876, relief='ridge', borderwidth=5, bg='#FAFAFA')
        self.topFrame.place(x=15, y=0)

        self.centerLabel = Frame(self, height=600, width=500, borderwidth=4, relief='sunken')
        self.centerLabel.place(x=22, y=110)

        if chosen_article_menu_id != 14 and chosen_article_menu_id != 16:
            self.Button_exit = Button(self.topFrame, image=showMonografie.image_to_show_monograph, command=self.destroy
                                      , cursor="hand2")
            self.Button_exit.place(x=30, y=40)

        if chosen_article_menu_id != 14 and chosen_article_menu_id != 16:
            rock_image = Image.open('app_icons/rocks.png')
            rock_image_resized = rock_image.resize((40, 40))
            rock_image_resized_rotated = rock_image_resized.rotate(180)

            rock_image_done = ImageTk.PhotoImage(rock_image_resized)
            rock_label = Label(self.topFrame, image=rock_image_done, bg='#FAFAFA')
            rock_label.image = rock_image_done
            rock_label.place(x=760, y=35)

            rock_image_done_2 = ImageTk.PhotoImage(rock_image_resized_rotated)
            rock_label2 = Label(self.topFrame, image=rock_image_done_2, bg='#FAFAFA')
            rock_label2.image = rock_image_done_2
            rock_label2.place(x=695, y=35)
        else:
            pass

        def default_listbox_state():
            articles = c.execute(
                "SELECT authors, title, publication_date  FROM articles_1 WHERE menu_id=?",
                (chosen_article_menu_id,)).fetchall()
            count = 0
            self.listOfArticles.delete(0, END)
            publication = ""

            for article in articles:

                if article[2] == 2014:
                    publication = "Ł.M I, "
                elif article[2] == 2016:
                    publication = "Ł.M II, "
                elif article[2] == 2018:
                    publication = "Ł.M IV, "
                elif article[2] == 2017:
                    publication = "Ł.M III, "
                elif article[2] == 2021:
                    publication = "Ł.M V, "
                else:
                    pass
                self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                           + str(article[2]))
                count = count + 1

            def showArticle_(x):
                openArticle.article_key_number = x
                openArticle.text_to_highlight = ""
                openArticle.OpenArticle()

            def display_the_art(evt):

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
                    showArticle_(article_key_id)

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art)

        def show_after_fetching():

            def showArticle_(x):
                openArticle.article_key_number = x
                openArticle.text_to_highlight = ""
                openArticle.OpenArticle()

            def display_the_art_after_fetching(evt):

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
                    showArticle_(article_key_id)

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_after_fetching)

        def show_machines():
            machines = c.execute("SELECT machine_name FROM machines")
            machines_fetched = machines.fetchall()
            count = 0
            self.listOfArticles.delete(0, END)

            for machine in machines_fetched:
                self.listOfArticles.insert(count, str(machine[0]))
                count = count + 1

            def display_the_art_4(evt):

                if self.listOfArticles.curselection() != ():
                    value = str(self.listOfArticles.get(self.listOfArticles.curselection()))
                    id = value
                    print(id)
                    article_to_find = c.execute("SELECT articles_1.authors, articles_1.title, "
                                                "articles_1.publication_date FROM articles_1 "
                                                "INNER JOIN machines_article_1_id_comparison "
                                                "ON machines_article_1_id_comparison.article_id = articles_1.key_id "
                                                "INNER JOIN machines "
                                                "ON machines.machine_id = "
                                                "machines_article_1_id_comparison.machine_id "
                                                "WHERE machine_name =?", (id,)).fetchall()
                    count = 0
                    self.listOfArticles.delete(0, END)
                    publication = ""
                    time.sleep(0.75)

                    for article in article_to_find:

                        if article[2] == 2014:
                            publication = "Ł.M I, "
                        elif article[2] == 2016:
                            publication = "Ł.M II, "
                        elif article[2] == 2018:
                            publication = "Ł.M IV, "
                        elif article[2] == 2017:
                            publication = "Ł.M III, "
                        elif article[2] == 2021:
                            publication = "Ł.M V, "
                        else:
                            pass
                        self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                                   + str(article[2]))
                        count = count + 1

                    self.listOfArticles.unbind('<<ListboxSelect>>')
                show_after_fetching()

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_4)

        def show_collectors():
            collectors = c.execute("SELECT collector_name FROM collectors")
            collectors_fetched = collectors.fetchall()
            count = 0
            self.listOfArticles.delete(0, END)

            for collector in collectors_fetched:
                self.listOfArticles.insert(count, str(collector[0]))
                count = count + 1

            def display_the_art_3(evt):

                if self.listOfArticles.curselection() != ():
                    value = str(self.listOfArticles.get(self.listOfArticles.curselection()))
                    id = value
                    print(id)
                    article_to_find = c.execute("SELECT articles_1.authors, articles_1.title, "
                                                "articles_1_publication_date FROM articles_1 "
                                                "INNER JOIN collectors_article_1_id_comparison "
                                                "ON collectors_article_1_id_comparison.article_id = articles_1.key_id "
                                                "INNER JOIN collectors "
                                                "ON collectors.collector_id = "
                                                "collectors_article_1_id_comparison.collector_id "
                                                "WHERE collector_name=?", (id,)).fetchall()
                    count = 0
                    self.listOfArticles.delete(0, END)
                    time.sleep(0.75)
                    publication = ""

                    for article in article_to_find:

                        if article[2] == 2014:
                            publication = "Ł.M I, "
                        elif article[2] == 2016:
                            publication = "Ł.M II, "
                        elif article[2] == 2018:
                            publication = "Ł.M IV, "
                        elif article[2] == 2017:
                            publication = "Ł.M III, "
                        elif article[2] == 2021:
                            publication = "Ł.M V, "
                        else:
                            pass
                        self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                                   + str(article[2]))
                        count = count + 1

                    self.listOfArticles.unbind('<<ListboxSelect>>')
                show_after_fetching()

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_3)

        def show_depressors():
            depressors = c.execute("SELECT depressor_name FROM depressors")
            depressors_fetched = depressors.fetchall()
            count = 0
            self.listOfArticles.delete(0, END)

            for depressor in depressors_fetched:
                self.listOfArticles.insert(count, str(depressor[0]))
                count = count + 1

            def display_the_art_5(evt):

                if self.listOfArticles.curselection() != ():
                    value = str(self.listOfArticles.get(self.listOfArticles.curselection()))
                    id = value
                    print(id)
                    article_to_find = c.execute("SELECT articles_1.authors, articles_1.title, "
                                                "articles_1.publication_date FROM articles_1 "
                                                "INNER JOIN depressors_article_1_id_comparison "
                                                "ON depressors_article_1_id_comparison.article_id = articles_1.key_id "
                                                "INNER JOIN depressors "
                                                "ON depressors.depressor_id = "
                                                "depressors_article_1_id_comparison.depressor_id "
                                                "WHERE depressor_name=?", (id,)).fetchall()
                    count = 0
                    self.listOfArticles.delete(0, END)
                    publication = ""
                    time.sleep(0.75)

                    for article in article_to_find:

                        if article[2] == 2014:
                            publication = "Ł.M I, "
                        elif article[2] == 2016:
                            publication = "Ł.M II, "
                        elif article[2] == 2018:
                            publication = "Ł.M IV, "
                        elif article[2] == 2017:
                            publication = "Ł.M III, "
                        elif article[2] == 2021:
                            publication = "Ł.M V, "
                        else:
                            pass
                        self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                                   + str(article[2]))
                        count = count + 1

                    self.listOfArticles.unbind('<<ListboxSelect>>')
                show_after_fetching()

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_5)

        def show_frothers():
            frothers = c.execute("SELECT frother_name FROM frothers_id")
            frothers_fetched = frothers.fetchall()
            count = 0
            self.listOfArticles.delete(0, END)

            for frother in frothers_fetched:
                self.listOfArticles.insert(count, str(frother[0]))
                count = count + 1

            def display_the_art_2(evt):

                if self.listOfArticles.curselection() != ():
                    value = str(self.listOfArticles.get(self.listOfArticles.curselection()))
                    id = value
                    print(id)
                    article_to_find = c.execute("SELECT articles_1.authors, articles_1.title, "
                                                "articles_1.publication_date FROM articles_1 "
                                                "INNER JOIN frothers_article_1_id_comparison "
                                                "ON frothers_article_1_id_comparison.article_id = articles_1.key_id "
                                                "INNER JOIN frothers_id "
                                                "ON frothers_id.frother_id = "
                                                "frothers_article_1_id_comparison.frother_id "
                                                "WHERE frother_name=?", (id,)).fetchall()
                    count = 0
                    self.listOfArticles.delete(0, END)
                    publication = ""
                    time.sleep(0.75)

                    for article in article_to_find:

                        if article[2] == 2014:
                            publication = "Ł.M I, "
                        elif article[2] == 2016:
                            publication = "Ł.M II, "
                        elif article[2] == 2018:
                            publication = "Ł.M IV, "
                        elif article[2] == 2017:
                            publication = "Ł.M III, "
                        elif article[2] == 2021:
                            publication = "Ł.M V, "
                        else:
                            pass
                        self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                                   + str(article[2]))
                        count = count + 1

                    self.listOfArticles.unbind('<<ListboxSelect>>')
                show_after_fetching()

            self.listOfArticles.bind('<<ListboxSelect>>', display_the_art_2)

        def show_others_parameters(parameter):
            h = c.execute(f"SELECT articles_1.authors, articles_1.title, articles_1.publication_date "
                          f"FROM articles_1 INNER JOIN other_parameters_filtration "
                          f"ON other_parameters_filtration.{parameter} = articles_1.key_id")
            h = h.fetchall()
            count = 0
            publication = ""
            self.listOfArticles.delete(0, END)

            for article in h:

                if article[2] == 2014:
                    publication = "Ł.M I, "
                elif article[2] == 2016:
                    publication = "Ł.M II, "
                elif article[2] == 2018:
                    publication = "Ł.M IV, "
                elif article[2] == 2017:
                    publication = "Ł.M III, "
                elif article[2] == 2021:
                    publication = "Ł.M V, "
                else:
                    pass
                self.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + publication
                                           + str(article[2]))
                count = count + 1


        # additional researches

        if chosen_article_menu_id == 14:
            self.button_exit = Button(self.topFrame, image=showMonografie.image_to_show_monograph,
                                      command=self.destroy, cursor="hand2")
            self.button_exit.place(x=10, y=10)
            self.return_button = Button(self.topFrame, image=listingSortedArticles.return_image,
                                        command=default_listbox_state,
                                        cursor="hand2")
            self.return_button.place(x=10, y=55)
            self.frothers_button = Button(self.topFrame, text='Spieniacze', font='arial 12',
                                          bg="#ebecf0", command=show_frothers, cursor="hand2")
            self.frothers_button.place(x=735, y=10)
            self.collectors_button = Button(self.topFrame, text='Zbieracze',
                                            font='arial 12', bg="#ebecf0", command=show_collectors, cursor="hand2")
            self.collectors_button.place(x=738, y=55)
            self.machines_button = Button(self.topFrame, text='Urządzenia flotacyjne', bg="#ebecf0",
                                          font='arial 12',
                                          command=show_machines, cursor="hand2")
            self.machines_button.place(x=55, y=55)
            self.depressors_button = Button(self.topFrame, text='Depresory', command=show_depressors, bg="#ebecf0",
                                            font='arial 12', cursor="hand2")
            self.depressors_button.place(x=55, y=10)
        elif chosen_article_menu_id == 16:

            self.button_exit = Button(self.topFrame, image=showMonografie.image_to_show_monograph,
                                      command=self.destroy, cursor="hand2")
            self.button_exit.place(x=10, y=10)
            self.return_button = Button(self.topFrame, image=listingSortedArticles.return_image,
                                        command=default_listbox_state,
                                        cursor="hand2")
            self.return_button.place(x=10, y=55)
            self.ph_button = Button(self.topFrame, text='Parametr pH', font='arial 12', bg="#ebecf0",
                                    command=lambda: show_others_parameters("ph_id"), cursor="hand2")
            self.ph_button.place(x=735, y=10)
            self.temperature_button = Button(self.topFrame, text='Temperatura', font='arial 12', bg="#ebecf0", command=
                                             lambda: show_others_parameters("temperature_id"), cursor="hand2")
            self.temperature_button.place(x=738, y=55)
            self.hydrophobicity_button = Button(self.topFrame, text='Hydrofobowość', bg="#ebecf0", font='arial 12',
                                                command=lambda: show_others_parameters("hydrophobicity_id"),
                                                cursor="hand2")
            self.hydrophobicity_button.place(x=55, y=55)

        else:
            pass

        # Headings
        if chosen_article_menu_id == 1:
            heading1 = Label(self.topFrame, text=f'BADANIA {chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=190, y=40)
        elif chosen_article_menu_id == 2:
            heading1 = Label(self.topFrame, text=f'BADANIA {chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=305, y=40)
        elif chosen_article_menu_id == 5:
            heading1 = Label(self.topFrame, text=f'BADANIA {chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=340, y=40)
        elif chosen_article_menu_id == 4:
            heading1 = Label(self.topFrame, text=f'BADANIA {chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=265, y=40)
        elif chosen_article_menu_id == 9 or chosen_article_menu_id == 12 or chosen_article_menu_id == 6 \
                or chosen_article_menu_id == 7 or chosen_article_menu_id == 8:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=340, y=40)
        elif chosen_article_menu_id == 10:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=265, y=40)
        elif chosen_article_menu_id == 11:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=265, y=40)
        elif chosen_article_menu_id == 13:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=300, y=40)
        elif chosen_article_menu_id == 14:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=330, y=40)
        elif chosen_article_menu_id == 15:
            heading1 = Label(self.topFrame, text=f'{chosen_article}', font='arial 14', bg='#FAFAFA')
            heading1.place(x=274, y=40)
        elif chosen_article_menu_id == 16:
            heading1 = Label(self.topFrame, text="FLOTACJA \n WZGLĘDEM INNYCH PARAMETRÓW", font='arial 14',
                             bg='#FAFAFA')
            heading1.place(x=250, y=20)
        else:
            pass

        # lists and scrollbars
        self.listOfArticles = Listbox(self.centerLabel, height=20, width=103, font='times 12', bg='grey', fg='white',
                                      highlightthickness=2, highlightcolor='black', selectbackground='black',
                                      cursor='hand2', selectmode=SINGLE, activestyle="dotbox")
        self.listOfArticles.grid(sticky=N, row=0, column=0, padx=(5, 21), pady=(5, 17))
        self.rightScrollbar = Scrollbar(self.centerLabel, orient="vertical")
        self.downScrollbar = Scrollbar(self.centerLabel, orient="horizontal")
        self.rightScrollbar.grid(row=0, column=0, pady=(0, 17), sticky=N + S + E)
        self.downScrollbar.grid(row=0, column=0, sticky=S + W + E)
        self.listOfArticles.config(yscrollcommand=self.rightScrollbar.set, xscrollcommand=self.downScrollbar.set)
        self.downScrollbar.config(command=self.listOfArticles.xview)
        self.rightScrollbar.config(command=self.listOfArticles.yview)

        default_listbox_state()
