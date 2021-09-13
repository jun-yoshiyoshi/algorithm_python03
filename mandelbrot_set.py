import tkinter
root = tkinter.Tk()
root.title("マンデルブロー複素数による計算")
cvs = tkinter.Canvas(width=500, height=500, bg="white")
cvs.pack()

for x in range(500):
    cvs.update()
    a = -3 + 0.01 * x
    for y in range(500):
        b = -3 + 0.01 * y
        c = a + b * 1j
        z = 0
        for n in range(30):
            z = z * z + c
            if abs(z) > 2:
                cvs.create_rectangle(x, y, x, y, fill="black", width=0)
                break

cvs.create_line(250, 0, 250, 500, fill="gray")
cvs.create_line(0, 250, 500, 250, fill="gray")
root.mainloop()
