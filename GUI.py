from tkinter import Tk, Label, Button

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Proyecto 5")
        master.geometry("260x280")

        #Tamaño de los Botones
        self.buttonWidth = 14
        self.buttonHeight = 2

        #Tamaño de los Labels
        self.labelWidth = 8
        self.labelHeight = 2

        #Tamañ∩o de los Fillers
        self.fillerWidth = 2
        self.fillerHeight = 2

        #Buttons
        self.button1 = Button(master, text = "Boton 1", width = self.buttonWidth, height = self.buttonHeight)
        self.button2 = Button(master, text = "Boton 2", width = self.buttonWidth, height = self.buttonHeight)
        self.button3 = Button(master, text = "Boton 3", width = self.buttonWidth, height = self.buttonHeight)

        #Labels
        self.labelx0 = Label(master, text = "x_0", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx1 = Label(master, text = "x_1", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx2 = Label(master, text = "x_2", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx3 = Label(master, text = "x_3", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx4 = Label(master, text = "x_4", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx5 = Label(master, text = "x_5", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx6 = Label(master, text = "x_6", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        
        self.labelv0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        #Filler
        self.filler0 = Label(master, background = "white", width = self.fillerWidth, height = self.fillerHeight)

        #Display Buttons
        self.button1.grid(row = 0, column = 0)
        self.button2.grid(row = 3, column = 0)
        self.button3.grid(row = 6, column = 0)

        #Display Filler
        self.filler0.grid(row = 0, column = 1)

        #Display Labels
        self.labelx0.grid(row = 0, column = 2)
        self.labelx1.grid(row = 1, column = 2)
        self.labelx2.grid(row = 2, column = 2)
        self.labelx3.grid(row = 3, column = 2)
        self.labelx4.grid(row = 4, column = 2)
        self.labelx5.grid(row = 5, column = 2)
        self.labelx6.grid(row = 6, column = 2)

        self.labelv0.grid(row = 0, column = 3)
        self.labelv1.grid(row = 1, column = 3)
        self.labelv2.grid(row = 2, column = 3)
        self.labelv3.grid(row = 3, column = 3)
        self.labelv4.grid(row = 4, column = 3)
        self.labelv5.grid(row = 5, column = 3)
        self.labelv6.grid(row = 6, column = 3)



if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    