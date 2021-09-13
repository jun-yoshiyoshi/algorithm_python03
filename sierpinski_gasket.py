import tkinter


def tri(x, y, s):
    h = s*1.732/2
    cvs.create_line(x - s / 2, y - h / 2, x + s / 2, y - h / 2, fill="green")
    cvs.create_line(x - s / 2, y - h / 2, x, y + h / 2, fill="green")
    cvs.create_line(x + s / 2, y - h / 2, x, y + h / 2, fill="green")
    if s > 10:
        tri(x, y - h / 2 - h / 4, s / 2)
        tri(x - s / 2, y + h / 4, s / 2)
        tri(x + s / 2, y + h / 4, s / 2)


root = tkinter.Tk()
root.title("シェルピンスキーのギャスケット")
cvs = tkinter.Canvas(width=800, height=800, bg="white")
cvs.pack()
tx, ty, si = 400, 400, 600
he = si*1.732/2
cvs.create_line(tx, ty - he/2, tx-si/2, ty+he/2, tx+si/2, ty+he/2, tx, ty-he/2, fill="blue")

tri(tx, ty+he/4, si/2)
root.mainloop()
