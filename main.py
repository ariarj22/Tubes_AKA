from tkinter import *
from tkinter import ttk
import random
from colors import *
from threading import Thread

# Importing algorithms
from algoritma.insertionsort import insertionsort
from algoritma.combsort import combsort

# Main window
window = Tk()
window.title("Visualisasi Algoritma Sorting")
window.maxsize(1100, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Insertion Sort', 'Comb Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data1 = []
data2 = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData1(data, colorArray):
    canvas1.delete("all")
    canvas_width = 500
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas1.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def drawData2(data, colorArray):
    canvas2.delete("all")
    canvas_width = 500
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# This function will generate array with random values every time we hit the generate button
def generate():
    global data1, data2

    data1 = []
    data2 = []
    for i in range(0, 60):
        random_value = random.randint(1, 120)
        data1.append(random_value)
        data2.append(random_value)

    drawData1(data1, [BLUE for x in range(len(data1))])
    drawData2(data2, [BLUE for x in range(len(data2))])

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.1
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0

# This funciton will trigger a selected algorithm and start sorting
def sort1():
    global data1
    timeTick = set_speed()

    insertionsort(data1, drawData1, timeTick)

def sort2():
    global data2
    timeTick = set_speed()

    combsort(data2, drawData2, timeTick)

def sort():
    p1 = Thread(target=sort1)
    p2 = Thread(target=sort2)
    p1.start();p2.start()


### User interface here ###
UI_frame1 = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame1.grid(row=0, column=0, padx=10, pady=5, sticky="E")

UI_frame2 = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame2.grid(row=0, column=1, padx=10, pady=5, sticky="W")

# dropdown to select sorting speed
l2 = Label(UI_frame1, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5)
speed_menu = ttk.Combobox(UI_frame2, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button
b1 = Button(UI_frame2, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5, sticky="W")

# button for generating array
b3 = Button(UI_frame1, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array
canvas1 = Canvas(window, width=500, height=400, bg=WHITE)
canvas1.grid(row=1, column=0, padx=10, pady=5)
t1 = Label(window, text="Insertion Sort", bg=WHITE)
t1.grid(row=2, column=0, padx=10, pady=5)

canvas2 = Canvas(window, width=500, height=400, bg=WHITE)
canvas2.grid(row=1, column=1, padx=10, pady=5)
t2 = Label(window, text="Comb Sort", bg=WHITE)
t2.grid(row=2, column=1, padx=10, pady=5)

window.mainloop()