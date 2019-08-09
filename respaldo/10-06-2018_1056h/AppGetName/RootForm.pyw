import os, sys
import tkinter as tk
from tkinter import messagebox
from modulos.menu_function import *
sys.path.append('..')
from system_var import *


root=Tk()
root.title("Archivo Detectado, Correccion de nombre")
root.config(bg="gray")
root.attributes('-alpha',0.6)
root.attributes('-fullscreen',True)

os.chdir("..")
sysVar=VariablesSystemas()
_Instdir=sysVar.VarInstalationDir()
_Ldir="{}{}".format(_Instdir,"/AppGetName")
os.chdir(_Ldir)
_archivoIMGname="calabaza.ico"
_archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/image/",_archivoIMGname)

root.iconbitmap(_archivoIMG)

def toplevel():
	top=Toplevel()	
	os.chdir("..")
	sysVar=VariablesSystemas()
	_Instdir=sysVar.VarInstalationDir()
	_Ldir="{}{}".format(_Instdir,"/AppGetName")
	os.chdir(_Ldir)

	top.title("Archivo Detectado, Correccion de nombre")
	_archivoIMGname="calabaza.ico"
	_archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/image/",_archivoIMGname)
	top.iconbitmap(_archivoIMG)
	top.resizable(1,1)
	top.geometry("650x350+100+200")  #  FOMRA QUE ME GUSTA ...PARA DAR TAMANO Y POSICION  OJO  ES AL MAIN FORM NO AL FRAME
	top.attributes("-topmost",True)
	##############################################################
	#				COMIENZA EL INGERTO
 	##############################################################
 	# mainForm.attributes('-alpha',0.6)
	# mainForm.attributes('-fullscreen',True)

	###	CONSTRUCCION DEL OBJETOs-MENU QUE SERAN USDADOS PARA EJECUTAR LAS LLAMADAS DEL MENU ###
	objetosMenu=function_menuBar()

	def mainFrame2_visible():
		mainFrame.pack_forget()
		mainFrame1.pack_forget()
		mainFrame2.pack(side="top", fill="both", expand=True)
	  	
	def mainFrame1_visible():
		mainFrame.pack_forget()
		mainFrame2.pack_forget()
		mainFrame1.pack(side="top", fill="both", expand=True)


	### 	construccion del menu   ####
	menuBar=Menu(top)
	#806533537 telefono de vidente espanola
	#construccion del menu base de datos

	#construccion del menu help
	helpmenu=Menu(menuBar, tearoff=0)
	helpmenu.add_command(label="About",command=objetosMenu.mabout)
	helpmenu.add_command(label="Help")


	menuBar.add_cascade(label="Help",menu=helpmenu)

	### ensamblado del menu en el main form
	top.config(menu=menuBar)

	###		construccion de los main frame 		####

	mainFrame=Frame(top,
	                 borderwidth=2,
	                 relief=GROOVE,
	                 width="650",
	                 height="350"
	                )
	mainFrame.pack(side="top", fill="both", expand=True)

	mainFrame1=Frame(top,
	                 borderwidth=2,
	                 relief=GROOVE,
	                 bg="blue",
	                 width="650",
	                 height="350"
	                )
	# mainFrame1.attributes('-alpha',1)
	mainFrame1.pack(padx=2, pady=2, side="top", fill="both", expand=True)
	mainFrame1.pack_forget()

	mainFrame2=Frame(top,
	                 borderwidth=2,
	                 relief=GROOVE,
	                 bg="red",
	                 width="650",
	                 height="350"
	                )
	# mainFrame2.attributes('-alpha',1)
	mainFrame2.pack(padx=2, pady=2,side="top", fill="both", expand=True)
	mainFrame2.pack_forget()

	####     construccion del frame de bienvenida    #####
	Label(mainFrame,text="Programa de prueba para archivo de base de datos", fg="black", font=("Comic Sans MS",14)).place(x=50,y=25)

	_archivoIMGname="calabaza_81x100.png"
	_archivoIMG="{}{}{}{}{}".format("\"",_Instdir,"/AppGetName/image/",_archivoIMGname,"\"")
	print(_archivoIMG)
	#os.chdir(_archivoIMG)

	# miLogo=PhotoImage(file=_archivoIMG)
	# Label(mainFrame,image=miLogo).place(x=100,y=150)
	##############################################################
	#				COMIENZA EL INGERTO
	##############################################################
#root = Tk()

toplevel()
root.mainloop()
