import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.message = tk.Label(self, height=20)
        self.message["text"] = "Hello"
 
root = tk.Tk(screenName="Setup for Bit-Build")
app = Application(master=root)
app.mainloop()