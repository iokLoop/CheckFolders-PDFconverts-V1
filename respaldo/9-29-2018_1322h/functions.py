from GEimport import *

########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################
from objetos_dir import *
from system_var import *

sysVar=VariablesSystemas()
MngObj=ManejarObjFile()

class FunctionsClass():
	
	
	def ListarDirectorio(self,_dirPDF):
		ListName=[]
		for (dirpath, dirnames, filenames) in os.walk(_dirPDF):
		    ListName.extend(filenames)
		    break

		return ListName[:]

	def DirChangeDetect(self):
		MngObj.CLEARListaObjAF(None)
		MngObj.GETStateFolder(sysVar.VarDirPDF(),"AFTER")
		_LObjBE=MngObj.GETListaObjBE()
		_LObjAF=MngObj.GETListaObjAF()
### BORRAR DESDE ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO
		print("\n\naca el after luego de tomarlo nuevamente ",_LObjAF)
		AA=[]
		BB=[]
		for i in _LObjBE:
			AA.append(i["_nomFILE"])
		for ii in _LObjAF:
			BB.append(ii["_nomFILE"])
		print ("\n\nel archivo before es : \n",AA[:])
		print("\n\nel archivo after es : \n",BB[:])
		AA=None
		BB=None
### BORRAR HASTA ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO
		if _LObjAF == _LObjBE:
			print ("\n\nno hay cambios en la carpeta")
		else:
			print("\n*******  SE HA DETECTADO UN CAMBIO LA CARPETA... ACTUALIZANDO!!!    *********")
			print("\nLlamando a las acciones a realizar")
			MngObj.MODListaObjBE(_LObjAF)
### BORRAR DESDE ACA 2222   ESTO ES SOLO PAA COMPROVACION DE CODIGO
		_LObjBE=MngObj.GETListaObjBE()
		_LObjAF=MngObj.GETListaObjAF()
		print("\nARRIBA se comprovo el codigooooooooooooooooooooooooooooo")
		AA=[]
		BB=[]
		for i in _LObjBE:
			AA.append(i["_nomFILE"])
		for i in _LObjAF:
			BB.append(i["_nomFILE"])
		print ("\nel archivo before es : \n",AA[:])
		print("\nel archivo after es : \n",BB[:])
		AA=None
		BB=None
