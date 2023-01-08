from tkinter import *


class SelectMenuArticles(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        self.geometry("1030x600+500+200")
        self.title("Artykuły")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        # Frames
        self.topFrame = Frame(self, height=150, width=700)
        self.topFrame.pack()

        self.downFrame = Frame(self, height=500, bg='white')
        self.downFrame.pack(fill=X)

        self.centerLabel = Frame(self, height=500, width=600, bg='#FAFAFA', borderwidth=4, relief='groove')
        self.centerLabel.place(x=20, y=150)

        # Headings
        heading1 = Label(self.topFrame, text='MONOGRAFIE ŁUPKA MIEDZIONOŚNEGO', font='arial 14')
        heading1.place(x=135, y=10)

        heading2 = Label(self.downFrame, text='Lista artykułów', font='arial 14', bg='white')
        heading2.place(x=850, y=15)

        # lists and scrollbars
        self.listOfArticles = Listbox(self.centerLabel, height=20, width=120, font='times 12', bg='#FAFAFA',
                                      cursor="hand2")
        self.listOfArticles.grid(sticky=N, row=0, column=0, padx=(5, 21), pady=(5, 17))
        self.rightScrollbar = Scrollbar(self.centerLabel, orient="vertical")
        self.downScrollbar = Scrollbar(self.centerLabel, orient="horizontal")
        self.rightScrollbar.grid(row=0, column=0, pady=(0, 17), sticky=N+S+E)
        self.downScrollbar.grid(row=0, column=0, sticky=S+W+E)
        self.listOfArticles.config(yscrollcommand=self.rightScrollbar.set, xscrollcommand=self.downScrollbar.set)
        self.downScrollbar.config(command=self.listOfArticles.xview)
        self.rightScrollbar.config(command=self.listOfArticles.yview)
