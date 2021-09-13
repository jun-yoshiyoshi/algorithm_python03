import tkinter
import math

x, y, l, a = 20, 300, 760, 0


def koch(n):
    global x, y, l, a
    if n > 0:
        l /= 2
        koch(n - 1)
        a += 60
        koch(n - 1)
        a -= 120
        koch(n - 1)
        a += 60
        koch(n - 1)
        l *= 2

    else:
        nx = x + l * math.cos(math.radians(a))
        ny = y - l * math.sin(math.radians(a))
        cvs.create_line(x, y, nx, ny)
        x, y = nx, ny


root = tkinter.Tk()
root.title("コッホ曲線")
cvs = tkinter.Canvas(width=800, height=400, bg="white")
cvs.pack()
koch(6)
root.mainloop()
