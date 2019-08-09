from GEimport import *
import tkinter as tk
from tkinter import messagebox
from AppGetName.modulos.menu_function import *
########################
#   IMPORTANDO FUNCIONES PROPIAS
#########################
from objetos_dir import *
from system_var import *


sysVar=VariablesSystemas()
MngObj=ManejarObjFile()




class FunctionsClass():

    def __init__(self):
        print("entre en el funtion clas y se limpio las variables")
        self._PDFdatos = []

    def OutPrint(self,*salida):
        _salida=" ".join(salida)
        _LogFile=sysVar.VarWriteLogFile()
        _Instdir=sysVar.VarInstalationDir()
        os.chdir(_Instdir)
        _time=str(datetime.now())
        if _LogFile==True:
            ###  escribir datos en el archivo
            from io import open 
            with open("Checkdir.Log","a") as _texto:
                ###  escritura de la lista en el archivo texton una variable por linea
                    _texto.write(_time+": "+_salida+"\n")
            _texto.close()
        else:
            _salida2="{}{}{}".format(_time,": ",salida)
            print(_salida2)

    def DirChangeDetect(self):
        MngObj.CLEARListaObjAF()
        MngObj.GETStateFolder(sysVar.VarDirPDF(),"AFTER")
        #############################################################
        #               comienza el ingerto
        #############################################################
        _change=False
        _LObjBE=MngObj.GETListaObjBE()
        _LObjAF=MngObj.GETListaObjAF()

        if _LObjAF == _LObjBE:
            print ("\n\nno hay cambios en la carpeta")
        else:
            print("\n*******  SE HA DETECTADO UN CAMBIO LA CARPETA... ACTUALIZANDO!!!    *********")
            MngObj.MODListaObjBE(_LObjAF)
            print("\n<<<<<  ACTUALIZADO  >>>>>\n")
            _change=True
        return _change
        #############################################################
        #               termina el ingerto
        #############################################################

    def Limpieza(self):
        os.chdir(sysVar.VarDirPDF())
        self.DirChangeDetect()
        _LObjBE=MngObj.GETListaObjBE()
        for i in _LObjBE:
            if int(i["_weigthKB"]) == 0:
                _archivo='{}{}{}'.format(sysVar.VarDirPDF(),"/",i["_nomFILE"])
                print("el archivo a borrar es:\" ",_archivo , "\"")
                os.remove(_archivo)
                print("BORRANDO: ",_archivo)


        self.DirChangeDetect()
            
    def ConvertToPDF(self,_dirPDF,_dirIMAGICK):
        
        print("\n\nentre al convertir a pdf")
        os.chdir(_dirPDF)
        ListName=MngObj.GET_ListaAfter()
        _error=False
        IMG=[".jpg",".JPG",".jpeg",".JPEG",".PNG",".png",".BMP","bmp"]
        for filename in ListName:
            file_name, file_extension = os.path.splitext(filename)
            print("estoy en el for y el archivo es ",file_name,".",file_extension)
            for f in IMG:
                print ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
                if file_extension == f: 
                    print("\nel directorio en el que se va a ejecutar la conversion es : ",os.getcwd())
                    try:
                        print("entre en la primera convercion con el archivo :",file_name)
                        #metodo ORIGINAL
                        ## opening from filename
                        # with open("name.pdf","wb") as f:
                        #   f.write(img2pdf.convert('test.jpg'))
                        
                        _filePDFname="{}{}".format(file_name,".pdf")
                        with open(_filePDFname,"wb") as f:
                            f.write(img2pdf.convert(filename))
                        #specify paper size (medidas en x , y ; A4 = 210 x 297: letter = 216 x 279 )
                        # a4inpt = (img2pdf.mm_to_pt(216),img2pdf.mm_to_pt(279))
                        # layout_fun = img2pdf.get_layout_fun(a4inpt)
                        
                        # with open('imageSinAlpha.jpg',"wb") as f:
                        #   f.write(img2pdf.convert(_fileLastName, layout_fun=layout_fun))
                        #os.remove(filename)
                    except:
                        print("\nSe ha identificado que la imagen contiene alpha channel")
                        print("\nProcediendo a Eliminar El Alpha Channel de la imagen")
                        try:
                            #Usar el ImagenMagick para quitarle el alpha a la imagen
                            #convert input.png -background white -alpha remove -alpha off output.png
                            #[f  for f in before.keys() if not f in after.keys()]
                            #for f in IMG:
                                #print ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
                                #if file_extension == f:
                                    print("entre en la segunda convercion con el archivo: ",file_name)
                                    _SnALPH="{}{}{}".format(file_name,"_SnALPH",file_extension)
                                    os.chdir(_dirIMAGICK)
                                    _comando='{}{}{}{}{}{}{}{}'.format( "convert ", _dirPDF,"/", filename," -background white -alpha remove -alpha off ", _dirPDF,"/",_SnALPH)
                                    print ("\nel comando a ejecutar es : ",_comando)
                                    os.popen( _comando)
                                    os.chdir(_dirPDF)
                                    #os.remove(filename)
                                    _SnALPHpdf="{}{}{}".format(file_name,"_SnALPH",".pdf")
                                    print("\n el nombre del archivo antes de convertir a pdf es : ",_SnALPHpdf)
                                    with open(_SnALPHpdf,"wb") as f:
                                        f.write(img2pdf.convert(_SnALPH))
                                    #os.remove(_SnALPH)

                        except:
                            print("\nse produjo un segundo error al convertir a PDF, limpiando la carpeta y procediendo a convertir de nuevo")
                            _error=True
                            
                    finally:
                        print("\nestamos en el finally")
            else:
                pass
        self.Limpieza()
        return _error
            
    # def ModNames(self,PDFuserName,PDFuserLast,PDFuserNum,PDFfileType):
    #     #limpueza de variales
    #     self.OutPrint("los valores recibidos en ModNames son: ", PDFuserName, PDFuserLast, PDFuserNum, PDFfileType)
    #     self._PDFdatos.clear()
    #     self._PDFdatos=[PDFuserName, PDFuserLast, PDFuserNum, PDFfileType]
    #     print("estoy en el ModNames y som: ",self._PDFdatos)
    #     print("el id de memoria es ",id(self._PDFdatos))
    #     return self._PDFdatos

    # def GETdatos(self):
    #   print("en get datos el valor es: ",self._PDFdatos)
    #   print("el id de memoria es ",id(self._PDFdatos))
    #   return self._PDFdatos[:]

    # def GetName(self):

    #     print("estoy en el <<< GET NAME para llamar a AppGUI >>> \n\n\n")
    #     # _Instdir=sysVar.VarInstalationDir()
    #     # _dirPDF=sysVar.VarDirPDF()

    #     # ldir="{}{}".format(_Instdir,"/AppGetName")
    #     # print(ldir)
    #     # os.chdir(ldir)
    #     # print(os.getcwd())
    #     # comando="{}".format("\"python RootForm.pyw\"")
    #     # print("se ejecutara el comando : ", comando)
    #     # os.system(comando)
    #     root = Tk()
    #     app = AppGUI(master=root)
    #     os.chdir(_dirPDF)   


    # def cambiar_nombre_pdf(self, dir_pdf, convert_to_pdf):
    #     print("Lanzando formulario")
    #     formulario = AppGUI()
    #     self._PDFdatos = formulario.get_data()
    #     print("Formulario cerrado")
    #     print(self._PDFdatos)


    def CambiarNombrePDF(self,_dirPDF,_convert2PDF):
        #ListName=self.ListarDirectorio(_dirPDF)
        print("entre en cmbio de nombre")
        _convertToPDF=False     
        # _LObjBE=MngObj.GETListaObjBE()
        os.chdir(_dirPDF)
        ListName=MngObj.GET_ListaAfter()
        #print(ListName)
        
        #os.getcwd()
        #definicion de las variables que formaran el nombre para cada archivo
        _Instdir=sysVar.VarInstalationDir()
        #define si dentro del cambio de nombre por script se hace por gui o por shell
        _RenameByGUI=sysVar.VarRenameByGUI()
        
        n=0
        
        for filename in ListName:
            #os.rename(filename, filename[5:])     #esta forma recorte el nombre
            print(filename)
            
            if _RenameByGUI==True:
                print("entre en el if de gui")
                # ldir="{}{}".format(_Instdir,"/AppGetName")
                # print(ldir)
                # os.chdir(ldir)
                # print(os.getcwd())
                # comando="{}".format("\"python RootForm.pyw\"")
                # print(comando)
                # os.system(comando)
                # print("se ejecuto el comando ")
                # os.chdir(_dirPDF)
                # _PDFname=""
                # _PDFuserName=""
                # _PDFuserLast=""
                # _PDFuserNum=""
                # _PDFfileType=""
                # BORRAR_ESTO=""

                #self.GetName()
                #LLAMANDO A LA APPGUI PARA INGRESAR DATOS DE USUARIO
                formulario = AppGUI()
                self._PDFdatos = formulario.get_data()
                #self._PDFname
                _PDFdatos=self._PDFdatos
                print("<<<<  continuo la ejecuncion desde el punto despues de ir por los nombres >>>")
                #_PDFname=self._PDFdatos[0]
                print("la lista es: ",_PDFdatos)
                print("la cantidad de datos que tiene es: ",len(_PDFdatos))
                _PDFuserName=_PDFdatos[0]
                _PDFuserLast=_PDFdatos[1]
                _PDFuserNum=_PDFdatos[2]
                _PDFfileType=_PDFdatos[3]
                print("los valores que devuelve el GetName antes de formato son:", _PDFuserName," ", _PDFuserLast," ", _PDFuserNum," ", _PDFfileType)
                #_PDFname=self._PDFname.replace(" ","_")
                _PDFuserName=_PDFuserName.replace(" ","_")
                _PDFuserLast=_PDFuserLast.replace(" ","_")
                _PDFuserNum=_PDFuserNum.replace(" ","_")
                _PDFfileType=_PDFfileType.replace(" ","_")
                print("los valores que devuelve el GetName despues de formato son:", _PDFuserName," ", _PDFuserLast," ", _PDFuserNum," ", _PDFfileType)
                #time.sleep (500)
            else:
                #### BORRAR ESTE SEGMENTO >
                _PDFname=""
                _PDFuserName="Carlos"
                _PDFuserLast="Mata"
                _PDFuserNum="4459"
                _PDFfileType=""
                BORRAR_ESTO=["Passport","DNI","DECLARACION DE IMPUESTOS","VISA","CEDULA","PERMISO DE TRABAJO"]
                n+=1
                _PDFname=_PDFname.replace(" ","_")
                _PDFuserName=_PDFuserName.replace(" ","_")
                _PDFuserLast=_PDFuserLast.replace(" ","_")
                _PDFuserNum=_PDFuserNum.replace(" ","_")
                _PDFfileType=(BORRAR_ESTO[n]).replace(" ","_")
                #### BORRAR ESTE SEGMENTO <

            #determinando la extencion del archivo
            file_name, file_extension = os.path.splitext(filename)  
            #_PDFname variable hace referencia al nuevo nombre CON la extencion del archivo original
            _PDFname='{}{}{}{}{}{}{}{}'.format( _PDFuserName,"_", _PDFuserLast,"_", _PDFuserNum,"_", _PDFfileType, file_extension)
            os.chdir(_dirPDF)
            print("el directorio de cambio de nombre es: ",os.getcwd())
            print("los archivos son: ",os.listdir(os.getcwd()))
            os.rename(filename, _PDFname)
            if _convert2PDF==True and file_extension != ".PDF" and file_extension != ".pdf"  :
                _convertToPDF=True          
        MngObj.CLEARListaObjAF()    
        return _convertToPDF
        

    def MoverPDF(self):
        print("\nse ha ingresado a la funsion Mover archivos")
        #_GetDomain es true o false
        _GETHostPCName=sysVar.VarGetDomainName()
        _DestPCName=sysVar.VarDestinyPC()
        _TXTHostPCName=sysVar.VarHostPC()
        _destFOLDER=sysVar.VarDestinyFOLDER()
        #_UnidadEnRED es true o false
        _UnidadEnRED=sysVar.VarUndEnRED()
        self.DirChangeDetect()
        MngObj.ShowObjectsListaBefore()
        AA=MngObj.GET_ListaAfter()
        
        if _UnidadEnRED==True:
            if _GETHostPCName==True:
                _GETTXTHostPCName=socket.gethostname()
                _dir="{}{}{}".format(_destFOLDER,"/",_GETTXTHostPCName)
                print(_dir)
                for f in AA:
                    print("mover << ",f," >> a << ",_dir," >>")
                    shutil.move(f,_dir)
            else:
                _dir="{}{}{}".format(_destFOLDER,"/",_TXTHostPCName)
                for f in AA:
                    print("mover << ",f," >> a << ",_dir," >>")
                    shutil.move(f,_dir)
        else:
            print ("se debe de establecer un socket")
        MngObj.CLEARListaObjBE()


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


