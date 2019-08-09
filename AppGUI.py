import os, sys
import tkinter as tk
from tkinter import messagebox
#from modulos.menu_function import *
#from functions import *
from system_var import *

#os.chdir("..")
sysVar=VariablesSystemas()
#

class fondoGUI():
    def __init__(self,var1):
        fondo=Toplevel()    
        fondo.title("VArchivo Detectado, Correccion de nombre")
        fondo.config(bg="gray")
        fondo.attributes('-alpha',0.6)
        fondo.attributes('-fullscreen',True)

        # os.chdir("..")
        # sysVar=VariablesSystemas()
        _Instdir=sysVar.Get("VarInstalationDir")
        _Ldir="{}{}".format(_Instdir,"/AppGetName")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        _archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/imagenes/",_archivoIMGname)

        fondo.iconbitmap(_archivoIMG)

 
    

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Archivo Detectado, Correccion de nombre")
        self.resizable(1,1)
        self.geometry("650x350+100+200")  #  FOMRA QUE ME GUSTA ...PARA DAR TAMANO Y POSICION  OJO  ES AL MAIN FORM NO AL Frame
        self.attributes("-topmost",True)
        
        print("entre en el root")

        os.chdir("..")
        #sysVar=Get("VariablesSystemas")
        _Instdir=sysVar.Get("VarInstalationDir")
        _Ldir="{}{}".format(_Instdir,"/AppGetName")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        _archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/imagenes/",_archivoIMGname)
        self.iconbitmap(_archivoIMG)

        Frame = tk.Frame(self)
        Frame.grid()

        ###############################################
        #       construccion de las rejillas
        ###############################################
        # for r in range(6):
        #     self.master.rowconfigure(r, weight=1)    
        # for c in range(5):
        #     self.master.columnconfigure(c, weight=1)
        ###############################################
        #       construccion de las rejillas
        ###############################################
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)
        # Frame0 = Frame(master, bg="yellow")
        # Frame0.grid(row = 0, column = 0, rowspan = 1, columnspan = 6, sticky = W+E+N+S)

        # Frame1 = Frame(master, bg="red")
        # Frame1.grid(row = 1, column = 0, rowspan = 5, columnspan = 3, sticky = W+E+N+S)

        # Frame2 = Frame(master, bg="blue")
        # Frame2.grid(row = 5, column = 3, rowspan = 3, columnspan = 3, sticky = W+E+N+S)

        # Frame3 = Frame(master, bg="green")
        # Frame3.grid(row = 1, column = 3, rowspan = 4, columnspan = 3, sticky = W+E+N+S)

        ###############################################
        #       construccion de los datos
        ###############################################
        _archivoIMGname="calabaza_81x100.png"
        _archivoIMG="{}{}".format(_Instdir,"/AppGetName/imagenes")
        os.chdir(_archivoIMG)
        print("---->>>>>>>    La imagenesn es:      ",_archivoIMGname," en carpeta : ",_archivoIMG)
        #Label(Frame3,imagenes=_archivoIMGname).grid(row=3, column=1, sticky=W)
        # Label(Frame0, text="<---- Enter the required data for this file ----> ").grid(row=0, column=0, rowspan = 1, columnspan = 6, sticky=W+E+N+S)

        # Label(Frame1, text="Enter customer's Name: ").grid(row=1, column=1, sticky=W)
        # _PDFuserName=StringVar()
        # Entry(Frame1, textvariable = _PDFuserName).grid(row=1, column=200,  sticky=W)

        # Label(Frame1, text="Enter customer's Last Name: ").grid(row=2, column=1, rowspan = 1, columnspan = 6, sticky=W)
        # _PDFuserLast=StringVar()
        # Entry(Frame1, textvariable = _PDFuserLast).grid(row=2, column=200, sticky=W)

        # Label(Frame1, text="Enter customer's Last 4 SSN: ").grid(row=3, column=1, rowspan = 1, columnspan = 6, sticky=W)
        # _PDFuserNum=StringVar()
        # Entry(Frame1, textvariable = _PDFuserNum).grid(row=3, column=200, sticky=W)

        # Label(Frame1, text="Enter Document Type: ").grid(row=4, column=1, rowspan = 1, columnspan = 6, sticky=W)
        # _PDFfileType=StringVar()
        # Entry(Frame1, textvariable = _PDFfileType).grid(row=4, column=200, sticky=W)

        # Button(Frame2, text="ACCEPT",command=return_entry).grid(row=6,column=3,sticky=E+W)
        ###############################################
        #      FIN DE  construccion de los datos
        ###############################################
        self.PDFuserName = tk.StringVar()
        self.PDFuserLast = tk.StringVar()
        self.PDFuserNum = tk.StringVar()
        self._PDFfileType = tk.StringVar()

        tk.Label(Frame, text="Enter customer's Name: ").grid(row=1, column=1, sticky=tk.W)
        tk.Entry(Frame, textvariable=self.PDFuserName).grid(row=1, column=200, sticky=tk.W)
        tk.Label(Frame, text="Enter customer's Last Name: ").grid(row=2, column=1,
            rowspan=1, columnspan=6, sticky=tk.W)
        tk. Entry(Frame, textvariable=self.PDFuserLast).grid(row=2, column=200, sticky=tk.W)
        tk.Label(Frame, text="Enter customer's Last 4 SSN: ").grid(row=3, column=1,
            rowspan = 1, columnspan = 6, sticky=tk.W)        
        tk.Entry(Frame, textvariable = self.PDFuserNum).grid(row=3, column=200, sticky=tk.W)
        tk.Label(Frame, text="Enter Document Type: ").grid(row=4, column=1, rowspan=1,
            columnspan = 6, sticky=tk.W)       
        tk.Entry(Frame, textvariable = self._PDFfileType).grid(row=4, column=200, sticky=tk.W)
        tk.Button(Frame, text="ACCEPT", command=self.on_accept).grid(row=6,
            column=3,sticky=tk.E + tk.W)

        ##  CONSTRUCCION DEL OBJETOs-MENU QUE SERAN USDADOS PARA EJECUTAR LAS LLAMADAS DEL MENU ###
        def mabout(self):
            messagebox.showinfo(title="About",message="""Hecho por: Yoka Alejandra Alvarez\nVersion: 0.0.1\n\n\ncorreo: Yoka.alvarezr@outlook.com""")
            return

        ###     construccion del menu   ####
        menuBar=Menu(self)

        #construccion del menu help
        helpmenu=Menu(menuBar, tearoff=0)
        helpmenu.add_command(label="About",command=self.mabout)
        helpmenu.add_command(label="Help")


        menuBar.add_cascade(label="About",menu=helpmenu)

        ### ensamblado del menu en el main form
        self.config(menu=menuBar)
        # ACA SE HACE LA LLAMADA AL FONDO HABILITAR DE ALGUN MODO
        # fondo=fondoGUI(self.master)
        # self.mainloop()



    def on_accept(self):  
        # Puedes aprobechar esto para validar los datos antes de cerrar
        self.destroy()

    def get_data(self):
        # ACA SE HACE LA LLAMADA AL FONDO HABILITAR DE ALGUN MODO
        fondo=fondoGUI(self)
        self.mainloop()
        PDFuserName = self.PDFuserName.get()
        PDFuserLast = self.PDFuserLast.get()
        PDFuserNum = self.PDFuserNum.get()
        _PDFfileType = self._PDFfileType.get()
        return [PDFuserName, PDFuserLast, PDFuserNum, _PDFfileType]       


if __name__ == "__main__":
    inst = FunctionsClass()
    inst.CambiarNombrePDF(None, None)