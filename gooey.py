#!/usr/bin/python3
import os, sys
import time
import threading
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser
import coloriser
import epubcolorise

FILENAME = "Enter Filepath to epub File!"
COLOR_VALS = {
    coloriser.POS.Untagged: '#eee8d5',
    coloriser.POS.Interjection: '#eee8d5',
    coloriser.POS.Noun: '#b58900',
    coloriser.POS.Verb: '#cb4b16',
    coloriser.POS.Adjective: '#d33682',
    coloriser.POS.Adverb: '#d33682',
    coloriser.POS.Preposition: '#eee8d5',
    coloriser.POS.Article: '#eee8d5',
    coloriser.POS.Conjunction: '#eee8d5',
    coloriser.POS.Pronoun: '#eee8d5',
    coloriser.POS.Modal: '#eee8d5',
}
def alert(message, root):
    top= Toplevel(root)
    top.geometry("250x100")
    top.title("Alert")
    l = Label(top, text= message, font=('Mistral 18 bold'))
    l.pack()

class color_frame(Frame):
    curr_config = {
        coloriser.POS.Untagged: '#eee8d5',
        coloriser.POS.Interjection: '#eee8d5',
        coloriser.POS.Noun: '#b58900',
        coloriser.POS.Verb: '#cb4b16',
        coloriser.POS.Adjective: '#d33682',
        coloriser.POS.Adverb: '#d33682',
        coloriser.POS.Preposition: '#eee8d5',
        coloriser.POS.Article: '#eee8d5',
        coloriser.POS.Conjunction: '#eee8d5',
        coloriser.POS.Pronoun: '#eee8d5',
        coloriser.POS.Modal: '#eee8d5',
    }

    cb_list = []

    def __init__(self, root):
        top = Toplevel(root)
        top.geometry("1000x250")
        top.title("Colour Picker")
        Label(top, text= "Colour Picker", font=('Mistral 18 bold')).place(x=150,y=80)

        #self.curr_config = (0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF)

        #color_menu = Button(root, text ="POS_1", command = __choose_color)
        index = 0
        for key in self.curr_config:
            cb = Button(top, text=key.name, bg=self.curr_config[key])
            self.cb_list.append(cb)
            #cb.grid( row=1, column=i)
            def handler(event, self=self, key=key, index=index):
                self.__choose_color(event, key, index=index)
            cb.bind('<Button-1>', handler)
            cb.pack()
            index +=1

        def handler(self=self, top=top):
            self.__submit(top)
        submit_button = Button(top, text ="Save", command = handler)
        submit_button.pack()

    def __choose_color(self, event, key, index):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        self.curr_config[key] = color_code[1]
        self.cb_list[index].config(bg=color_code[1])

    def __submit(self, top):
        global COLOR_VALS
        COLOR_VALS = self.curr_config
        top.destroy()

class main(Frame):
    button1_val = 1
    button2_val = 1
    button3_val = 1

    def __init__(self, root):
        w = Label(root, text ='speedpub', font = "50")
        w.pack()

        self.root = root

        l = Label(root, text = FILENAME)
        l.config(font =("Courier", 14))

        l.pack()

        def handler(self=self, l=l):
            self.__fileselect(l)
        browse = Button(root, text ="Browse", command = handler)
        browse.pack()

        self.button1_val = IntVar()
        self.button2_val = IntVar()
        self.button3_val = IntVar()

        button1 = Checkbutton(root, text = "Colour Text",
                            variable = self.button1_val,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)

        button2 = Checkbutton(root, text = "Bold Text",
                            variable = self.button2_val,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)

        button3 = Checkbutton(root, text = "PLACEHOLDER",
                            variable = self.button3_val,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)

        button1.pack()
        button2.pack()
        button3.pack()

        def handler(self=self, root=root):
            self.__raise_color_picker(root)
        color_menu_button = Button(root, text ="Colour Picker", command = handler)
        color_menu_button.pack()

        submit_button = Button(root, text ="Colourise", command = self.__submit)
        submit_button.pack()
    def __fileselect(self, l):
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        if(not filename.endswith('.epub') or not os.path.exists(filename)):
            alert("Invalid Filepath!", self.root)
            return
        global FILENAME
        FILENAME = filename
        l.config(text=FILENAME)
    def __raise_color_picker(self, root):
        color_frame(root)
    def __submit(self):
        if(FILENAME == "Enter Filepath to epub File!"):
            alert("Select an epub file!", self.root)
            return
        b = epubcolorise.EpubColorise(FILENAME, './out/joe.epub')
        b.options.embolden = True if self.button2_val == 1 else False
        b.options.colors = COLOR_VALS
        b.write()
        root.destroy()

root = Tk()
root.geometry("600x300")
main(root)
root.mainloop()
