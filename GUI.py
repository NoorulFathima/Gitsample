from tkinter import *
from tkinter import filedialog


# create Window object
class Window(Tk):

    def __init__(self):
        super().__init__()
        # window's look
        root = Frame(self)
        root.grid()
        self.title('Diary')
        self.iconbitmap('D:\python\git\h.ico')
        self.geometry('500x500')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # calling other classes(frames) in tkinter window by storing them in dictionaries
        self.pages = {}

        for i in (Page1, Page2):
            frame = i(root, self)
            frame.config(background='black', highlightbackground='#3D3C3A', highlightthickness=15)

            self.pages[i] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

        self.show_frame(Page1)

    # Bringing up frames
    def show_frame(self, cont):
        global ans, no
        frame = self.pages[cont]
        frame.tkraise()
        # Text to be shown from user's input
        if cont == Page2:
            ans, no, mon = self.pages[Page1].save_values()
            p = Label(self.pages[Page2], font=('Bold', 20))
            p['text'] = 'Hello ' + ans + ','
            p.pack()
            p1 = Label(self.pages[Page2], font=('Bold', 20))
            p1['text'] = no + ' - ' + mon
            p1.place(x=1200, y=700)
            self.pages[Page2].text_space.insert(INSERT, no + ' - ' + mon + '\n\n')
            self.pages[Page2].text_space.insert(INSERT,'Life of ' + ans + ',' )


class Page1(Frame):

    def __init__(self, root, parent):
        super().__init__()

        # Welcome page
        head = Label(self, text="", font=('Bold', 20))
        head.pack(pady=20, padx=800)
        head = Label(self, text="Memories... ", font=('Bold', 20))
        head.pack(pady=25)
        head = Label(self, text="Enter your name and current year ", font=('Bold', 20))
        head.pack(pady=50)

        head = Label(self, text='Name ', font=('Bold', 20))
        head.pack(pady=10)
        self.name = Entry(self, font=('Bold', 20), bg='yellow')
        self.name.pack()

        year = Label(self, text='Year', font=('Bold', 20))
        year.pack(pady=10)
        self.year1 = Entry(self, font=('Bold', 20), bg='yellow')
        self.year1.pack()

        month = Label(self, text='Month', font=('Bold', 20))
        month.pack(pady=10)
        self.month1 = Entry(self, font=('Bold', 20), bg='yellow')
        self.month1.pack()

        click = Button(self, text='Next', font=('Bold', 20), command=lambda: parent.show_frame(Page2))
        click.pack(pady=35)

    def save_values(self):
        name_print = self.name.get()
        year1_print = self.year1.get()
        month_print = self.month1.get()
        return name_print, year1_print, month_print


class Page2(Frame):
    def __init__(self, root, parent):
        super().__init__()

        # Text page
        global name
        name = False

        self.text_space = Text(self, height=20, width=80, font=('Bold', 20), selectbackground='yellow',
                               selectforeground='black')
        self.text_space.place(x=60, y=50)

        self.pic_button = Button(self, text='Open',font=('Bold', 15), command=lambda: self.file_open())
        self.pic_button.place(x=1350, y=200)

        self.pic_button = Button(self, text='Save',font=('Bold', 15), command=lambda: self.save())
        self.pic_button.place(x=1350, y=300)

        self.pic_button = Button(self, text='Save as',font=('Bold', 15), command=lambda: self.save_as())
        self.pic_button.place(x=1350, y=400)

        self.pic_button = Button(self, text='Clear',font=('Bold', 15), command=lambda: self.clear())
        self.pic_button.place(x=1350, y=500)

        self.pic_button = Button(self, text='Back',font=('Bold', 15), command=lambda: parent.show_frame(Page1))
        self.pic_button.place(x=1350, y=600)

    def file_open(self):
        file1 = filedialog.askopenfilename(initialdir='D:/documents', title='Open a file',
                                           filetypes=(('Text files', '*.txt'),
                                                      ('all files', '*.*')))
        if file1:
            global name
            name = file1
        file = open(file1, 'r')
        stuff = file.read()
        self.text_space.delete('1.0', END)
        self.text_space.insert(END, stuff)
        file.close()

    def save_as(self):
        file = filedialog.asksaveasfilename(defaultextension='.txt', initialdir='D:/documents', title='Save as',
                                            filetypes=(('Text files', '*.txt'),
                                                       ('all files', '*.*')))
        file = open(file, 'w')
        file.write(self.text_space.get(1.0, END))
        file.close()

    def save(self):
        global name
        if name:
            file = open(name, 'w')
            file = open('sample.txt', 'w')
            file.write(self.text_space.get(1.0, END))
            file.close()
        else:
            self.save_as()

    def clear(self):
        self.text_space.delete('1.0', END)


opening = Window()
opening.mainloop()
