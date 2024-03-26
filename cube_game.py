import tkinter as tk
import random

def move_player(event):
    if event.keysym == 'w':
        canvas.move( player, 0, -20)
    if event.keysym == 'a':
        canvas.move( player, -20, 0)
    if event.keysym == 's':
        canvas.move( player, 0, 20)
    if  event.keys == 'd':
        canvas.move( player, 20, 0)


def create_point():
    global point
    point_pos = (random.randint(1, 350), random.randint(1, 350))
    point= canvas.create_oval(point_pos[0], point_pos[1], point_pos[0] + 50, point_pos[1] + 50, fill='#6A5ACD')

def restart_game():
    global canvas, player
    start_pos = (random.randint( 1, 350), random.randint( 1, 350))
    player = canvas.create_rectangle(start_pos[0], start_pos[1], start_pos[0] + 50, start_pos[1] + 50, fill='#ff0')
    restart_bt.config(state="disabled")
    create_point()

root = tk.Tk()
root.title("My game")
root.geometry("400x450")

label_score =tk.Label(root, text="Inginirium!")
restart_bt =tk.Button(root, text="Start", command=restart_game)
canvas = tk.Canvas(root,  width=400, height=400, bg='#fff')

player = ''
point = ''
label_score.pack()
restart_bt.pack()
canvas.pack()
root.bind('<KeyPress>', move_player)
root.mainloop()