class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Archivo Detectado, Correccion de nombre")
        self.resizable(1,1)
        self.geometry("650x350+100+200")  #  FOMRA QUE ME GUSTA ...PARA DAR TAMANO Y POSICION  OJO  ES AL MAIN FORM NO AL Frame
        self.attributes("-topmost",True)
        
        Job.OutPrint("entre en el root")

        os.chdir("..")
        #sysVar=VariablesSystemas()
        _Instdir=sysVar.VarInstalationDir()
        _Ldir="{}{}".format(_Instdir,"/AppGetName")
        os.chdir(_Ldir)
        _archivoIMGname="calabaza.ico"
        _archivoIMG="{}{}{}".format(_Instdir,"/AppGetName/image/",_archivoIMGname)
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
        _archivoIMG="{}{}".format(_Instdir,"/AppGetName/image")
        os.chdir(_archivoIMG)
        Job.OutPrint("---->>>>>>>    La imagen es:      ",_archivoIMGname," en carpeta : ",_archivoIMG)
        #Label(Frame3,image=_archivoIMGname).grid(row=3, column=1, sticky=W)
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
        objetosMenu=function_menuBar()

        ###     construccion del menu   ####
        menuBar=Menu(self)

        #construccion del menu help
        helpmenu=Menu(menuBar, tearoff=0)
        helpmenu.add_command(label="About",command=objetosMenu.mabout)
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