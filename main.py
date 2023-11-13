from tkinter import Tk, Canvas
from grid import Grid
from human import human


root = Tk()
canvas= Canvas(root, width=800,height=600)
canvas.pack()
grid=Grid(canvas)
grid.display()
p1=human(canvas, 'Inokentiy', 100, 300, 'м')
p1.display()

p2=human(canvas, 'Masha', 400, 300, 'ж')
p2.display()
root.mainloop()