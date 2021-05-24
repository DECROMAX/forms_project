from tkinter import *
import pandas as pd


def submit_fields():
    path = r"C:\Users\rjlyn\Desktop\Scaffold_Tkinter_test.csv"
    df = pd.read_csv(path)
    series_a = df['Scaffold ID']
    series_b = df['Location']
    a = pd.Series(entry1.get())
    b = pd.Series(entry2.get())
    series_a = series_a.append(a)
    series_b = series_b.append(b)
    df1 = pd.DataFrame({"Scaffold ID": series_a, 'Location': series_b})
    df1.to_csv(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)


master = Tk()

Label(master, text='Scaffold ID').grid(row=0)
Label(master, text='Location').grid(row=1)

entry1 = Entry(master)
entry2 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=3, column=1, pady=4)

mainloop()
