from tkinter import *
import mysql.connector as c

sql = c.connect(host='localhost', user='root', password='Noelk@24', database="noel")
cur = sql.cursor()

root = Tk()
root.geometry('800x600')
lhead = Label(root, text='Tournament', font='aerial 30')
lhead.grid(row=0, column=1)
lab = Label(root, text='(Click on the winner to enter the next round)')
lab.grid(row=0, column=2)


def b1():
    global but1

    def win1():
        # global but1
        def winner():
            global but1
            but1['state'] = DISABLED
            but1 = Button(text=a[0], fg='black', bg='gold')
            but1.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but1
        but1['state'] = DISABLED
        but1 = Button(text=a[0], fg='white', bg='black', command=winner)
        but1.grid(row=6, column=3)
        but3['state'] = DISABLED
        but4['state'] = DISABLED

    # global but2
    but2['state'] = DISABLED
    but1['state'] = DISABLED
    but1 = Button(text=a[0], fg='white', bg='black', command=win1)
    but1.grid(row=4, column=2)


def b2():
    global but2

    def win1():
        def winner():
            global but2
            but2['state'] = DISABLED
            but2 = Button(text=a[1], fg='black', bg='gold')
            but2.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but1['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but2
        but2['state'] = DISABLED
        but2 = Button(text=a[1], fg='white', bg='black', command=winner)
        but2.grid(row=6, column=3)
        but3['state'] = DISABLED
        but4['state'] = DISABLED

    but1['state'] = DISABLED
    but2['state'] = DISABLED
    but2 = Button(text=a[1], fg='white', bg='black', command=win1)
    but2.grid(row=4, column=2)


def b3():
    global but3

    def win1():
        def winner():
            global but3
            but3['state'] = DISABLED
            but3 = Button(text=a[2], fg='black', bg='gold')
            but3.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but1['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but3
        but3['state'] = DISABLED
        but3 = Button(text=a[2], fg='white', bg='black', command=winner)
        but3.grid(row=6, column=3)
        but1['state'] = DISABLED
        but2['state'] = DISABLED

    but4['state'] = DISABLED
    but4['state'] = DISABLED
    but3['state'] = DISABLED
    but3 = Button(text=a[2], fg='white', bg='black', command=win1)
    but3.grid(row=8, column=2)


def b4():
    global but4

    def win1():
        def winner():
            global but4
            but4['state'] = DISABLED
            but4 = Button(text=a[3], fg='black', bg='gold')
            but4.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but1['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but4
        but4['state'] = DISABLED
        but4 = Button(text=a[3], fg='white', bg='black', command=winner)
        but4.grid(row=6, column=3)
        but1['state'] = DISABLED
        but2['state'] = DISABLED

    but3['state'] = DISABLED
    but4['state'] = DISABLED
    but4 = Button(text=a[3], fg='white', bg='black', command=win1)
    but4.grid(row=8, column=2)


def b5():
    global but5

    def win1():
        def winner():
            global but5
            but5['state'] = DISABLED
            but5 = Button(text=a[4], fg='black', bg='gold')
            but5.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but1['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but5
        but5['state'] = DISABLED
        but5 = Button(text=a[4], fg='white', bg='black', command=winner)
        but5.grid(row=14, column=3)
        but7['state'] = DISABLED
        but8['state'] = DISABLED

    but6['state'] = DISABLED
    but5['state'] = DISABLED
    but5 = Button(text=a[4], fg='white', bg='black', command=win1)
    but5.grid(row=12, column=2)


def b6():
    global but6

    def win1():
        def winner():
            global but6
            but6['state'] = DISABLED
            but6 = Button(text=a[5], fg='black', bg='gold')
            but6.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but1['state'] = DISABLED
            but7['state'] = DISABLED
            but8['state'] = DISABLED

        global but6
        but6['state'] = DISABLED
        but6 = Button(text=a[5], fg='white', bg='black', command=winner)
        but6.grid(row=14, column=3)
        but7['state'] = DISABLED
        but8['state'] = DISABLED

    but5['state'] = DISABLED
    but6['state'] = DISABLED
    but6 = Button(text=a[5], fg='white', bg='black', command=win1)
    but6.grid(row=12, column=2)


def b7():
    global but7

    def win1():
        def winner():
            global but7
            but7['state'] = DISABLED
            but7 = Button(text=a[6], fg='black', bg='gold')
            but7.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but1['state'] = DISABLED
            but8['state'] = DISABLED

        global but7
        but7['state'] = DISABLED
        but7 = Button(text=a[6], fg='white', bg='black', command=winner)
        but7.grid(row=14, column=3)
        but5['state'] = DISABLED
        but6['state'] = DISABLED

    but8['state'] = DISABLED
    but7['state'] = DISABLED
    but7 = Button(text=a[6], fg='white', bg='black', command=win1)
    but7.grid(row=16, column=2)


def b8():
    global but8

    def win1():
        def winner():
            global but8
            but8['state'] = DISABLED
            but8 = Button(text=a[7], fg='black', bg='gold')
            but8.grid(row=10, column=5, padx=10)
            lab_x = Label(text='---')
            lab_x.grid(row=10, column=4)
            l_ch = Label(text='Champion', font='courier 14')
            l_ch.grid(row=10, column=6)

            but2['state'] = DISABLED
            but3['state'] = DISABLED
            but4['state'] = DISABLED
            but5['state'] = DISABLED
            but6['state'] = DISABLED
            but7['state'] = DISABLED
            but1['state'] = DISABLED

        global but8
        but8['state'] = DISABLED
        but8 = Button(text=a[7], fg='white', bg='black', command=winner)
        but8.grid(row=14, column=3)
        but5['state'] = DISABLED
        but6['state'] = DISABLED

    but7['state'] = DISABLED
    but8['state'] = DISABLED
    but8 = Button(text=a[7], fg='white', bg='black', command=win1)
    but8.grid(row=16, column=2)


cur.execute('select name from players')
pl = cur.fetchall()

a = []
for x in pl:
    a.append(x)

but1 = Button(text=a[0], fg='white', bg='black', command=b1)
but1.grid(row=3, column=0, pady=10, padx=10)

but2 = Button(text=a[1], fg='white', bg='black', command=b2)
but2.grid(row=5, column=0, pady=10, padx=10)

but3 = Button(text=a[2], fg='white', bg='black', command=b3)
but3.grid(row=7, column=0, pady=10, padx=10)

but4 = Button(text=a[3], fg='white', bg='black', command=b4)
but4.grid(row=9, column=0, pady=10, padx=10)

but5 = Button(text=a[4], fg='white', bg='black', command=b5)
but5.grid(row=11, column=0, pady=10, padx=10)

but6 = Button(text=a[5], fg='white', bg='black', command=b6)
but6.grid(row=13, column=0, pady=10, padx=10)

but7 = Button(text=a[6], fg='white', bg='black', command=b7)
but7.grid(row=15, column=0, pady=10, padx=10)

but8 = Button(text=a[7], fg='white', bg='black', command=b8)
but8.grid(row=17, column=0, pady=10, padx=10)
#k = 0
for i in [4,8,12,16]:
    label = Label(text='Round-1')
    label.grid(row=i, column=1)
    #k += 2
for x in [6,10,14]:
    label = Label(text='    |')
    label.grid(row=x, column=1)

root.mainloop()
