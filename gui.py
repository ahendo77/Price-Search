from tkinter import *
import tkinter as tk
from tkinter.constants import LEFT, RIGHT, TOP


# GUI window 

def main():

    # About menu section 
    def about():
        about = tk.Toplevel(window)
        about.title("About")
        about.geometry("300x300")
        about.config(bg="white")
        label1 = tk.Label(about, text="Price-Search (C) Copyright Alex Henderson 2021", bg="white")
        label1.pack()

    # Main window
    window = tk.Tk()
    window.geometry('1000x600')
    window.configure(background='white')
    

    window.title('Price Search')

    label1 = tk.Label(master = window, text= 'Price Search', font = ('Arial', 13), fg = 'black', bg = 'white')
    label1.place(x=5, y=5)
    

    frame1 = tk.Frame(master=window, width=1500, height=700)
    #frame1.pack(side=RIGHT)

    frame2 = tk.Frame(master=window, width=1500, height=700)
    #frame2.pack(side=LEFT)

    # Create menu bar 
    menubar = tk.Menu(window)
    window.config(menu=menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label='About', command=about)
    menubar.add_cascade(label='Menu', menu=filemenu)

    window.mainloop()



if __name__ == '__main__':
    main()