from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

import pandas as pd

blks = ('11', '11A', '8', '11B', '7A', '12', '4')

def submit_fields():
    path = r"C:\Users\User\OneDrive - Altrad\Desktop\scaffold_id.csv"
    df = pd.read_csv(path)
    series_a = df['Scaffold ID']
    series_b = df['Location']
    series_c = df['Blk']
    a = pd.Series(entry1.get())
    b = pd.Series(entry2.get())
    c = pd.Series(w.get())
    series_a = series_a.append(a)
    series_b = series_b.append(b)
    df1 = pd.DataFrame({"Scaffold ID": series_a, 'Location': series_b})
    df1.to_csv(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)


master = Tk()


Label(master, text='Scaffold ID:').grid(row=0)
Label(master, text='Location:').grid(row=1)
w = (master,  variable, "11A", "8", "11B")

entry1 = Entry(master)
entry2 = Entry(master)
entry3 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
w.grid(row=2, column=0)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=3, column=1, pady=4)

mainloop()