### BORRAR HASTA ACA 2222   ESTO ES SOLO PAA COMPROVACION DE CODIGO

	def ConvertToPDF(self,_dirPDF,_dirIMAGICK,_fileName,_fileName2,_fileName3,_fileName4):
		try:
			
			# with Image(filename=_fileName) as img:
			# 	if img.alpha_channel==True:
			# 		print ("el alfa es : ", img.alpha_channel)
			# 		img.alpha_channel=False
			# 	print ("el alfa es ahora : ", img.alpha_channel)

			#metodo ORIGINAL
			## opening from filename
			# with open("name.pdf","wb") as f:
			# 	f.write(img2pdf.convert('test.jpg'))
			
			#os.chdir(_dirPDF)
			print("\nel directorio en el que se va a ejecutar la conversion es : ",os.getcwd())
			print("\nEL ARCHIVO pdf ES: ",_fileName3)
			print("\nEL ARCHIVO jpg ES: ",_fileName)
			with open(_fileName3,"wb") as f:
				f.write(img2pdf.convert(_fileName))
			#specify paper size (medidas en x , y ; A4 = 210 x 297: letter = 216 x 279 )
			# a4inpt = (img2pdf.mm_to_pt(216),img2pdf.mm_to_pt(279))
			# layout_fun = img2pdf.get_layout_fun(a4inpt)
			
			# with open('imageSinAlpha.jpg',"wb") as f:
			# 	f.write(img2pdf.convert(_fileName2, layout_fun=layout_fun))


		except:
			try:
				print("\nSe ha identificado que la imagen contiene alpha channel")
				print("\nProcediendo a Eliminar El Alpha Channel de la imagen")
				#elimino el primer archivo de conversion FALLIDO
				#os.remove(_fileName3)
				#Usar el ImagenMagick para quitarle el alpha a la imagen
				#convert input.png -background white -alpha remove -alpha off output.png
				os.chdir(_dirIMAGICK)
				#print (os.getcwd())
				_SnALPH='{}{}{}'.format(_fileName2,"_SnALPH",_fileName4)
				_SnALPHpdf='{}{}{}'.format(_fileName2,"_SnALPH",".pdf")
				_comando='{}{}{}{}{}{}{}{}'.format( "convert ", _dirPDF,"/", _fileName," -background white -alpha remove -alpha off ", _dirPDF,"/",_SnALPH)
				print ("\"el comando a ejecutar es : ",_comando)
				os.popen( _comando)
				os.chdir(_dirPDF)
				
				print("\nel directorio en el que se va a ejecutar la conversion es : ",os.getcwd())
				print("\nEL ARCHIVO pdf ES: ",_SnALPHpdf)
				print("\nEL ARCHIVO jpg ES: ",_SnALPH)
				with open(_SnALPHpdf,"wb") as f:
					print("\n el nombre del archivo antes de convertir a pdf es : ",_SnALPHpdf)
					f.write(img2pdf.convert(_SnALPH))
			except:
				print("\nse produjo un segundo error al convertir a PDF, se enviara el archivo en jpg")
				#_errorCONV=True
		finally:
			print("\nestamos en el finally")
			# if _errorCONV==True:
			# 	print("entre en el TRUE")
			# 	os.remove(_SnALPHpdf)
			# 	print(_fileName)
			# 	#os.remove(_fileName)
			# 	_errorCONV=None
			# 	_count=0
			# 	_count+=1
			# else:
			# 	#borrando el segundo archivo antiguo
			# 	#os.remove(_fileName)
			# 	print("entre en el FALSE")
			
			self.MoverPDF()
			

	def CambiarNombrePDF(self,_dirPDF,_convert2PDF,_ImgMagickDir):
		ListName=self.ListarDirectorio(_dirPDF)
		os.chdir(_dirPDF)
		#os.getcwd()
		#definicion de las variables que formaran el nombre para cada archivo
		_PDFname=""
		_PDFuserName="Carlos"
		_PDFuserLast="Mata"
		_PDFuserNum="4459"
		_PDFfileType="Passport"
		

		for filename in os.listdir(_dirPDF):
			#os.rename(filename, filename[5:])     #esta forma recorte el nombre
#### BORRAR ESTE SEGMENTO >
			_PDFname=_PDFname + "1"
			_PDFuserName=_PDFuserName + "1"
			_PDFuserLast=_PDFuserLast + "1"
			_PDFuserNum=_PDFuserNum + "1"
			_PDFfileType=_PDFfileType + "1"
#### BORRAR ESTE SEGMENTO <
			#determinando la extencion del archivo
			file_name, file_extension = os.path.splitext(filename)	
			if _convert2PDF==True and file_extension != ".PDF" and file_extension != ".pdf"  :
				_convertToPDF=True
			else:
				_convertToPDF=False
			#_PDFname variable hace referencia al nuevo nombre CON la extencion del archivo original
			_PDFname='{}{}{}{}{}{}{}{}'.format( _PDFuserName,"_", _PDFuserLast,"_", _PDFuserNum,"_", _PDFfileType,file_extension)
			print(_PDFname)
			os.rename(filename, _PDFname)
			
			# YA CAMBIADO EL NOMBRE DEL ARCHIVO SE CONVIERTE A PDF DE SER NECESARIO
			if _convertToPDF == True:
				#_PDFname2 variable hace referencia al nuevo nombre SIN la extencion de archivo
				_PDFname2='{}{}{}{}{}{}{}'.format( _PDFuserName,"_", _PDFuserLast,"_", _PDFuserNum,"_", _PDFfileType)
				#_PDFname3 variable hace referencia al nuevo nombre CON la extencion de archivo en PDF
				_PDFname3='{}{}{}{}{}{}{}{}'.format( _PDFuserName,"_", _PDFuserLast,"_", _PDFuserNum,"_", _PDFfileType,".pdf")
				self.ConvertToPDF(_dirPDF,_ImgMagickDir,_PDFname,_PDFname2,_PDFname3,file_extension)
			else:
				pass

			#Limpiando variables para la siguiente ejecucion
			# _PDFname=None
			# _PDFuserName=None
			# _PDFuserLast=None
			# _PDFuserNum=None
			# _PDFfileType=None

		ListName=self.ListarDirectorio(_dirPDF)
		print(ListName[:])

	def MoverPDF(self):
		print("\nse ha ingresado a la funsion Mover archivos")

#sysVar=VariablesSystemas()
