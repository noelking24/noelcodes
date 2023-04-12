# This Player Registration is for the Players to register for their participation for their tournament

from tkinter import *
import mysql.connector as c

sql= c.connect(host='localhost', user='root', password='Noelk@24', database="noel")
cur = sql.cursor()

cur.execute("delete from players")

w=Tk()
w.geometry('400x400')


label= Label(text='Player Registration', font= 'aerial 20')
label.grid(row=0, column=0)

lname= Label(text='Enter 8 Player Names', font='aerial 15')
lname.grid(row=1, column=0, padx=10, pady=10)

global x
x=0
def submit():
    global x
    lnm=Label(text=e.get(), font='aerial 12')
    lnm.grid(row=3+x, column=0)
    x=x+1
    if(x==8):
        bsubmit['state']=DISABLED
    st=("INSERT INTO players (name) VALUES (%s)")
    nm= [e.get()]
    cur.execute(st, nm)
    sql.commit()
    e.delete(0, END)



e=Entry(w)
e.grid(row=2, column=0, columnspan=10)

bsubmit= Button(text='Submit',fg='white', bg='black', command=submit)
bsubmit.grid(row=2, column=1)
w.mainloop()
