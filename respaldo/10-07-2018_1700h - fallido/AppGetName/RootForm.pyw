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

		def return_entry():
			Job.OutPrint("entre en el return del AppGUI")
			#PDFname=_pdfnombre.get()

			PDFuserName=_PDFuserName.get()
			PDFuserLast=_PDFuserLast.get()
			PDFuserNum=_PDFuserNum.get()
			PDFfileType=_PDFfileType.get()
			print("los valores son : ", PDFuserName, PDFuserLast, PDFuserNum, PDFfileType)
			Job.ModNames(PDFuserName,PDFuserLast,PDFuserNum,PDFfileType)   
			self.master.destroy()
		###############################################
		#       construccion de los datos
		###############################################
		for r in range(6):
		    self.master.rowconfigure(r, weight=1)    
		for c in range(5):
		    self.master.columnconfigure(c, weight=1)
		###############################################
		#       construccion de los datos
		###############################################
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
		_archivoIMGname="calabaza_81x100.png"
		_archivoIMG="{}{}".format(_Instdir,"/AppGetName/image")
		os.chdir(_archivoIMG)
		Job.OutPrint("---->>>>>>>    La imagen es:      ",_archivoIMGname," en carpeta : ",_archivoIMG)
		#Label(Frame3,image=_archivoIMGname).grid(row=3, column=1, sticky=W)
		Label(Frame0, text="<---- Enter the required data for this file ----> ").grid(row=0, column=0, rowspan = 1, columnspan = 6, sticky=W+E+N+S)

		Label(Frame1, text="Enter customer's Name: ").grid(row=1, column=1, sticky=W)
		_PDFuserName=StringVar()
		Entry(Frame1, textvariable = _PDFuserName).grid(row=1, column=200,  sticky=W)

		Label(Frame1, text="Enter customer's Last Name: ").grid(row=2, column=1, rowspan = 1, columnspan = 6, sticky=W)
		_PDFuserLast=StringVar()
		Entry(Frame1, textvariable = _PDFuserLast).grid(row=2, column=200, sticky=W)

		Label(Frame1, text="Enter customer's Last 4 SSN: ").grid(row=3, column=1, rowspan = 1, columnspan = 6, sticky=W)
		_PDFuserNum=StringVar()
		Entry(Frame1, textvariable = _PDFuserNum).grid(row=3, column=200, sticky=W)

		Label(Frame1, text="Enter Document Type: ").grid(row=4, column=1, rowspan = 1, columnspan = 6, sticky=W)
		_PDFfileType=StringVar()
		Entry(Frame1, textvariable = _PDFfileType).grid(row=4, column=200, sticky=W)

		Button(Frame2, text="ACCEPT",command=return_entry).grid(row=6,column=3,sticky=E+W)
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

		fondo=fondoGUI(self.master)
		self.master.mainloop()


root = Tk()
app = AppGUI(master=root)