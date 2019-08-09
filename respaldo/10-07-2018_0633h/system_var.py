# define todas las variables del sistema
import os
#_dirPDF ES LA VARIABLE QUE VA A ALMACENAR EL DIRECTORIO EN DONDE VAN A ESTAR LOS ARCHIVOS PDF EN LA CUAL VA A TRABAJAR EL SCRIPT
#_dirDES ES LA VARIABLE QUE VA A ALMACENAR 
#_orgPC ES LA VARIABLE QUE VA A ALMACENAR
#_destPC ES LA VARIABLE QUE VA A ALMACENAR
#__convert2PDF ES LA VARIABLE QUE VA A ALMACENAR 

#print("directorio en system",os.getcwd())
b=os.getcwd()
l=[]
l.extend((b.replace("\\"," ")).split())
#print("la carpeta es: ",l[-1])
if l[-1] == "AppGetName":
	os.chdir("..")
else:
	#print("directorio en system",os.getcwd())
	pass
	
class VariablesSystemas():
	#TXT ES LA VARIABLE QUE ALMACENA EL NOMBRE DEL ARCHIVO DE TEXTO CON LA CONFIGURACION DE PARAMETROS
	#os.chdir(r"C:\Users\Tor\Desktop\Sublime Text Build 3143 x64\PROGRAMAS\script_folder")
	TXT="data.conf"
	def __init__(self):
		print("en 3 ",os.getcwd())
		## separando cada linea en nombre de variable y contenido de variable
		with open(self.TXT,"r") as _texto:
			self._lista=_texto.readlines()
		
		self._lista1=[]
		self._lista2=[]
		#recorre la lista[] original por linea creada y remmplaza los espacios vacios por el texto "#espacio#" que 
		#permitira hayar a futuro y volver a remplazar por espacio vacio y asi mantener accesibles los directorios
		# por ejemplo el directorio C:/Program Files/...  con esto sera accesible al final del proceso
		for i in self._lista:
			b=i.replace(" ","#espacio#")
			self._lista1.extend((b.replace("="," ")).split())

		#recorre la lista1[] ya dividida en variable y respuesta y remmplaza de vuelta los el texto "#espacio#" por espacio vacio
		for c in self._lista1:
			self._lista2.append((c.replace("#espacio#"," ")))


	###########    cargador de variables
	
	#PARA VARIABLE= Usar_rename_por_script
	def VarUseRenByScrypt(self):
		v=self._lista2.index("Usar_rename_por_script")
		_TXTrenBySCRPT=self._lista2[v+1]
		if _TXTrenBySCRPT=="yes" or _TXTrenBySCRPT=="Yes" or _TXTrenBySCRPT=="YES" or _TXTrenBySCRPT=="y" or _TXTrenBySCRPT=="Y":
			_renBySCRPT=True
		else:
			_renBySCRPT=False
		return _renBySCRPT

	#PARA VARIABLE= Whatch_Directory
	def VarDirPDF(self):
		v=self._lista2.index("Whatch_Directory")
		_dirPDF=self._lista2[v+1]
		return _dirPDF

	#PARA VARIABLE= Directorio_de_instalacion
	def VarInstalationDir(self):
		v=self._lista2.index("Directorio_de_instalacion")
		_Instdir=self._lista2[v+1]
		return _Instdir

	#PARA VARIABLE= Nombre_PC_destino , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarDestinyFOLDER(self):
		v=self._lista2.index("Destiny_Directory")
		_destFOLDER=self._lista2[v+1]
		return _destFOLDER
	
	#PARA VARIABLE= PC_HOST_Name , permite introducir manualmente el nombre de dominio del pcen el que se ejecuta la accion
	def VarHostPC(self):
		v=self._lista2.index("PC_HOST_Name")
		_TXTHostPCName=self._lista2[v+1]
		return _TXTHostPCName
		
	#PARA VARIABLE= PC_Destiny_name , permite introducir manualmente el nombre de dominio del pc al que se va a enviar el archivo
	def VarDestinyPC(self):
		v=self._lista2.index("PC_Destiny_name")
		_DestPCName=self._lista2[v+1]
		return _DestPCName

	#PARA VARIABLE= Convertir_a_PDF
	def VarConvertToPDF(self):
		v=self._lista2.index("Convertir_a_PDF")
		_TXTConvertToPDF=self._lista2[v+1]
		if _TXTConvertToPDF=="yes" or _TXTConvertToPDF=="Yes" or _TXTConvertToPDF=="YES" or _TXTConvertToPDF=="y" or _TXTConvertToPDF=="Y":
			_convert2PDF=True
		else:
			_convert2PDF=False
		return _convert2PDF
	
	#PARA VARIABLE= Usar_Unida_en_Red , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarUndEnRED(self):
		v=self._lista2.index("Usar_Unida_en_Red")
		_TXTGetDomain=self._lista2[v+1]
		if _TXTGetDomain=="yes" or _TXTGetDomain=="Yes" or _TXTGetDomain=="YES" or _TXTGetDomain=="y" or _TXTGetDomain=="Y":
			_UnidadEnRED=True
		else:
			_UnidadEnRED=False
		return _UnidadEnRED
		
	#PARA VARIABLE= Get_Domain_Name , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarGetDomainName(self):
		v=self._lista2.index("Get_Domain_Name")
		_TXTGetDomain=self._lista2[v+1]
		if _TXTGetDomain=="yes" or _TXTGetDomain=="Yes" or _TXTGetDomain=="YES" or _TXTGetDomain=="y" or _TXTGetDomain=="Y":
			_GETHostPCName=True
		else:
			_GETHostPCName=False
		return _GETHostPCName
	
	#PARA VARIABLE= Imagen_magick_dir , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarImgMagickDir(self):
		v=self._lista2.index("Imagen_magick_dir")
		_dirIMAGICK=self._lista2[v+1]
		return _dirIMAGICK

	#PARA VARIABLE= Rename_By_GUI , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarRenameByGUI(self):
		v=self._lista2.index("Rename_By_GUI")
		_TXTRenameByGUI=self._lista2[v+1]
		if _TXTRenameByGUI=="yes" or _TXTRenameByGUI=="Yes" or _TXTRenameByGUI=="YES" or _TXTRenameByGUI=="y" or _TXTRenameByGUI=="Y":
			_RenameByGUI=True
		else:
			_RenameByGUI=False
		return _RenameByGUI

	#PARA VARIABLE= Usar_Log_File , esta variable determina si se habilita la escritura del archivo LOG
	def VarWriteLogFile(self):
		v=self._lista2.index("Usar_Log_File")
		_TXTLogFile=self._lista2[v+1]
		if _TXTLogFile=="yes" or _TXTLogFile=="Yes" or _TXTLogFile=="YES" or _TXTLogFile=="y" or _TXTLogFile=="Y":
			_LogFile=True
		else:
			_LogFile=False
		return _LogFile