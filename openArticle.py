from tkinter import *
import deployingArticles
import showLiterature
from PIL import ImageTk, Image

global title
global article_key_number
global author
global text_to_highlight
global boolean_to_high

font = ("times new roman", 12)


def check_if_1400(self):
    if article_key_number == 1401:
        deployingArticles.deploying_article_1(self)
    elif article_key_number == 1402:
        deployingArticles.deploying_article_2(self)
    elif article_key_number == 1403:
        deployingArticles.deploying_article_3(self)
    elif article_key_number == 1404:
        deployingArticles.deploying_article_4(self)
    elif article_key_number == 1405:
        deployingArticles.deploying_article_5(self)
    elif article_key_number == 1406:
        deployingArticles.deploying_article_6(self)
    elif article_key_number == 1407:
        deployingArticles.deploying_article_7(self)
    elif article_key_number == 1408:
        deployingArticles.deploying_article_8(self)
    elif article_key_number == 1409:
        deployingArticles.deploying_article_9(self)
    elif article_key_number == 1410:
        deployingArticles.deploying_article_10(self)
    elif article_key_number == 1411:
        deployingArticles.deploying_article_11(self)
    elif article_key_number == 1412:
        deployingArticles.deploying_article_12(self)
    elif article_key_number == 1413:
        deployingArticles.deploying_article_13(self)
    elif article_key_number == 1414:
        deployingArticles.deploying_article_14(self)
    elif article_key_number == 1415:
        deployingArticles.deploying_article_15(self)
    elif article_key_number == 1416:
        deployingArticles.deploying_article_16(self)
    elif article_key_number == 1417:
        deployingArticles.deploying_article_17(self)
    elif article_key_number == 1418:
        deployingArticles.deploying_article_18(self)
    elif article_key_number == 1419:
        deployingArticles.deploying_article_19(self)
    else:
        pass


def check_if_1600(self):
    if article_key_number == 1601:
        deployingArticles.deploying_article_20(self)
    elif article_key_number == 1602:
        deployingArticles.deploying_article_21(self)
    elif article_key_number == 1603:
        deployingArticles.deploying_article_22(self)
    elif article_key_number == 1604:
        deployingArticles.deploying_article_23(self)
    elif article_key_number == 1605:
        deployingArticles.deploying_article_24(self)
    elif article_key_number == 1606:
        deployingArticles.deploying_article_25(self)
    elif article_key_number == 1607:
        deployingArticles.deploying_article_26(self)
    elif article_key_number == 1608:
        deployingArticles.deploying_article_27(self)
    elif article_key_number == 1609:
        deployingArticles.deploying_article_28(self)
    elif article_key_number == 1610:
        deployingArticles.deploying_article_29(self)
    elif article_key_number == 1611:
        deployingArticles.deploying_article_30(self)
    elif article_key_number == 1612:
        deployingArticles.deploying_article_31(self)
    elif article_key_number == 1613:
        deployingArticles.deploying_article_32(self)
    elif article_key_number == 1614:
        deployingArticles.deploying_article_33(self)
    elif article_key_number == 1615:
        deployingArticles.deploying_article_34(self)
    elif article_key_number == 1616:
        deployingArticles.deploying_article_35(self)
    elif article_key_number == 1617:
        deployingArticles.deploying_article_36(self)
    else:
        pass


def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
    start = self.index(start)
    end = self.index(end)
    self.mark_set("matchStart", start)
    self.mark_set("matchEnd", start)
    self.mark_set("searchLimit", end)

    patterns = {
        1: str(pattern).upper(),
        2: str(pattern).lower(),
        3: str(pattern).capitalize(),
        4: str(pattern).title()
    }
    count = IntVar()
    i = 1

    for x in patterns:
        while True:
            index = self.search(patterns[i], "matchEnd", "searchLimit",
                                count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
        i = i+1


def Literature():
    showLiterature.ShowLiterature()


class OpenArticle(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("790x900+600+50")
        self.title("Article_test")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()
        self.titleLabel = Label(self, height=3, width=750, text=f"\n{author}\n{title}",
                                font='times 12 bold ', pady=25, bd=10, borderwidth=10, relief="sunken")
        self.titleLabel.pack()

        self.textFrame = Text(self, height=900, width=750, padx=65, pady=15)
        self.textFrame.tag_configure("red", foreground="red", background="#e1e1e1")
        self.right_scrollbar = Scrollbar(self)
        self.right_scrollbar.pack(side=RIGHT, fill=Y)
        self.right_scrollbar.config(command=self.textFrame.yview)
        self.textFrame.pack()
        self.textFrame.config(yscrollcommand=self.right_scrollbar.set)
        self.Button = Button(self.titleLabel, text='Literatura', font='times 12', command=Literature)
        self.Button.place(x=30, y=15)
        self.Button_exit = Button(self.titleLabel, text='Cofnij', font='times 12', command=self.destroy)
        self.Button_exit.place(x=40, y=60)

        rock_image = Image.open('app_icons/rocks.png')
        rock_image_resized = rock_image.resize((40, 40))
        rock_image_resized_rotated = rock_image_resized.rotate(180)

        rock_image_done = ImageTk.PhotoImage(rock_image_resized)
        rock_label = Label(self.titleLabel, image=rock_image_done)
        rock_label.image = rock_image_done
        rock_label.place(x=690, y=45)

        rock_image_done_2 = ImageTk.PhotoImage(rock_image_resized_rotated)
        rock_label2 = Label(self.titleLabel, image=rock_image_done_2)
        rock_label2.image = rock_image_done_2
        rock_label2.place(x=649, y=15)

        if article_key_number < 1420:
            check_if_1400(self)
        elif 1420 < article_key_number < 1640:
            check_if_1600(self)
        else:
            pass

        if highlight_pattern != "":
            highlight_pattern(self.textFrame, text_to_highlight, "red")
        else:
            pass





