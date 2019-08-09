import os, sys
import tkinter as tk
from tkinter import messagebox
from modulos.menu_function import *
sys.path.append('..')
from functions import *
from system_var import *

#os.chdir("..")
sysVar=VariablesSystemas()
Job=FunctionsClass()

class AppGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Archivo Detectado, Correccion de nombre")
        self.master.resizable(1,1)
        self.master.geometry("650x350+100+200")  #  FOMRA QUE ME GUSTA ...PARA DAR TAMANO Y POSICION  OJO  ES AL MAIN FORM NO AL FRAME
        self.master.attributes("-topmost",True)

        Job.OutPrint("entre en el root")
        
        os.chdir("..")
        #sysVar=VariablesSystemas()
        _Instdir=sysVar.VarInstalationDir()
        _Ldir="{}{}".format(_Instdir,"/AppGetName")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        _archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/image/",_archivoIMGname)
        self.master.iconbitmap(_archivoIMG)

        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)
        Frame0 = Frame(master, bg="yellow")
        Frame0.grid(row = 0, column = 0, rowspan = 1, columnspan = 6, sticky = W+E+N+S)

        Frame1 = Frame(master, bg="red")
        Frame1.grid(row = 1, column = 0, rowspan = 5, columnspan = 3, sticky = W+E+N+S)

        Frame2 = Frame(master, bg="blue")
        Frame2.grid(row = 5, column = 3, rowspan = 3, columnspan = 3, sticky = W+E+N+S)

        Frame3 = Frame(master, bg="green")
        Frame3.grid(row = 1, column = 3, rowspan = 4, columnspan = 3, sticky = W+E+N+S)

        ##  CONSTRUCCION DEL OBJETOs-MENU QUE SERAN USDADOS PARA EJECUTAR LAS LLAMADAS DEL MENU ###
        objetosMenu=function_menuBar()

        def mainFrame2_visible():
            mainFrame.pack_forget()
            mainFrame1.pack_forget()
            mainFrame2.pack(side="top", fill="both", expand=True)
            
        def mainFrame1_visible():
            mainFrame.pack_forget()
            mainFrame2.pack_forget()
            mainFrame1.pack(side="top", fill="both", expand=True)


        ###     construccion del menu   ####
        menuBar=Menu(self.master)
        #806533537 telefono de vidente espanola
        #construccion del menu base de datos

        #construccion del menu help
        helpmenu=Menu(menuBar, tearoff=0)
        helpmenu.add_command(label="About",command=objetosMenu.mabout)
        helpmenu.add_command(label="Help")


        menuBar.add_cascade(label="About",menu=helpmenu)

        ### ensamblado del menu en el main form
        AppGui.config(menu=menuBar)

        ###     construccion de los main frame      ####

        mainFrame=Frame(self.master,
                         borderwidth=2,
                         relief=GROOVE,
                         width="650",
                         height="350"
                        )
        mainFrame.pack(side="top", fill="both", expand=True)

        mainFrame1=Frame(self.master,
                         borderwidth=2,
                         relief=GROOVE,
                         bg="blue",
                         width="650",
                         height="350"
                        )
        # mainFrame1.attributes('-alpha',1)
        mainFrame1.pack(padx=2, pady=2, side="top", fill="both", expand=True)
        mainFrame1.pack_forget()

        mainFrame2=Frame(self.master,
                         borderwidth=2,
                         relief=GROOVE,
                         bg="red",
                         width="650",
                         height="350"
                        )
        # mainFrame2.attributes('-alpha',1)
        mainFrame2.pack(padx=2, pady=2,side="top", fill="both", expand=True)
        mainFrame2.pack_forget()
    

        


root = Tk()
app = AppGUI(master=root)
app.mainloop()