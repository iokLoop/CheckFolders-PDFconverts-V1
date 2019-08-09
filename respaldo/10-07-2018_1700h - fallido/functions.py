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
	
	_PDFname=""
	_PDFuserName=""
	_PDFuserLast=""
	_PDFuserNum=""
	_PDFfileType=""
	# def ListarDirectorio(self,_dirPDF):
	# 	ListName=[]
	# 	# for (dirpath, dirnames, filenames) in os.walk(_dirPDF):
	# 	#     ListName.extend(filenames)
	# 	#     break

	# 	return ListName[:]
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
		#				comienza el ingerto
		#############################################################
		_change=False
		_LObjBE=MngObj.GETListaObjBE()
		_LObjAF=MngObj.GETListaObjAF()

		if _LObjAF == _LObjBE:
			self.OutPrint ("\n\nno hay cambios en la carpeta")
		else:
			self.OutPrint("\n*******  SE HA DETECTADO UN CAMBIO LA CARPETA... ACTUALIZANDO!!!    *********")
			MngObj.MODListaObjBE(_LObjAF)
			self.OutPrint("\n<<<<<  ACTUALIZADO  >>>>>\n")
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
				self.OutPrint("el archivo a borrar es:\" ",_archivo , "\"")
				os.remove(_archivo)
				self.OutPrint("BORRANDO: ",_archivo)


		self.DirChangeDetect()
			
	def ConvertToPDF(self,_dirPDF,_dirIMAGICK):
		
		self.OutPrint("\n\nentre al convertir a pdf")
		os.chdir(_dirPDF)
		ListName=MngObj.GET_ListaAfter()
		_error=False
		IMG=[".jpg",".JPG",".jpeg",".JPEG",".PNG",".png",".BMP","bmp"]
		for filename in ListName:
			file_name, file_extension = os.path.splitext(filename)
			self.OutPrint("estoy en el for y el archivo es ",file_name,".",file_extension)
			for f in IMG:
				self.OutPrint ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
				if file_extension == f: 
					self.OutPrint("\nel directorio en el que se va a ejecutar la conversion es : ",os.getcwd())
					try:
						self.OutPrint("entre en la primera convercion con el archivo :",file_name)
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
						self.OutPrint("\nSe ha identificado que la imagen contiene alpha channel")
						self.OutPrint("\nProcediendo a Eliminar El Alpha Channel de la imagen")
						try:
							#Usar el ImagenMagick para quitarle el alpha a la imagen
							#convert input.png -background white -alpha remove -alpha off output.png
							#[f	 for f in before.keys() if not f in after.keys()]
							#for f in IMG:
								#OutPrint ("comparacion entre <<< ",f," >>> y <<< ",file_extension," >>>")
								#if file_extension == f:
									self.OutPrint("entre en la segunda convercion con el archivo: ",file_name)
									_SnALPH="{}{}{}".format(file_name,"_SnALPH",file_extension)
									os.chdir(_dirIMAGICK)
									_comando='{}{}{}{}{}{}{}{}'.format( "convert ", _dirPDF,"/", filename," -background white -alpha remove -alpha off ", _dirPDF,"/",_SnALPH)
									self.OutPrint ("\nel comando a ejecutar es : ",_comando)
									os.popen( _comando)
									os.chdir(_dirPDF)
									#os.remove(filename)
									_SnALPHpdf="{}{}{}".format(file_name,"_SnALPH",".pdf")
									self.OutPrint("\n el nombre del archivo antes de convertir a pdf es : ",_SnALPHpdf)
									with open(_SnALPHpdf,"wb") as f:
										f.write(img2pdf.convert(_SnALPH))
									#os.remove(_SnALPH)

						except:
							self.OutPrint("\nse produjo un segundo error al convertir a PDF, limpiando la carpeta y procediendo a convertir de nuevo")
							_error=True
							
					finally:
						self.OutPrint("\nestamos en el finally")
			else:
				pass
		self.Limpieza()
		return _error
	

	def ModNames(self,PDFuserName,PDFuserLast,PDFuserNum,PDFfileType):
		#limpueza de variales
		self._PDFname=""
		self._PDFuserName=""
		self._PDFuserLast=""
		self._PDFuserNum=""
		self._PDFfileType=""
		#asignacion de variables
		self._PDFuserName=PDFuserName
		self._PDFuserLast=PDFuserLast
		self._PDFuserNum=PDFuserNum
		self._PDFfileType=PDFfileType
		# lst=[PDFname,PDFuserName,PDFuserLast,PDFuserNum,PDFfileType]
		# return lst[:]
		print("estoy en el ModNames y som: ",self._PDFuserName, self._PDFuserLast, self._PDFuserNum, self._PDFfileType)

	def GetName(self):

		self.OutPrint("estoy en el <<< GET NAME >>> \n\n\n")
		_Instdir=sysVar.VarInstalationDir()
		_dirPDF=sysVar.VarDirPDF()

		ldir="{}{}".format(_Instdir,"/AppGetName")
		self.OutPrint("el directorio objetivo es: ",ldir)
		os.chdir(ldir)
		self.OutPrint("el directorio en el que se va ejecutar el comando es: ",os.getcwd())
		comando="{}".format("\"python RootForm.pyw\"")
		self.OutPrint("el comando a ejecutaar es: ",comando)
		os.system(comando)
		self.OutPrint("se ejecuto el comando ")
		os.chdir(_dirPDF)		
		

	def CambiarNombrePDF(self,_dirPDF,_convert2PDF):
		#ListName=self.ListarDirectorio(_dirPDF)
		self.OutPrint("entre en cmbio de nombre")
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
			self.OutPrint(filename)
			
			if _RenameByGUI==True:
				self.OutPrint("entre en el if de gui")

				self.GetName()
				#self._PDFname
				self._PDFuserName
				self._PDFuserLast
				self._PDFuserNum
				self._PDFfileType
				_PDFname=self._PDFname.replace(" ","_")
				_PDFuserName=self._PDFuserName.replace(" ","_")
				_PDFuserLast=self._PDFuserLast.replace(" ","_")
				_PDFuserNum=self._PDFuserNum.replace(" ","_")
				_PDFfileType=self._PDFfileType.replace(" ","_")
			else:
				#### BORRAR ESTE SEGMENTO >
				_PDFname=""
				_PDFuserName="Carlos"
				_PDFuserLast="Mata"
				_PDFuserNum="4459"
				_PDFfileType=""
				
				n+=1
				#_PDFname=_PDFname.replace(" ","_")
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
		self.OutPrint("\nse ha ingresado a la funsion Mover archivos")
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
				self.OutPrint(_dir)
				for f in AA:
					self.OutPrint("mover << ",f," >> a << ",_dir," >>")
					shutil.move(f,_dir)
			else:
				_dir="{}{}{}".format(_destFOLDER,"/",_TXTHostPCName)
				for f in AA:
					self.OutPrint("mover << ",f," >> a << ",_dir," >>")
					shutil.move(f,_dir)
		else:
			self.OutPrint ("se debe de establecer un socket")
		MngObj.CLEARListaObjBE()

	