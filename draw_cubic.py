import tkinter


def cubic(a, b, c, d, col):
    x = -1
    while x < 4:
        y = a * x * x*x + b * x*x + c*x+d
        x2 = x + 0.1
        y2 = a * x2 * x2 * x2 + b * x2 * x2 + c * x2 + d

        cx = x * 30 + ox
        cy = oy - y * 30
        cx2 = x2 * 30 + ox
        cy2 = oy - y2 * 30
        cvs.create_line(cx, cy, cx2, cy2, fill=col)
        x += 0.1


root = tkinter.Tk()
root.title("三次曲線")
cvs = tkinter.Canvas(width=800, height=800, bg="white")
cvs.pack()

ox, oy = 400, 400
cvs.create_text(ox + 20, oy + 15, text="(0,0)")
cvs.create_line(ox, 0, ox, 800, fill="gray")
cvs.create_line(0, oy, 800, oy, fill="gray")
for x in range(0, 800, 10):
    cvs.create_line(x, oy - 2, x, oy + 3, fill="silver")

cubic(1, -4, -2, 8, "green")
root.mainloop()
