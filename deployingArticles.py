from tkinter import *
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
import openArticle


def deploying_article_1(self):

    temp_articles_dictionary = {
        1: 'article_documents/1401.pdf',
        2: 'article_documents/1402.pdf'
    }

    images_1401 = {
        1: PhotoImage(file="article_photos/1401_photos/1401_1.gif"),
        2: PhotoImage(file="article_photos/1401_photos/1401_2.gif"),
        3: PhotoImage(file="article_photos/1401_photos/1401_3.gif"),
        4: PhotoImage(file="article_photos/1401_photos/1401_4.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    # 1401

    text_page_1 = get_pdf_file_content(path_to_pdf=temp_articles_dictionary[1], number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=temp_articles_dictionary[1], number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=temp_articles_dictionary[1], number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=temp_articles_dictionary[1], number_of_page=3)

    self.textFrame.image = images_1401
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(25)
    adding_image(images_1401[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(60)
    adding_space(2)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1401[2])
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(35)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1401[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(60)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_2(self):

    article_to_get = 'article_documents/1402.pdf'

    images_1402 = {
        1: PhotoImage(file="article_photos/1402_photos/1402_1.gif"),
        2: PhotoImage(file="article_photos/1402_photos/1402_2.gif"),
        3: PhotoImage(file="article_photos/1402_photos/1402_3.gif"),
        4: PhotoImage(file="article_photos/1402_photos/1402_4.gif"),
        5: PhotoImage(file="article_photos/1402_photos/1402_5.gif"),
        6: PhotoImage(file="article_photos/1402_photos/1402_6.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    # 1401

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images_1402
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(13)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1402[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(60)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1402[2])
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(100)
    adding_image(images_1402[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(88)
    self.textFrame.insert(END, " ", "center")
    adding_image(images_1402[4])
    adding_space(2)
    adding_image(images_1402[5])
    adding_space(2)
    self.textFrame.insert(END, " ", "center")
    adding_image(images_1402[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(15)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_3(self):

    article_to_get = "article_documents/1403.pdf"

    images_1403 = {
        1: PhotoImage(file="article_photos/1403_photos/1403_1.gif"),
        2: PhotoImage(file="article_photos/1403_photos/1403_2.gif"),
        3: PhotoImage(file="article_photos/1403_photos/1403_3.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    # 1403

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)

    self.textFrame.image = images_1403
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(48)
    adding_image(images_1403[1])
    adding_space(3)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images_1403[2])
    adding_space(3)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1403[3])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_4(self):

    article_to_get = "article_documents/1404.pdf"

    images_1404 = {
        1: PhotoImage(file="article_photos/1404_photos/1404_1.gif"),
        2: PhotoImage(file="article_photos/1404_photos/1404_2.gif"),
        3: PhotoImage(file="article_photos/1404_photos/1404_3.gif"),
        4: PhotoImage(file="article_photos/1404_photos/1404_4.gif"),
        5: PhotoImage(file="article_photos/1404_photos/1404_5.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)

    self.textFrame.image = images_1404
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(5)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images_1404[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images_1404[2])
    adding_space(2)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1404[3])
    adding_space(2)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1404[4])
    adding_space(2)
    self.textFrame.insert(END, "  ", "center")
    adding_image(images_1404[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_5(self):

    article_to_get = "article_documents/1405.pdf"

    images = {
        1: PhotoImage(file="article_photos/1405_photos/1405_1.gif"),
        2: PhotoImage(file="article_photos/1405_photos/1405_2.gif"),
        3: PhotoImage(file="article_photos/1405_photos/1405_3.gif"),
        4: PhotoImage(file="article_photos/1405_photos/1405_4.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(50)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(86)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(85)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    adding_image(images[4])
    adding_space(3)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_6(self):

    article_to_get = "article_documents/1406.pdf"

    images = {
        1: PhotoImage(file="article_photos/1406_photos/1406_1.gif"),
        2: PhotoImage(file="article_photos/1406_photos/1406_2.gif"),
        3: PhotoImage(file="article_photos/1406_photos/1406_3.gif"),
        4: PhotoImage(file="article_photos/1406_photos/1406_4.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(30)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_7(self):

    article_to_get = "article_documents/1407.pdf"

    images = {
        1: PhotoImage(file="article_photos/1407_photos/1407_1.gif"),
        2: PhotoImage(file="article_photos/1407_photos/1407_2.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(8)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(83)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_8(self):

    article_to_get = "article_documents/1408.pdf"

    images = {
        1: PhotoImage(file="article_photos/1408_photos/1408_1.gif"),
        2: PhotoImage(file="article_photos/1408_photos/1408_2.gif"),
        3: PhotoImage(file="article_photos/1408_photos/1408_3.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(70)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(10)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_9(self):

    article_to_get = "article_documents/1409.pdf"

    images = {
        1: PhotoImage(file="article_photos/1409_photos/1409_1.gif"),
        2: PhotoImage(file="article_photos/1409_photos/1409_2.gif"),
        3: PhotoImage(file="article_photos/1409_photos/1409_3.gif"),
        4: PhotoImage(file="article_photos/1409_photos/1409_4.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(86)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(50)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(85)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(10)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_10(self):

    article_to_get = "article_documents/1410.pdf"

    images = {
        1: PhotoImage(file="article_photos/1410_photos/1410_1.gif"),
        2: PhotoImage(file="article_photos/1410_photos/1410_2.gif"),
        3: PhotoImage(file="article_photos/1410_photos/1410_3.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(19)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(1)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(82)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_12(self):

    article_to_get = "article_documents/1412.pdf"

    images = {
        1: PhotoImage(file="article_photos/1412_photos/1412_1.gif"),
        2: PhotoImage(file="article_photos/1412_photos/1412_2.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(10)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(66)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_11(self):

    article_to_get = "article_documents/1411.pdf"

    images = {
        1: PhotoImage(file="article_photos/1411_photos/1411_1.gif"),
        2: PhotoImage(file="article_photos/1411_photos/1411_2.gif"),
        3: PhotoImage(file="article_photos/1411_photos/1411_3.gif"),
        4: PhotoImage(file="article_photos/1411_photos/1411_4.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(83)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(1)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(1)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(83)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_13(self):

    article_to_get = "article_documents/1413.pdf"

    images = {
        1: PhotoImage(file="article_photos/1413_photos/1413_1.gif"),
        2: PhotoImage(file="article_photos/1413_photos/1413_2.gif"),
        3: PhotoImage(file="article_photos/1413_photos/1413_3.gif"),
        4: PhotoImage(file="article_photos/1413_photos/1413_4.gif"),
        5: PhotoImage(file="article_photos/1413_photos/1413_5.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(84)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(39)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(3)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(73)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(76)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_14(self):

    article_to_get = "article_documents/1414.pdf"

    images = {
        1: PhotoImage(file="article_photos/1414_photos/1414_1.gif"),
        2: PhotoImage(file="article_photos/1414_photos/1414_2.gif"),
        3: PhotoImage(file="article_photos/1414_photos/1414_3.gif")

    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(40)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(62)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(1)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_15(self):
    article_to_get = "article_documents/1415.pdf"
    images = {
        1: PhotoImage(file="article_photos/1415_photos/1415_1.gif"),
        2: PhotoImage(file="article_photos/1415_photos/1415_2.gif"),
        3: PhotoImage(file="article_photos/1415_photos/1415_3.gif"),
        4: PhotoImage(file="article_photos/1415_photos/1415_4.gif"),
        5: PhotoImage(file="article_photos/1415_photos/1415_5.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(48)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(90)
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(88)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(44)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_16(self):
    article_to_get = "article_documents/1416.pdf"
    images = {
        1: PhotoImage(file="article_photos/1416_photos/1416_1.gif"),
        2: PhotoImage(file="article_photos/1416_photos/1416_2.gif"),
        3: PhotoImage(file="article_photos/1416_photos/1416_3.gif"),
        4: PhotoImage(file="article_photos/1416_photos/1416_4.gif"),
        5: PhotoImage(file="article_photos/1416_photos/1416_5.gif"),
        6: PhotoImage(file="article_photos/1416_photos/1416_6.gif"),
        7: PhotoImage(file="article_photos/1416_photos/1416_7.gif"),
        8: PhotoImage(file="article_photos/1416_photos/1416_8.gif"),
        9: PhotoImage(file="article_photos/1416_photos/1416_9.gif"),
        10: PhotoImage(file="article_photos/1416_photos/1416_10.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=10, password=''
                                                             ,caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)
    text_page_7 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=6)
    text_page_8 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=7)
    text_page_9 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=8)
    text_page_10 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=9)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(23)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(62)
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(83)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(95)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(90)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_7)
    deleting_blank_lines_at_the_end(92)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, text_page_8)
    deleting_blank_lines_at_the_end(92)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[8])
    adding_space(2)
    self.textFrame.insert(END, text_page_9)
    deleting_blank_lines_at_the_end(60)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[9])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[10])
    adding_space(2)
    self.textFrame.insert(END, text_page_10)
    deleting_blank_lines_at_the_end(50)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_17(self):
    article_to_get = "article_documents/1417.pdf"
    images = {
        1: PhotoImage(file="article_photos/1417_photos/1417_1.gif"),
        2: PhotoImage(file="article_photos/1417_photos/1417_2.gif"),
        3: PhotoImage(file="article_photos/1417_photos/1417_3.gif"),
        4: PhotoImage(file="article_photos/1417_photos/1417_4.gif"),
        5: PhotoImage(file="article_photos/1417_photos/1417_5.gif"),
        6: PhotoImage(file="article_photos/1417_photos/1417_6.gif"),
        7: PhotoImage(file="article_photos/1417_photos/1417_7.gif"),
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=10, password=''
                , caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(25)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(66)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(40)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(5)
    self.textFrame.insert(END, "   ", "center")

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_18(self):

    article_to_get = "article_documents/1418.pdf"

    images = {
        1: PhotoImage(file="article_photos/1418_photos/1418_1.gif"),
        2: PhotoImage(file="article_photos/1418_photos/1418_2.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(29)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(1)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(10)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_19(self):

    article_to_get = "article_documents/1419.pdf"

    images = {
        1: PhotoImage(file="article_photos/1419_photos/1419_1.gif"),
        2: PhotoImage(file="article_photos/1419_photos/1419_2.gif"),
        3: PhotoImage(file="article_photos/1419_photos/1419_3.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=7, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(24)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(65)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_20(self):
    article_to_get = "article_documents/1601.pdf"
    images = {
        1: PhotoImage(file="article_photos/1601_photos/1601_1.gif"),
        2: PhotoImage(file="article_photos/1601_photos/1601_2.gif"),
        3: PhotoImage(file="article_photos/1601_photos/1601_3.gif"),
        4: PhotoImage(file="article_photos/1601_photos/1601_4.gif"),
        5: PhotoImage(file="article_photos/1601_photos/1601_5.gif"),
        6: PhotoImage(file="article_photos/1601_photos/1601_6.gif"),
        7: PhotoImage(file="article_photos/1601_photos/1601_7.gif"),
        8: PhotoImage(file="article_photos/1601_photos/1601_8.gif"),
        9: PhotoImage(file="article_photos/1601_photos/1601_9.gif"),
        10: PhotoImage(file="article_photos/1601_photos/1601_10.gif"),
        11: PhotoImage(file="article_photos/1601_photos/1601_11.gif"),
        12: PhotoImage(file="article_photos/1601_photos/1601_12.gif"),
        13: PhotoImage(file="article_photos/1601_photos/1601_13.gif"),
        14: PhotoImage(file="article_photos/1601_photos/1601_14.gif"),
        15: PhotoImage(file="article_photos/1601_photos/1601_15.gif"),
        16: PhotoImage(file="article_photos/1601_photos/1601_16.gif"),
        17: PhotoImage(file="article_photos/1601_photos/1601_17.gif"),
        18: PhotoImage(file="article_photos/1601_photos/1601_18.gif"),
        19: PhotoImage(file="article_photos/1601_photos/1601_19.gif"),
        20: PhotoImage(file="article_photos/1601_photos/1601_20.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=20, password=''
                                                             ,caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)
    text_page_7 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=6)
    text_page_8 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=7)
    text_page_9 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=8)
    text_page_10 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=9)
    text_page_11 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=10)
    text_page_12 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=11)
    text_page_13 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=12)
    text_page_14 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=13)
    text_page_15 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=14)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(40)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(0)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(10)
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(7)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(56)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(52)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(38)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[8])
    adding_space(2)
    self.textFrame.insert(END, text_page_7)
    deleting_blank_lines_at_the_end(4)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[9])
    adding_space(2)
    self.textFrame.insert(END, text_page_8)
    deleting_blank_lines_at_the_end(3)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[10])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[11])
    adding_space(2)
    self.textFrame.insert(END, text_page_9)
    deleting_blank_lines_at_the_end(54)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[12])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[13])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[14])
    adding_space(2)
    self.textFrame.insert(END, text_page_10)
    deleting_blank_lines_at_the_end(69)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[15])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[16])
    adding_space(2)
    self.textFrame.insert(END, text_page_11)
    deleting_blank_lines_at_the_end(65)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[17])
    adding_space(1)
    self.textFrame.insert(END, text_page_12)
    deleting_blank_lines_at_the_end(64)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[18])
    adding_space(2)
    self.textFrame.insert(END, text_page_13)
    deleting_blank_lines_at_the_end(50)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[19])
    adding_space(2)
    self.textFrame.insert(END, text_page_14)
    deleting_blank_lines_at_the_end(1)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[20])
    adding_space(2)
    self.textFrame.insert(END, text_page_15)
    deleting_blank_lines_at_the_end(1)
    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_21(self):

    article_to_get = "article_documents/1602.pdf"

    images = {
        1: PhotoImage(file="article_photos/1602_photos/1602_1.gif"),
        2: PhotoImage(file="article_photos/1602_photos/1602_2.gif"),
        3: PhotoImage(file="article_photos/1602_photos/1602_3.gif"),
        4: PhotoImage(file="article_photos/1602_photos/1602_4.gif"),
        5: PhotoImage(file="article_photos/1602_photos/1602_5.gif"),
        6: PhotoImage(file="article_photos/1602_photos/1602_6.gif"),
        7: PhotoImage(file="article_photos/1602_photos/1602_7.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)
    text_page_7 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=6)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(1)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(71)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(60)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(30)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(1)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(85)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(1)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(1)
    self.textFrame.insert(END, "   ", "center")

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_22(self):

    article_to_get = "article_documents/1603.pdf"

    images = {
        1: PhotoImage(file="article_photos/1603_photos/1603_1.gif"),
        2: PhotoImage(file="article_photos/1603_photos/1603_2.gif"),
        3: PhotoImage(file="article_photos/1603_photos/1603_3.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(5)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(75)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(1)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(54)
    self.textFrame.insert(END, "       ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(1)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_23(self):

    article_to_get = "article_documents/1604.pdf"

    images = {
        1: PhotoImage(file="article_photos/1604_photos/1604_1.gif"),
        2: PhotoImage(file="article_photos/1604_photos/1604_2.gif"),
        3: PhotoImage(file="article_photos/1604_photos/1604_3.gif"),
        4: PhotoImage(file="article_photos/1604_photos/1604_4.gif"),
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(37)
    adding_image(images[1])
    adding_space(3)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_24(self):

    article_to_get = "article_documents/1605.pdf"

    images = {
        1: PhotoImage(file="article_photos/1605_photos/1605_1.gif"),
        2: PhotoImage(file="article_photos/1605_photos/1605_2.gif"),
        3: PhotoImage(file="article_photos/1605_photos/1605_3.gif"),
        4: PhotoImage(file="article_photos/1605_photos/1605_4.gif"),
        5: PhotoImage(file="article_photos/1605_photos/1605_5.gif")
    }

    # list_of_pages
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(10)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(20)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(37)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(67)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(54)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_25(self):

    article_to_get = "article_documents/1606.pdf"

    images = {
        1: PhotoImage(file="article_photos/1606_photos/1606_1.gif"),
        2: PhotoImage(file="article_photos/1606_photos/1606_2.gif"),
        3: PhotoImage(file="article_photos/1606_photos/1606_3.gif"),
        4: PhotoImage(file="article_photos/1606_photos/1606_4.gif"),
        5: PhotoImage(file="article_photos/1606_photos/1606_5.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(15)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(40)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(70)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_26(self):

    article_to_get = "article_documents/1607.pdf"

    images = {
        1: PhotoImage(file="article_photos/1607_photos/1607_1.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(9)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_27(self):

    article_to_get = "article_documents/1608.pdf"

    images = {
        1: PhotoImage(file="article_photos/1608_photos/1608_1.gif"),
        2: PhotoImage(file="article_photos/1608_photos/1608_2.gif"),
        3: PhotoImage(file="article_photos/1608_photos/1608_3.gif"),
        4: PhotoImage(file="article_photos/1608_photos/1608_4.gif"),
        5: PhotoImage(file="article_photos/1608_photos/1608_5.gif"),
        6: PhotoImage(file="article_photos/1608_photos/1608_6.gif")
    }

    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(82)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(55)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(78)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(44)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(17)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_28(self):

    article_to_get = "article_documents/1609.pdf"

    images = {
        1: PhotoImage(file="article_photos/1609_photos/1609_1.gif"),
        2: PhotoImage(file="article_photos/1609_photos/1609_2.gif"),
        3: PhotoImage(file="article_photos/1609_photos/1609_3.gif"),
        4: PhotoImage(file="article_photos/1609_photos/1609_4.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(18)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(12)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(65)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(57)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_29(self):

    article_to_get = "article_documents/1610.pdf"

    images = {
        1: PhotoImage(file="article_photos/1610_photos/1610_1.gif"),
        2: PhotoImage(file="article_photos/1610_photos/1610_2.gif"),
        3: PhotoImage(file="article_photos/1610_photos/1610_3.gif"),
        4: PhotoImage(file="article_photos/1610_photos/1610_4.gif"),
        5: PhotoImage(file="article_photos/1610_photos/1610_5.gif"),
        6: PhotoImage(file="article_photos/1610_photos/1610_6.gif"),
        7: PhotoImage(file="article_photos/1610_photos/1610_7.gif")
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)
    text_page_7 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=6)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(7)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(51)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(65)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(52)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(16)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(61)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, text_page_7)
    deleting_blank_lines_at_the_end(5)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_30(self):

    article_to_get = "article_documents/1611.pdf"

    images = {
        1: PhotoImage(file="article_photos/1611_photos/1611_1.gif"),
        2: PhotoImage(file="article_photos/1611_photos/1611_2.gif"),
        3: PhotoImage(file="article_photos/1611_photos/1611_3.gif"),
        4: PhotoImage(file="article_photos/1611_photos/1611_4.gif"),
        5: PhotoImage(file="article_photos/1611_photos/1611_5.gif"),
        6: PhotoImage(file="article_photos/1611_photos/1611_6.gif"),
        7: PhotoImage(file="article_photos/1611_photos/1611_7.gif")
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(77)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(42)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_31(self):

    article_to_get = "article_documents/1612.pdf"

    images = {
        1: PhotoImage(file="article_photos/1612_photos/1612_1.gif"),
        2: PhotoImage(file="article_photos/1612_photos/1612_2.gif"),
        3: PhotoImage(file="article_photos/1612_photos/1612_3.gif"),
        4: PhotoImage(file="article_photos/1612_photos/1612_4.gif"),
        5: PhotoImage(file="article_photos/1612_photos/1612_5.gif"),
        6: PhotoImage(file="article_photos/1612_photos/1612_6.gif"),
        7: PhotoImage(file="article_photos/1612_photos/1612_7.gif"),
        8: PhotoImage(file="article_photos/1612_photos/1612_8.gif")
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(45)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(26)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(67)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(35)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[6])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(35)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[7])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[8])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(1)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_32(self):

    article_to_get = "article_documents/1613.pdf"

    images = {
        1: PhotoImage(file="article_photos/1613_photos/1613_1.gif"),
        2: PhotoImage(file="article_photos/1613_photos/1613_2.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(22)
    adding_space(1)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(90)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(50)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_33(self):

    article_to_get = "article_documents/1614.pdf"

    images = {
        1: PhotoImage(file="article_photos/1614_photos/1614_1.gif"),
        2: PhotoImage(file="article_photos/1614_photos/1614_2.gif"),
        3: PhotoImage(file="article_photos/1614_photos/1614_3.gif")
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(14)
    adding_space(1)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(62)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(84)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(7)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_34(self):

    article_to_get = "article_documents/1615.pdf"

    images = {
        1: PhotoImage(file="article_photos/1615_photos/1615_1.gif"),
        2: PhotoImage(file="article_photos/1615_photos/1615_2.gif"),
        3: PhotoImage(file="article_photos/1615_photos/1615_3.gif"),
        4: PhotoImage(file="article_photos/1615_photos/1615_4.gif"),
        5: PhotoImage(file="article_photos/1615_photos/1615_5.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)
    text_page_5 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=4)
    text_page_6 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=5)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(3)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(86)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[3])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(87)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[4])
    adding_space(2)
    self.textFrame.insert(END, text_page_5)
    deleting_blank_lines_at_the_end(80)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[5])
    adding_space(2)
    self.textFrame.insert(END, text_page_6)
    deleting_blank_lines_at_the_end(2)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_35(self):

    article_to_get = "article_documents/1616.pdf"

    images = {
        1: PhotoImage(file="article_photos/1616_photos/1616_1.gif"),
        2: PhotoImage(file="article_photos/1616_photos/1616_2.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(30)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(20)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(57)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(30)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_36(self):

    article_to_get = "article_documents/1617.pdf"

    images = {
        1: PhotoImage(file="article_photos/1617_photos/1617_1.gif"),
        2: PhotoImage(file="article_photos/1617_photos/1617_2.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(92)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(72)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(6)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


def deploying_article_37(self):

    article_to_get = "article_documents/1618.pdf"

    images = {
        1: PhotoImage(file="article_photos/1618_photos/1618_1.gif"),
        2: PhotoImage(file="article_photos/1618_photos/1618_2.gif"),
    }
    list_of_pages = []

    def adding_image(y):
        self.textFrame.image_create('end', image=y)

    def deleting_blank_lines_at_the_end(proper_number_of_blank_lines):
        while proper_number_of_blank_lines > 0:
            self.textFrame.delete("end-1 line")
            proper_number_of_blank_lines -= 1

    def adding_space(proper_number_of_spaces):
        while proper_number_of_spaces > 0:
            self.textFrame.insert(END, "\n")
            proper_number_of_spaces -= 1

    def get_pdf_file_content(path_to_pdf, number_of_page):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        la_params = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)

        for page_number, page in enumerate(PDFPage.get_pages(fp, pagenos=set(), maxpages=8, password='',caching=True,
                                                             check_extractable=True)):
            if page_number == number_of_page:
                interpreter.process_page(page)

        list_of_pages.insert(number_of_page, out_text.getvalue())
        fp.close()
        text_converter.close()
        out_text.close()

        return list_of_pages[number_of_page]

    text_page_1 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=0)
    text_page_2 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=1)
    text_page_3 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=2)
    text_page_4 = get_pdf_file_content(path_to_pdf=article_to_get, number_of_page=3)

    self.textFrame.image = images
    self.textFrame.tag_configure("center", justify='center')
    self.textFrame.insert(1.0, text_page_1)
    deleting_blank_lines_at_the_end(2)
    self.textFrame.insert(END, text_page_2)
    deleting_blank_lines_at_the_end(92)
    adding_space(2)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[1])
    adding_space(2)
    self.textFrame.insert(END, text_page_3)
    deleting_blank_lines_at_the_end(72)
    self.textFrame.insert(END, "   ", "center")
    adding_image(images[2])
    adding_space(2)
    self.textFrame.insert(END, text_page_4)
    deleting_blank_lines_at_the_end(6)

    self.textFrame.configure(font=openArticle.font, state=DISABLED, cursor='arrow')


