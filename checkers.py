import tkinter as tk
win=tk.Tk()
canvas = tk.Canvas(win,bg="#fff", width=400 , height=400)
for minions in range(0 ,8):
    canvas.create_line(50*minions, 0, 50*minions, 400, fill="#000")
    canvas.create_line(0, 50*minions, 400, 50*minions, fill="#000")
for i in range(8):
    for j in range(3):
        if (i+j) % 2 == 0:
            canvas.create_oval((i*50,j*50), ((i+1)*50,((j+1)*50)), fill="blue")
    for j in range(5,8):
        if (i+j) % 2 == 0:
            canvas.create_oval((i*50,j*50), ((i+1)*50,((j+1)*50)), fill="pink")
canvas.pack()
win.mainloop()
