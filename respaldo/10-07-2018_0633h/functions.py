from GEimport import *
import datetime
########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################
from objetos_dir import *
from system_var import *


sysVar=VariablesSystemas()
MngObj=ManejarObjFile()

class FunctionsClass():
	
	
	# def ListarDirectorio(self,_dirPDF):
	# 	ListName=[]
	# 	# for (dirpath, dirnames, filenames) in os.walk(_dirPDF):
	# 	#     ListName.extend(filenames)
	# 	#     break

	# 	return ListName[:]

	def DirChangeDetect(self):
		MngObj.CLEARListaObjAF()
		MngObj.GETStateFolder(sysVar.VarDirPDF(),"AFTER")
		#############################################################
		#				comienza el ingerto
		#############################################################
		_change=False
		_LObjBE=MngObj.GETListaObjBE()
		_LObjAF=MngObj.GETListaObjAF()

		if _LObjAF == _LObjBE:
			OutPrint ("\n\nno hay cambios en la carpeta")
		else:
			OutPrint("\n*******  SE HA DETECTADO UN CAMBIO LA CARPETA... ACTUALIZANDO!!!    *********")
			MngObj.MODListaObjBE(_LObjAF)
			OutPrint("\n<<<<<  ACTUALIZADO  >>>>>\n")
			_change=True
		return _change
		#############################################################
		#				termina el ingerto
		#############################################################

	def Limpieza(self):
		os.chdir(sysVar.VarDirPDF())
		self.DirChangeDetect()
		_LObjBE=MngObj.GETListaObjBE()
		for i in _LObjBE:
			if int(i["_weigthKB"]) == 0:
				_archivo='{}{}{}'.format(sysVar.VarDirPDF(),"/",i["_nomFILE"])
				OutPrint("el archivo a borrar es:\" ",_archivo , "\"")
				os.remove(_archivo)
				OutPrint("BORRANDO: ",_archivo)


		self.DirChangeDetect()
			
	def ConvertToPDF(self,_dirPDF,_dirIMAGICK):
		
		OutPrint("\n\nentre al convertir a pdf")
		os.chdir(_dirPDF)
		ListName=MngObj.GET_ListaAfter()
		_error=False
		IMG=[".jpg",".JPG",".jpeg",".JPEG",".PNG",".png",".BMP","bmp"]
		for filename in ListName:
			file_name, file_extension = os.path.splitext(filename)
			OutPrint("estoy en el for y el archivo es ",file_name,".",file_extension)
			for f in IMG:
				OutPrint ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
				if file_extension == f: 
					OutPrint("\nel directorio en el que se va a ejecutar la conversion es : ",os.getcwd())
					try:
						OutPrint("entre en la primera convercion con el archivo :",file_name)
						#metodo ORIGINAL
						## opening from filename
						# with open("name.pdf","wb") as f:
						# 	f.write(img2pdf.convert('test.jpg'))
						
						_filePDFname="{}{}".format(file_name,".pdf")
						with open(_filePDFname,"wb") as f:
							f.write(img2pdf.convert(filename))
						#specify paper size (medidas en x , y ; A4 = 210 x 297: letter = 216 x 279 )
						# a4inpt = (img2pdf.mm_to_pt(216),img2pdf.mm_to_pt(279))
						# layout_fun = img2pdf.get_layout_fun(a4inpt)
						
						# with open('imageSinAlpha.jpg',"wb") as f:
						# 	f.write(img2pdf.convert(_fileLastName, layout_fun=layout_fun))
						#os.remove(filename)
					except:
						OutPrint("\nSe ha identificado que la imagen contiene alpha channel")
						OutPrint("\nProcediendo a Eliminar El Alpha Channel de la imagen")
						try:
							#Usar el ImagenMagick para quitarle el alpha a la imagen
							#convert input.png -background white -alpha remove -alpha off output.png
							#[f	 for f in before.keys() if not f in after.keys()]
							#for f in IMG:
								#OutPrint ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
								#if file_extension == f:
									OutPrint("entre en la segunda convercion con el archivo: ",file_name)
									_SnALPH="{}{}{}".format(file_name,"_SnALPH",file_extension)
									os.chdir(_dirIMAGICK)
									_comando='{}{}{}{}{}{}{}{}'.format( "convert ", _dirPDF,"/", filename," -background white -alpha remove -alpha off ", _dirPDF,"/",_SnALPH)
									OutPrint ("\nel comando a ejecutar es : ",_comando)
									os.popen( _comando)
									os.chdir(_dirPDF)
									#os.remove(filename)
									_SnALPHpdf="{}{}{}".format(file_name,"_SnALPH",".pdf")
									OutPrint("\n el nombre del archivo antes de convertir a pdf es : ",_SnALPHpdf)
									with open(_SnALPHpdf,"wb") as f:
										f.write(img2pdf.convert(_SnALPH))
									#os.remove(_SnALPH)

						except:
							OutPrint("\nse produjo un segundo error al convertir a PDF, limpiando la carpeta y procediendo a convertir de nuevo")
							_error=True
							
					finally:
						OutPrint("\nestamos en el finally")
			else:
				pass
		self.Limpieza()
		return _error
			

	def CambiarNombrePDF(self,_dirPDF,_convert2PDF):
		#ListName=self.ListarDirectorio(_dirPDF)
		OutPrint("entre en cmbio de nombre")
		_convertToPDF=False		
		# _LObjBE=MngObj.GETListaObjBE()
		os.chdir(_dirPDF)
		ListName=MngObj.GET_ListaAfter()
		#OutPrint(ListName)
		
		#os.getcwd()
		#definicion de las variables que formaran el nombre para cada archivo
		_Instdir=sysVar.VarInstalationDir()
		#define si dentro del cambio de nombre por script se hace por gui o por shell
		_RenameByGUI=sysVar.VarRenameByGUI()
		
		n=0
		
		for filename in ListName:
			#os.rename(filename, filename[5:])     #esta forma recorte el nombre
			OutPrint(filename)
			
			if _RenameByGUI==True:
				OutPrint("entre en el if de gui")
				ldir="{}{}".format(_Instdir,"/AppGetName")
				OutPrint(ldir)
				os.chdir(ldir)
				OutPrint(os.getcwd())
				comando="{}".format("\"python RootForm.pyw\"")
				OutPrint(comando)
				os.system(comando)
				OutPrint("se ejecuto el comando ")
				os.chdir(_dirPDF)
				_PDFname=""
				_PDFuserName=""
				_PDFuserLast=""
				_PDFuserNum=""
				_PDFfileType=""
				BORRAR_ESTO=""
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
			os.rename(filename, _PDFname)
			if _convert2PDF==True and file_extension != ".PDF" and file_extension != ".pdf"  :
				_convertToPDF=True			
		MngObj.CLEARListaObjAF()	
		return _convertToPDF
		

	def MoverPDF(self):
		OutPrint("\nse ha ingresado a la funsion Mover archivos")
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
				OutPrint(_dir)
				for f in AA:
					OutPrint("mover << ",f," >> a << ",_dir," >>")
					shutil.move(f,_dir)
			else:
				_dir="{}{}{}".format(_destFOLDER,"/",_TXTHostPCName)
				for f in AA:
					OutPrint("mover << ",f," >> a << ",_dir," >>")
					shutil.move(f,_dir)
		else:
			OutPrint ("se debe de establecer un socket")
		MngObj.CLEARListaObjBE()

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
			OutPrint(_salida)