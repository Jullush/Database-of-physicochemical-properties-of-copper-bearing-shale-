from tkinter import *
import showArticles


class ShowMonografie(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("1030x600+500+200")
        self.title("Monografie")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        # Frames
        self.topFrame = Frame(self, height=150, width=800)
        self.topFrame.pack()

        self.downFrame = Frame(self, height=500, bg='white')
        self.downFrame.pack(fill=X)

        self.centerLabel = Frame(self, height=500, width=600, bg='#FAFAFA', borderwidth=4, relief='groove')
        self.centerLabel.place(x=20, y=150)


        # Headings
        heading1 = Label(self.topFrame, text='MONOGRAFIE ŁUPKA MIEDZIONOŚNEGO', font='arial 14')
        heading1.place(x=235, y=10)

        heading2 = Label(self.downFrame, text='Lista artykułów', font='arial 14', bg='white')
        heading2.place(x=850, y=15)

        # lists and scrollbars
        self.listOfArticles = Listbox(self.centerLabel, height=20, width=120, font='times 12', bg='#FAFAFA')
        self.listOfArticles.grid(sticky=N, row=0, column=0, padx=(5, 21), pady=(5, 17))
        self.rightScrollbar = Scrollbar(self.centerLabel, orient="vertical")
        self.downScrollbar = Scrollbar(self.centerLabel, orient="horizontal")
        self.rightScrollbar.grid(row=0, column=0, pady=(0, 17), sticky=N+S+E)
        self.downScrollbar.grid(row=0, column=0, sticky=S+W+E)
        self.listOfArticles.config(yscrollcommand=self.rightScrollbar.set, xscrollcommand=self.downScrollbar.set)
        self.downScrollbar.config(command=self.listOfArticles.xview)
        self.rightScrollbar.config(command=self.listOfArticles.yview)

        # Buttons
        monograph1 = Button(self.topFrame, text='Monografia I 2014', font='arial 12',
                            command=self.showArticlesInMonograph1)
        monograph1.place(x=150, y=45)

        monograph2 = Button(self.topFrame, text='Monografia II 2016', font='arial 12',
                            command=self.showArticlesInMonograph2)
        monograph2.place(x=350, y=45)

        monograph3 = Button(self.topFrame, text='Monografia III 2017', font='arial 12',
                            command=self.showArticlesInMonograph3)
        monograph3.place(x=550, y=45)

        monograph4 = Button(self.topFrame, text='Monografia IV 2018', font='arial 12',
                            command=self.showArticlesInMonograph4)
        monograph4.place(x=250, y=100)

        monograph5 = Button(self.topFrame, text='Monografia V 2021', font='arial 12',
                            command=self.showArticlesInMonograph5)
        monograph5.place(x=450, y=100)

        self.Button_exit = Button(self.topFrame, text='Cofnij', font='arial 12', command=self.destroy)
        self.Button_exit.place(x=0, y=70)

    def showArticlesInMonograph1(self):
        showArticles.displayMonograph1(self)

    def showArticlesInMonograph2(self):
        showArticles.displayMonograph2(self)

    def showArticlesInMonograph3(self):
        showArticles.displayMonograph3(self)

    def showArticlesInMonograph4(self):
        showArticles.displayMonograph4(self)

    def showArticlesInMonograph5(self):
        showArticles.displayMonograph5(self)





