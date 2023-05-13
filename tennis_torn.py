from tkinter import *
import mysql.connector as c

sql = c.connect(host='localhost', user='root', password='Noelk@24', database="noel")
cur = sql.cursor()

root = Tk()
root.geometry('800x700')                                            # Window Created
lhead = Label(root, text='Tournament', font='aerial 30')
lhead.grid(row=0, column=2)
win_1 = ''
w_1=0
w_2=0
w_3=0
w_4=0
com=0
f_win1=0
f_win2=0
def l1():
    global w_1
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=4, column=3)
    w_1 = win_1

def l2():
    global w_2
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=8, column=3)
    w_2 = win_1

def l3():
    global w_3
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=12, column=3)
    w_3 = win_1

def l4():
    global w_4
    w_4 = win_1
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=16, column=3)

    bw1 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match_w1)
    bw1.grid(row=6, column=4)
    bw2 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match_w2)
    bw2.grid(row=14, column=4)
def l5():
    global f_win1
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=6, column=6, padx=15)
    f_win1 = win_1
def l6():
    global f_win2
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=14, column=6, padx=15)
    f_win2 = win_1
    but_4 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match_f)
    but_4.grid(row=10, column=7, padx=10)
def l7():
    lab_win = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    lab_win.grid(row=10, column=8, padx=15)




def game_score(pl_1, pl_2):                                                  # Score Board
    score = Tk()
    score.geometry('400x300')
    buttonframe = Frame(score)
    # score of P-1

    global a
    global c
    global b
    global x
    global y
    global z
    global w_1
    global w_2
    global w_3
    global w_4
    a = 0
    b = 0
    c = 0
    # score of P-2
    x = 0
    y = 0
    z = 0

    def sr():
        global com
        global c
        global b
        global a
        global z
        global x
        global y
        global win_1
        if (a < 3):
            if (b < 6):
                if (c == 0):
                    c = 15
                    lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + '15', font='aerial 20')
                    lsr1.grid(row=0, column=1)

                elif (c == 15):
                    c = 30
                    lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + '30', font='aerial 20')
                    lsr1.grid(row=0, column=1)

                elif (c == 30):
                    c = 40
                    lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + '40', font='aerial 20')
                    lsr1.grid(row=0, column=1)

                elif (c == 40 and z == 40):
                    c = 'AD'
                    lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                    lsr1.grid(row=0, column=1)
                elif (c == 40 and z == 'AD'):
                    z = 40
                    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                    lsr2.grid(row=1, column=1)

                elif (c == 'AD' or c == 40):
                    c = 0
                    z = 0
                    b += 1
                    if (b != 6):
                        lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                        lsr1.grid(row=0, column=1)
                        lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                        lsr2.grid(row=1, column=1)
                    if (b == 6):
                        b = 0
                        y = 0
                        a += 1
                        if (a == 3):
                            lwin = Label(score, text=pl_1, font='aerial 30')
                            lwin.grid(row=3, column=0, pady=10)
                            win_1 = pl_1
                            if (com==1):
                                l1()
                            elif (com==2):
                                l2()
                            elif(com==3):
                                l3()
                            elif(com==4):
                                l4()
                            elif(com==5):
                                l5()
                            elif(com==6):
                                l6()
                            elif(com==7):
                                l7()
                        else:
                            lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                            lsr1.grid(row=0, column=1)
                            lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                            lsr2.grid(row=1, column=1)
                else:
                    return 0


    def wr():
        global x
        global y
        global z
        global a
        global b
        global c
        global win_1
        if (x < 3):
            if (y < 6):
                if (z == 0):
                    z = 15
                    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + '15', font='aerial 20')
                    lsr2.grid(row=1, column=1)

                elif (z == 15):
                    z = 30
                    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + '30', font='aerial 20')
                    lsr2.grid(row=1, column=1)

                elif (z == 30):
                    z = 40
                    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + '40', font='aerial 20')
                    lsr2.grid(row=1, column=1)

                elif (c == 40 and z == 40):
                    z = 'AD'
                    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                    lsr2.grid(row=1, column=1)
                elif (z == 40 and c == 'AD'):
                    c = 40
                    lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                    lsr1.grid(row=0, column=1)
                # elif(z=='AD'):

                elif (z == 'AD' or z == 40):
                    z = 0
                    c = 0
                    y += 1
                    if (y != 6):
                        lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                        lsr2.grid(row=1, column=1)
                        lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                        lsr1.grid(row=0, column=1)
                    if (y == 6):
                        y = 0
                        b = 0
                        x += 1
                        if (x == 3):
                            lwin = Label(score, text=pl_2, font='aerial 30')
                            lwin.grid(row=3, column=0, pady=10)
                            win_1 = pl_2
                            if (com==1):
                                l1()
                            elif (com==2):
                                l2()
                            elif(com==3):
                                l3()
                            elif(com==4):
                                l4()
                            elif(com == 5):
                                l5()
                            elif(com == 6):
                                l6()
                        else:
                            lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
                            lsr2.grid(row=1, column=1)
                            lsr1 = Label(score, text=str(a) + ':' + str(b) + ':' + str(c), font='aerial 20')
                            lsr1.grid(row=0, column=1)
                else:
                    return 0
        return win_1



    q = str(a)
    w = str(b)
    e = str(c)

    lpl1 = Label(score, text=pl_1, font='aerial 20')
    lpl1.grid(row=0, column=0, pady=10)
    lsr1 = Label(score, text=q + ':' + w + ':' + e, font='aerial 20')
    lsr1.grid(row=0, column=1)

    lpl2 = Label(score, text=pl_2, font='aerial 20')
    lpl2.grid(row=1, column=0, pady=10)
    lsr2 = Label(score, text=str(x) + ':' + str(y) + ':' + str(z), font='aerial 20')
    lsr2.grid(row=1, column=1)

    butp1 = Button(score, text=pl_1, fg='white', bg='black', command=sr)
    butp1.grid(row=0, column=2, padx=20)

    butp2 = Button(score, text=pl_2, fg='white', bg='black', command=wr)
    butp2.grid(row=1, column=2, padx=20)


