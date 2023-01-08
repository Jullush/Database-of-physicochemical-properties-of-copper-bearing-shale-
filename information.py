from tkinter import *
from PIL import Image, ImageTk
import information
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
global image_to_show_monograph


class Information(Toplevel):
    def __init__(self):

        Toplevel.__init__(self)

        # arrow
        information.image_to_show_monograph = Image.open('app_icons/arrow.png')
        arrow_image_resized = information.image_to_show_monograph.resize((25, 25))
        information.image_to_show_monograph = ImageTk.PhotoImage(arrow_image_resized)
        information.image_to_show_monograph.image = information.image_to_show_monograph

        # class
        self.geometry("400x500+500+200")
        self.title("Informacje")
        self.resizable(False, False)
        self.iconbitmap('app_icons/mainicon.ico')
        self.focus_set()
        self.grab_set()

        # Frames
        self.topFrame = Frame(self, height=75, width=500, borderwidth=4, relief="sunken")
        self.topFrame.pack()
        self.downFrame = Frame(self, height=500, bg='#FAFAFA')
        self.downFrame.pack(fill=X)
        self.centerLabel = Frame(self, height=380, width=360, bg='#FAFAFA', borderwidth=4, relief='groove')
        self.centerLabel.place(x=20, y=100)

        heading1 = Label(self.topFrame, text="Informacje", font='arial 14')
        heading1.place(x=145, y=20)

        # lists and scrollbars
        self.textFrame = Text(self.centerLabel, height=26, width=43, padx=2, pady=2)
        self.right_scrollbar = Scrollbar(self.centerLabel)
        self.right_scrollbar.pack(side=RIGHT, fill=Y)
        self.right_scrollbar.config(command=self.textFrame.yview, cursor="hand2")
        self.textFrame.pack()
        self.textFrame.config(yscrollcommand=self.right_scrollbar.set)
        button_exit = Button(self.topFrame, image=information.image_to_show_monograph, command=self.destroy,
                             cursor="hand2")
        button_exit.place(x=30, y=20)

        article_to_get = 'article_documents/instrukcje.pdf'
        list_of_pages = []

        def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
            while proper_number_of_blank_lines > 0:
                self.textFrame.delete("end-1 line")
                proper_number_of_blank_lines -= 1

        def get_pdf_file_content(path_to_pdf, number_of_page):
            resource_manager = PDFResourceManager(caching=True)
            out_text = StringIO()
            la_params = LAParams()
            text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
            fp = open(path_to_pdf, 'rb')
            interpreter = PDFPageInterpreter(resource_manager, text_converter)
            for page_number, page in enumerate(
                    PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='', caching=True,
                                      check_extractable=True)):
                if page_number == number_of_page:
                    interpreter.process_page(page)

            list_of_pages.insert(number_of_page, out_text.getvalue())
            fp.close()
            text_converter.close()
            out_text.close()

            return list_of_pages[number_of_page]

        text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
        self.textFrame.tag_configure("center", justify='center')
        self.textFrame.insert(1.0, text_page_1)
        deleting_blank_lines_at_the_end(20)
        self.textFrame.configure(font=("lucida Console", 10), state=DISABLED, cursor='arrow')
