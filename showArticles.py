from tkinter import *
import sqlite3
import showMonografie
import openArticle


co = sqlite3.connect('monograph_db.db')
c = co.cursor()

global text_to_highlight


def cleaning_the_author_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.author = str(db_data_2)


def cleaning_the_title_data(x):
    db_data_1 = str(x)
    db_data_2 = db_data_1.translate(({ord(b): None for b in "[()]"}))
    openArticle.title = str(db_data_2)


def showArticle(self):
    showMonografie.ShowMonografie()


def displayMonograph1(x):
    text_to_highlight = ""
    articles = c.execute("SELECT authors,title,publication_date FROM articles_1 WHERE key_id < 1420").fetchall()
    count = 0
    x.listOfArticles.delete(0, END)
    x.listOfArticles.insert(END, "\n")

    def showArticle_(x, y):
        openArticle.article_key_number = x
        openArticle.text_to_highlight = y
        openArticle.OpenArticle()

    for article in articles:
        x.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + " Ł.M I, " + str(article[2]))
        count += 1

    def display_the_art(evt):

        if x.listOfArticles.curselection() != ():
            value = str(x.listOfArticles.get(x.listOfArticles.curselection()))
            id = value.split(' - ')[1]
            # print(id)
            article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?", (id,))
            article_to_find_key_id = article_to_find.fetchall()
            article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
            article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(({ord(b): None for
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
            showArticle_(article_key_id, text_to_highlight)

    x.listOfArticles.bind('<<ListboxSelect>>', display_the_art)


def displayMonograph2(x):
    text_to_highlight = ""
    articles = c.execute("SELECT authors,title, publication_date "
                         "FROM articles_1 "
                         "WHERE key_id < 1638 AND key_id > 1420").fetchall()
    count = 0
    x.listOfArticles.delete(0, END)
    x.listOfArticles.insert(END, "\n")

    for article in articles:
        x.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + " Ł.M II, " + str(article[2]))
        count = count + 1

    def showArticle_(x, y):
        openArticle.article_key_number = x
        openArticle.text_to_highlight = y
        openArticle.OpenArticle()

    def display_the_art(evt):

        if x.listOfArticles.curselection() != ():
            value = str(x.listOfArticles.get(x.listOfArticles.curselection()))
            id = value.split(' - ')[1]
            # print(id)
            article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?",(id,))
            article_to_find_key_id = article_to_find.fetchall()
            article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
            article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(({ord(b): None for
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
            showArticle_(article_key_id,text_to_highlight)

    x.listOfArticles.bind('<<ListboxSelect>>', display_the_art)


def displayMonograph3(x):
    text_to_highlight = ""
    articles = c.execute("SELECT authors,title, publication_date "
                         "FROM articles_1 "
                         "WHERE key_id < 1720 AND key_id >1638").fetchall()
    count = 0
    x.listOfArticles.delete(0, END)
    x.listOfArticles.insert(END, "\n")

    def showArticle_(x, y):
        openArticle.article_key_number = x
        openArticle.text_to_highlight = y
        openArticle.OpenArticle()

    for article in articles:
        x.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + " Ł.M III, " + str(article[2]))
        count += 1

    def display_the_art(evt):

        if x.listOfArticles.curselection() != ():
            value = str(x.listOfArticles.get(x.listOfArticles.curselection()))
            id = value.split(' - ')[1]
            # print(id)
            article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?", (id,))
            article_to_find_key_id = article_to_find.fetchall()
            article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
            article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(({ord(b): None for
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
            showArticle_(article_key_id,text_to_highlight)

    x.listOfArticles.bind('<<ListboxSelect>>', display_the_art)


def displayMonograph4(x):
    text_to_highlight = ""
    articles = c.execute("SELECT authors,title,publication_date date "
                         "FROM articles_1 "
                         "WHERE key_id < 1830 AND key_id > 1720").fetchall()
    count = 0
    x.listOfArticles.delete(0, END)

    for article in articles:
        x.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + " Ł.M IV, " + str(article[2]))
        count = count + 1

    def showArticle_(x,y):
        openArticle.article_key_number = x
        openArticle.text_to_highlight = y
        openArticle.OpenArticle()

    def display_the_art(evt):

        if x.listOfArticles.curselection() != ():
            value = str(x.listOfArticles.get(x.listOfArticles.curselection()))
            id = value.split(' - ')[1]
            # print(id)
            article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?", (id,))
            article_to_find_key_id = article_to_find.fetchall()
            article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
            article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(({ord(b): None for
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
            showArticle_(article_key_id,text_to_highlight)

    x.listOfArticles.bind('<<ListboxSelect>>', display_the_art)


def displayMonograph5(x):
    text_to_highlight = ""
    articles = c.execute("SELECT authors,title, publication_date "
                         "FROM articles_1 "
                         "WHERE key_id < 2116 AND key_id > 1817").fetchall()
    count = 0
    x.listOfArticles.delete(0, END)

    for article in articles:
        x.listOfArticles.insert(count, article[0] + " - " + article[1] + " - " + " Ł.M V, " + str(article[2]))
        count = count + 1

    def showArticle_(x,y):
        openArticle.article_key_number = x
        openArticle.text_to_highlight = y
        openArticle.OpenArticle()

    def display_the_art(evt):

        if x.listOfArticles.curselection() != ():
            value = str(x.listOfArticles.get(x.listOfArticles.curselection()))
            id = value.split(' - ')[1]
            # print(id)
            article_to_find = c.execute("SELECT key_id FROM articles_1 WHERE title=?",(id,))
            article_to_find_key_id = article_to_find.fetchall()
            article_to_find_key_id_to_translate_1 = str(article_to_find_key_id)
            article_to_find_key_id_to_translate_2 = article_to_find_key_id_to_translate_1.translate(({ord(b): None for
                                                                                                      b in "[(,)]"}))
            article_key_id = int(article_to_find_key_id_to_translate_2)
            title_of_article = c.execute("SELECT title FROM articles_1 WHERE key_id=?", (article_key_id,))
            title_of_article_ready = title_of_article.fetchall()
            cleaning_the_title_data(title_of_article_ready)

            if len(openArticle.title) > 30:
                openArticle.title = openArticle.title.split(" ")
                openArticle.title.insert(8, "\n")
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
            showArticle_(article_key_id, text_to_highlight)

    x.listOfArticles.bind('<<ListboxSelect>>', display_the_art)