def start_match1():
    global win_1
    global w_1
    global com
    com=1

    game_score(pl[0], pl[1])
    #return com
def start_match2():
    global win_2
    global w_2
    global com
    com=2
    game_score(pl[2], pl[3])
def start_match3():
    global win_3
    global w_3
    global com
    com=3
    game_score(pl[4], pl[5])
def start_match4():
    global win_4
    global w_4
    global com
    com=4
    game_score(pl[6], pl[7])

def start_match_w1():
    global w_1
    global w_2
    global com
    com=5
    game_score(w_1,w_2)
   # l_w_1 = Label(root, text=win_1, fg='White', bg='Black', font='imperial 20 bold')
    #l_w_1.grid(row=6, column=5)
def start_match_w2():
    global w_3
    global w_4
    global com
    com=6
    game_score(w_3,w_4)
def start_match_f():
    global f_win1
    global f_win2
    global com
    com = 7
    game_score(f_win1, f_win2)



cur.execute('select name from players')                             # Extracting player names from DB
player = cur.fetchall()
pl=[]
k = 0
for i in player:
    pl.append(i)

for s in range(len(pl)):
    label = Label(text = pl[s], fg='White', bg='Black', font='imperial 18 bold')
    label.grid(row=3 + k, column=0, pady=10)
    k += 2

but_1 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match1)
but_1.grid(row=4, column=1, padx=10)
but_2 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match2)
but_2.grid(row=8, column=1, padx=10)
but_3 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match3)
but_3.grid(row=12, column=1, padx=10)
but_4 = Button(text='Start Match!', fg='Black', bg='Green', font='courier 10', command=start_match4)
but_4.grid(row=16, column=1, padx=10)

label_1 = Label(text='----------')
label_1.grid(row=6, column=1)
label_2 = Label(text='----------')
label_2.grid(row=10, column=1)
label_3 = Label(text='----------')
label_3.grid(row=14, column=1)





root.mainloop()