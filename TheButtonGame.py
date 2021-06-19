# This Program will create a simple GUI Using Tkinter
import tkinter as tk

# step 1 make a GUI
class App (tk.Frame):

    # step 2 set size for GUI and all other preferences like windowed/resizable
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()



        # 2 Buttons that are packed on the bottom, that say back and forth as well as a quit button
        # a shape which resembles a character
    def create_widget(self):

        self.button_pressed = tk.Button(self, height = 30, width = 30, bg = "Red")
        self.button_pressed["text"] = "Back"
        self.button_pressed["command"] = self.button_press_Back
        self.button_pressed.pack(side = "left")

        self.button_pressed = tk.Button(self, height = 30, width = 30, bg = "green")
        self.button_pressed["text"] = "Forward"
        self.button_pressed["command"] = self.button_press_Forward
        self.button_pressed.pack(side="right")

        canvas_width, canvas_height = 1800,400
        x1, y1 = canvas_width // 2, canvas_height // 2

        self.quit = tk.Button(self, text = "QUIT NOW", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")

        self.canvas = tk.Canvas(self, bg="gray", width = canvas_width, height = canvas_height)

        self.canvas.create_line(20, 360, 1780, 360)
        self.c1 = self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
        self.canvas.pack()



# Def for the button to call
    def button_press_Back(self):
        print("Button Pressed Backward")
        x = 0
        y = 0
        x = -10
        self.canvas.move(self.c1, x, y)
    def button_press_Forward(self):
        x = 0
        y = 0
        x = 10
        self.canvas.move(self.c1, x, y)
        print("Button Pressed Forward")
# Pack the GUI and Main loop it




root = tk.Tk()
app = App(master=root)
app.master.title("The Useless App")
app.master.geometry("1920x1080")
app.mainloop()




