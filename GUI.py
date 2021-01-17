from tkinter import Tk, Label, Button

class GUI:
    def __init__(self,master):
        self.master = master
        self.state = 0
        master.title("Proyecto 5")
        master.geometry("550x360")

        #####################################CONTAINTER DIMENSIONS#############################################################

        #Heights
        self.height = 2

        #Tamaño de los Botones
        self.buttonWidth = 14
        self.buttonHeight = self.height

        #Tamaño de los Labels
        self.labelWidth = 8
        self.labelHeight = self.height

        #Tamaño de los Fillers
        self.fillerWidth = 2
        self.fillerHeight = self.height

        #Tamaño del Funcion Label 
        self.funcionWidth = 20
        self.funcionHeight = self.height



        ######################################OBJECTS############################################################################

        #Funcion Label
        self.labelFuncion = Label(master, width = self.funcionWidth, height = self.funcionHeight)

        #Buttons
        self.button1 = Button(master, text = "Función 1", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion1_pressed())
        self.button2 = Button(master, text = "Función 2", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion2_pressed())
        self.button3 = Button(master, text = "Función 3", width = self.buttonWidth, height = self.buttonHeight, command = lambda: self.funcion3_pressed())

        #Labels
        self.labelx0 = Label(master, text = "x_0", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx1 = Label(master, text = "x_1", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx2 = Label(master, text = "x_2", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx3 = Label(master, text = "x_3", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx4 = Label(master, text = "x_4", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx5 = Label(master, text = "x_5", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelx6 = Label(master, text = "x_6", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        
        self.mejor1 = Label(master, text= "mejor 1", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.mejor2 = Label(master, text= "mejor 2", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.mejor3 = Label(master, text= "mejor 3", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.mejor4 = Label(master, text= "mejor 4", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.mejor5 = Label(master, text= "mejor 5", borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)


        self.labelv0b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b0 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b1 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b2 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b3 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)

        self.labelv0b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv1b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv2b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv3b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv4b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv5b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)
        self.labelv6b4 = Label(master, borderwidth = 2, relief = "ridge", background = "white", width = self.labelWidth, height = self.labelHeight)


        #Playback buttons
        self.startButton = Button(master, text = "START", background = "white", width = self.buttonWidth, height = self.buttonHeight)
        self.stopButton = Button(master, text = "STOP", background = "white", width = self.buttonWidth, height = self.buttonHeight)
        self.stepButton = Button(master, text = "STEP", background = "white", width = self.buttonWidth, height = self.buttonHeight)



        #Filler
        self.filler0 = Label(master, width = self.fillerWidth, height = self.fillerHeight)


        #################################DISPLAY###########################################################################

        #Display Buttons
        self.labelFuncion.grid(row = 0, column = 0)
        self.button1.grid(row = 1, column = 0)
        self.button2.grid(row = 2, column = 0)
        self.button3.grid(row = 3, column = 0)

        #Playback Buttons
        self.startButton.grid(row = 5, column = 0)
        self.stopButton.grid(row = 6, column = 0)
        self.stepButton.grid(row = 7, column = 0)


        #Display Filler
        self.filler0.grid(row = 1, column = 1)

        #Display Labels
        self.labelx0.grid(row = 1, column = 2)
        self.labelx1.grid(row = 2, column = 2)
        self.labelx2.grid(row = 3, column = 2)
        self.labelx3.grid(row = 4, column = 2)
        self.labelx4.grid(row = 5, column = 2)
        self.labelx5.grid(row = 6, column = 2)
        self.labelx6.grid(row = 7, column = 2)

        self.mejor1.grid(row = 8, column = 3)
        self.mejor2.grid(row = 8, column = 4)
        self.mejor3.grid(row = 8, column = 5)
        self.mejor4.grid(row = 8, column = 6)
        self.mejor5.grid(row = 8, column = 7)

        self.labelv0b0.grid(row = 1, column = 3)
        self.labelv1b0.grid(row = 2, column = 3)
        self.labelv2b0.grid(row = 3, column = 3)
        self.labelv3b0.grid(row = 4, column = 3)
        self.labelv4b0.grid(row = 5, column = 3)
        self.labelv5b0.grid(row = 6, column = 3)
        self.labelv6b0.grid(row = 7, column = 3)

        self.labelv0b1.grid(row = 1, column = 4)
        self.labelv1b1.grid(row = 2, column = 4)
        self.labelv2b1.grid(row = 3, column = 4)
        self.labelv3b1.grid(row = 4, column = 4)
        self.labelv4b1.grid(row = 5, column = 4)
        self.labelv5b1.grid(row = 6, column = 4)
        self.labelv6b1.grid(row = 7, column = 4)

        self.labelv0b2.grid(row = 1, column = 5)
        self.labelv1b2.grid(row = 2, column = 5)
        self.labelv2b2.grid(row = 3, column = 5)
        self.labelv3b2.grid(row = 4, column = 5)
        self.labelv4b2.grid(row = 5, column = 5)
        self.labelv5b2.grid(row = 6, column = 5)
        self.labelv6b2.grid(row = 7, column = 5)
        
        self.labelv0b3.grid(row = 1, column = 6)
        self.labelv1b3.grid(row = 2, column = 6)
        self.labelv2b3.grid(row = 3, column = 6)
        self.labelv3b3.grid(row = 4, column = 6)
        self.labelv4b3.grid(row = 5, column = 6)
        self.labelv5b3.grid(row = 6, column = 6)
        self.labelv6b3.grid(row = 7, column = 6)

        self.labelv0b4.grid(row = 1, column = 7)
        self.labelv1b4.grid(row = 2, column = 7)
        self.labelv2b4.grid(row = 3, column = 7)
        self.labelv3b4.grid(row = 4, column = 7)
        self.labelv4b4.grid(row = 5, column = 7)
        self.labelv5b4.grid(row = 6, column = 7)
        self.labelv6b4.grid(row = 7, column = 7)


    #############################FUNTIONS#######################################################

    def funcion1_pressed(self):
        self.state = 1
        self.labelFuncion["text"] = "Función 1 selecionado"
        return

    def funcion2_pressed(self):
        self.labelFuncion["text"] = "Función 2 selecionado"
        self.state = 2
        return

    def funcion3_pressed(self):
        self.labelFuncion["text"] = "Función 3 selecionado"
        self.state = 3
        return



if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
    