from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('450x200')
root.resizable(width=False, height=False)
root.title('Sign In')

email_label = Label(root, text='Email Address:', font='Poppins 10')
email_label.place(x=15, y=15)

email_entry = ttk.Entry(root, width=35, font='Inter 15')
email_entry.place(x=15, y=45)

pw_label = Label(root, text='Password:', font='Poppins 10')
pw_label.place(x=15, y=80)

pw_entry = ttk.Entry(root, width=35, font='Inter 15')
pw_entry.place(x=15, y=110)

bt = Button(root, width=48, height=1, text='Login', font='Inter 10')
bt.place(x=14, y=150)

if __name__ == '__main__':
    root.mainloop()