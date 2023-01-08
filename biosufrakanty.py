from tkinter import *
from PIL import ImageTk, Image
import showMonografie

class Biosufrakanty(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)
        # arrow
        showMonografie.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = showMonografie.image_to_show_monograph.resize((25, 25))
        showMonografie.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        showMonografie.image_to_show_monograph.image = showMonografie.image_to_show_monograph
        # class
        self.geometry("1100x600+600+50")
        self.title("Biosufrakanty użyte jako spieniacze")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()
        self.titleLabel = Label(self, height=1, width=750, text="Biosufrakanty użyte jako spieniacze",
                                font='times 12 bold ', pady=25, bd=10, borderwidth=10, relief="sunken")
        self.titleLabel.pack()
        self.textFrame = Text(self, height=600, width=900, padx=65, pady=15)
        self.textFrame.tag_configure("red", foreground="red", background="#e1e1e1")
        self.Button_exit = Button(self.titleLabel, image=showMonografie.image_to_show_monograph, command=self.destroy
                                  , cursor="hand2")
        self.Button_exit.place(x=20, y=20)
        self.right_scrollbar = Scrollbar(self, orient="vertical")
        self.down_scrollbar = Scrollbar(self, orient="horizontal")
        self.down_scrollbar.pack(side=BOTTOM, fill=X)
        self.right_scrollbar.pack(side=RIGHT, fill=Y)
        self.textFrame.config(xscrollcommand=self.down_scrollbar.set)
        self.right_scrollbar.config(command=self.textFrame.yview)
        self.down_scrollbar.config(command=self.textFrame.xview)
        self.textFrame.pack()
        self.textFrame.config(yscrollcommand=self.right_scrollbar.set)
        self.textFrame.configure(state=DISABLED, cursor='arrow')

        def adding_space(proper_number_of_spaces):
            while proper_number_of_spaces > 0:
                self.textFrame.insert(END, "\n")
                proper_number_of_spaces -= 1

        images = {
            1: PhotoImage(file="article_photos/biosufrakanty/Tab_1.gif"),
            2: PhotoImage(file="article_photos/biosufrakanty/Tab_2.gif"),
            3: PhotoImage(file="article_photos/biosufrakanty/Tab_3.gif")

        }
        self.textFrame.image = images
        self.textFrame.image_create('end', image=images[1])
        adding_space(2)
        self.textFrame.image_create('end', image=images[2])
        adding_space(2)
        self.textFrame.image_create('end', image=images[3])



