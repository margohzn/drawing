from tkinter import * 
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = "black"

    def __init__(self):
        self.window = Tk()
        self.pen_button = Button(self.window, text = "Pen", command = self.use_pen)
        self.brush_button = Button(self.window, text = "Brush", command = self.use_brush)
        self.color_button = Button(self.window, text = "Color", command = self.change_color)
        self.eraser_button = Button(self.window, text = "Eraser", command = self.use_eraser)
        self.change_size = Scale(self.window, from_ = 1, to = 10 , orient = HORIZONTAL) 
        self.canvas = Canvas(self.window, bg = "white", width = 600, height = 600)

        self.pen_button.grid(row = 1, column = 1, padx = 20)
        self.brush_button.grid(row = 1, column = 2)
        self.color_button.grid(row = 1, column = 3, padx = 20)
        self.eraser_button.grid(row = 1, column = 4)
        self.change_size.grid(row = 1, column = 5, padx = 20)
        self.canvas.grid(row = 2, column = 1, columnspan = 5)

        self.setup()
        self.window.mainloop()

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def change_color(self):
        self.eraser_on = False
        self.color = askcolor(color = self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, erase_mode = True)
    
    def activate_button(self, any_button, eraser_mode = False):
        self.active_button.config(relief = RAISED)
        any_button.config(relief = SUNKEN)
        self.active_button = any_button
        self.erase_on = eraser_mode

    def setup(self):
        self.previouse_x = None
        self.previouse_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button

Paint()


