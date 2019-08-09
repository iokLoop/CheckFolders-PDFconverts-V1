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

class fondoGUI():
    def __init__(self,var1):
        fondo=Toplevel()    
        fondo.title("VArchivo Detectado, Correccion de nombre")
        fondo.config(bg="gray")
        fondo.attributes('-alpha',0.6)
        fondo.attributes('-fullscreen',True)

        # os.chdir("..")
        # sysVar=VariablesSystemas()
        _Instdir=sysVar.VarInstalationDir()
        _Ldir="{}{}".format(_Instdir,"/AppGetName")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        _archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/image/",_archivoIMGname)

        fondo.iconbitmap(_archivoIMG)


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

        ###############################################
        #       construccion de los datos
        ###############################################
        # Label(mainFrame,image=miLogo).grid(row=1, column=0, sticky=W)
        # Label(master, text="Enter customer's Name: ").grid(row=1, column=2,sticky=W)
        # Label(master, text="Enter customer's Last Name: ").grid(row=2, column=2,sticky=W)
        # Label(master, text="Enter customer's Last 4 SSN: ").grid(row=3, column=2,sticky=W)
        # Label(master, text="Enter Document Type: ").grid(row=4, column=1,sticky=W)
        ###############################################
        #      FIN DE  construccion de los datos
        ###############################################
        ##  CONSTRUCCION DEL OBJETOs-MENU QUE SERAN USDADOS PARA EJECUTAR LAS LLAMADAS DEL MENU ###
        objetosMenu=function_menuBar()

        ###     construccion del menu   ####
        menuBar=Menu(self.master)

        #construccion del menu help
        helpmenu=Menu(menuBar, tearoff=0)
        helpmenu.add_command(label="About",command=objetosMenu.mabout)
        helpmenu.add_command(label="Help")


        menuBar.add_cascade(label="About",menu=helpmenu)

        ### ensamblado del menu en el main form
        self.master.config(menu=menuBar)

        def return_entry():
            #
            PDFname=_pdfnombre.get()
            PDFuserName=_nombre.get()
            PDFuserLast=_apellido.get()
            PDFuserNum=_social.get()
            PDFfileType=_tipo.get()
            Job.ModNames(PDFname,PDFuserName,PDFuserLast,PDFuserNum,PDFfileType)   
        
        fondo=fondoGUI(self.master)
        self.master.mainloop()


root = Tk()
app = AppGUI(master=root)