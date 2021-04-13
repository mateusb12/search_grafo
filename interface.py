from tkinter import *
import tkinter
import time

window = Tk()
width = 1200
height = 500
window.title = "CP"
window.geometry("1500x500+300+300")

canvas = Canvas(window, width=width, height=height)
canvas.pack()

b1 = Button(window, width=5, text="Init", bg="lightblue")
b1.place(x=45, y=230)


class NodeCell:
    def __init__(self, input_canvas: Canvas, **kwargs):
        self.x = kwargs["x"]
        self.y = kwargs["y"]
        self.diameter = kwargs["diameter"]
        self.radius = self.diameter / 2
        self.thickness = kwargs["thickness"]
        self.text = kwargs["text"]

        self.x0 = self.x + self.radius
        self.x1 = self.x - self.radius
        self.y0 = self.y - self.radius
        self.y1 = self.y + self.radius

        self.canvas = input_canvas
        # self.x_velocity = kwargs["x_speed"]
        # self.y_velocity = kwargs["y_speed"]
        self.color = kwargs["color"]
        self.image = canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.color, width=self.thickness)

        self.cell_content = self.canvas.create_text(self.x, self.y, fill="darkblue",
                                                    font="Times 40 bold", text=self.text)
        self.lines = []
        if "link" in kwargs:
            self.lines.append(self.draw_connection(kwargs["link"][1], orientation=kwargs["link"][0]))

    def move(self):
        coordinates = self.get_coordinates()
        # self.canvas.move(self.image, self.x_velocity, self.y_velocity)

    def get_coordinates(self):
        return self.canvas.coords(self.image)

    def change_value(self, new_value: str):
        self.canvas.itemconfig(self.cell_content, text=new_value)

    def get_value(self):
        return self.cell_content.text

    def draw_connection(self, connection_length: int, **kwargs):
        pm = tuple()
        if kwargs["orientation"] == "right":
            pm = (self.x + self.radius, self.y, self.x + connection_length, self.y, 5)
        if kwargs["orientation"] == "left":
            pm = (self.x - self.radius, self.y, self.x - connection_length, self.y, 5)
        if kwargs["orientation"] == "up":
            pm = (self.x, self.y - self.radius, self.x, self.y - connection_length, 5)
        if kwargs["orientation"] == "down":
            pm = (self.x, self.y + self.radius, self.x, self.y + connection_length, 5)

        self.lines.append(canvas.create_line(pm[0], pm[1], pm[2], pm[3], width=pm[4]))


node1 = NodeCell(canvas, x=400, y=250, diameter=80, thickness=3, color="white", text="A", link=("right", 200))

# while True:
#     window.update()
#     time.sleep(0.01)

window.mainloop()
