from tkinter import*
from tkinter import messagebox
import sudoku as s

win = Tk()
win.title('Sudoku')
win.geometry('1110x765+800+50')
win.configure(bg='lightblue')
win.resizable(False, False)
#win.iconbitmap("sud.jpg")

sample_board = [[3, 9, 0, 0, 5, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 5], [0, 0, 0, 7, 1, 9, 0, 8, 0],
                [0, 5, 0, 0, 6, 8, 0, 0, 0], [2, 0, 6, 0, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 4],
                [5, 0, 0, 0, 0, 0, 0, 0, 0], [6, 7, 0, 1, 0, 5, 0, 4, 0], [1, 0, 9, 0, 0, 0, 2, 0, 0]]

board = [[0 for i in range(9)] for i in range(9)]

def sample():
    for i in range(9):
        for j in range(9):
            ents[i][j].config(state="normal")
            ents[i][j].delete(0, END)
            if sample_board[i][j] != 0:
                ents[i][j].insert(0, sample_board[i][j])
    sets()

def sets():
    for i in range(9):
        for j in range(9):
            x = ents[i][j].get()
            if x != '':
                board[i][j] = x
                if board[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    board[i][j] = int(x)
                    ents[i][j].delete(0, END)
                    ents[i][j].insert(0, f" {x}")
                    ents[i][j].config(state="disabled")
                else:
                    board[i][j] = 0
                    messagebox.showerror(title="Invalid Input", message=f"At Row : {i + 1},\n Column : {j + 1}.")
    clearb.config(state="normal")
    checkb.config(state="normal")
    solveb.config(state="normal")
    setb.config(state="disabled")
    s.solve(board)

def clr():
    for i in range(9):
        for j in range(9):
            ents[i][j].delete(0, END)
    uncheck()

def show():
    for i in range(9):
        for j in range(9):
            ents[i][j].delete(0, END)
            ents[i][j].insert(0, f' {board[i][j]}')

def check():
    for i in range(9):
        for j in range(9):
            e = ents[i][j]
            num = e.get()
            if num == '':
                pass
            elif int(num) != board[i][j]:
                ents[i][j].config({"background": "indianred2"})
    uncheckb.config(state="normal")
    checkb.config(state="disabled")

def uncheck():  
    for i in range(9):
        for j in range(9):
            e = ents[i][j]
            e.config({"background": "white"})
    uncheckb.config(state="disabled")
    checkb.config(state="normal")

def reset():
    for i in range(9):
        for j in range(9):
            ents[i][j].config(state="normal")
            ents[i][j].delete(0, END)
            ents[i][j].config({"background": "white"})
            board[i][j] = 0
    setb.config(state="normal")
    uncheckb.config(state="disabled")
    checkb.config(state="disabled")
    clearb.config(state="disabled")
    solveb.config(state="disabled")

ents = [[0 for i in range(9)]for i in range(9)]
yc = 15
cs = 79

for j in range(9):
    xc = 15
    if j % 3 == 0:
        yc += 4
    for i in range(9):
        if i % 3 == 0:
            xc += 4
        e = Entry(win, font=('Arial', 50))
        e.place(x=xc, y=yc, width=cs, height=cs)
        ents[j][i]=e
        xc += cs
    yc += cs

Label(win, text='Sudoku', font=('Arial', 45, 'bold'), bg='lightblue', fg='black').place(x=825, y=30)
Label(win, text='Solver', font=('Arial', 25, 'bold'), bg='lightblue', fg='black').place(x=945, y=90)
setb = Button(win, text='Submit your board', font='Arial 15', activebackground = '#ba78a4', width=21, height=2, bg='white', command=sets)
setb.place(x=820, y= 440)
checkb = Button(win, text='Check', font=('Arial', 15), width=10, height=2,activebackground = '#ba78a4', bg='white', state="disabled", command=check)
checkb.place(x=820, y=513)
clearb = Button(win, text='Clear', font=('Arial', 15), width=21, height=2,activebackground = '#ba78a4', bg='white', state="disabled", command=clr)
clearb.place(x=820, y=600)
uncheckb = Button(win, text='Uncheck', font=('Arial', 15), width=10, height=2, bg='white',activebackground = '#ba78a4', state="disabled", command=uncheck)
uncheckb.place(x=940, y=513)
Button(win, text='Quit', font=('Arial', 15), width=21, height=2,activebackground = '#ba78a4', bg='white', command=win.quit).place(x=820, y=664)
Button(win, text='Create your board', font=('Arial', 15), width=21, height=2, bg='white',activebackground = '#ba78a4', command=reset).place(x=820, y=377)
solveb = Button(win, text='Solve', font=('Arial', 15),activebackground = '#ba78a4', width=21, height=2, bg='white', state="disabled", command=show)
solveb.place(x=820, y=300)
sample()
win.mainloop()