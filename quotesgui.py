#!usr/bin/env python
import Tkinter
from Tkinter import *
from urllib import urlretrieve

master= Tkinter.Tk()
master.wm_title("Share Value Finder")
master.geometry('500x200')
symbol=StringVar(master)
#data=StringVar(master)

frame=Frame()

label = Tkinter.Label(master, text='Enter NASDAQ Symbol:')
label.pack()
label=Tkinter.Label(master,text='')
label.pack()
#mack=StringVar(master)
e=Entry(master,textvariable=symbol)
e.pack()
e.focus_set()
label2=Tkinter.Label(text='')
label2.pack()

label1=Tkinter.Label(master,text='Enter the Symbol And Press Submit Button')
label1.pack()

frame.pack()


"""urlretrieve('http://download.finance.yahoo.com/d/quotes.csv?s= %s&f=l1'% i,'quotes.csv')
f=open('quotes.csv','r')
data=f.read()
label = Tkinter.Label(master, text=data )
label.pack()
"""
def callback():
    symbol=e.get()
    label1.config(text='Please Wait.....')
    label1.update()
    try:
        urlretrieve('http://download.finance.yahoo.com/d/quotes.csv?s=%s  &f=l1'%(symbol) ,'quotes.csv')
        f=open('quotes.csv','r')
        data=float(f.read())
        result="The Current Share Value for the given NASDAQ symbol is%f" %(data)
        f.close()
    except:
        result="No Internet Connection"

    label1.config(text=result)
    label1.update()
    #f.close()

frame2=Frame()

b= Button(master,text="Submit", width=10,command=callback)
b.pack(padx=100,side=LEFT)
b2=Button(master,text="Exit",width=10,command=master.quit)
b2.pack(side=LEFT)

frame2.pack()

Tkinter.mainloop()