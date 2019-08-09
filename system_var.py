# define todas las variables del sistema
import os


#_dirPDF ES LA VARIABLE QUE VA A ALMACENAR EL DIRECTORIO EN DONDE VAN A ESTAR LOS ARCHIVOS PDF EN LA CUAL VA A TRABAJAR EL SCRIPT
#_dirDES ES LA VARIABLE QUE VA A ALMACENAR 
#_orgPC ES LA VARIABLE QUE VA A ALMACENAR
#_destPC ES LA VARIABLE QUE VA A ALMACENAR
#__convert2PDF ES LA VARIABLE QUE VA A ALMACENAR 

#print("directorio en system",os.getcwd())
# b=os.getcwd()
# l=[]
# l.extend((b.replace("\\"," ")).split())
# #print("la carpeta es: ",l[-1])
# if l[-1] == "AppGetName":
# 	os.chdir("..")
# else:
# 	#print("directorio en system",os.getcwd())
# 	pass
print("la variable __name__ en system_var es  : ",__name__)
print("la variable __file__ en system_vares es : ",__file__)
#print("la variable __path__ en system_vares es : ",__path__)		
class VariablesSystemas():
	#TXT ES LA VARIABLE QUE ALMACENA EL NOMBRE DEL ARCHIVO DE TEXTO CON LA CONFIGURACION DE PARAMETROS
	#os.chdir(r"C:\Users\Tor\Desktop\Sublime Text Build 3143 x64\PROGRAMAS\script_folder")

	def __init__(self):

		#if __name__ == "__main__":  #ojo puede ser que esto no funcione porque este rchivo nunca se ejecuta desde cero siempre es importado
			
			_renBySCRPT=""
			_dirPDF=""
			_Instdir=""
			_destFOLDER=""
			_TXTHostPCName=""
			_DestPCName=""
			_convert2PDF=""
			_UnidadEnRED=""
			_GETHostPCName=""
			_dirIMAGICK=""
			_RenameByGUI=""
			_LogFile=""
			_UseDate2Move=""

			TXT="data.conf"
			#print("en 3 ",os.getcwd())
			## separando cada linea en nombre de variable y contenido de variable
			print("estoy en system_var voy a leer .TXT y mi directorio es: ",os.getcwd())
			with open(TXT,"r") as _texto:
				self._lista=_texto.readlines()
			
			self._lista1=[]
			self._lista2=[]
			#recorre la lista[] original por linea creada y remmplaza los espacios vacios por el texto "#espacio#" que 
			#permitira hayar a futuro y volver a remplazar por espacio vacio y asi mantener accesibles los directorios
			# por ejemplo el directorio C:/Program Files/...  con esto sera accesible al final del proceso
			for i in self._lista:
				if i[0] != "#":
					if  i[0] != " ":
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
			self._renBySCRPT=True
		else:
			self._renBySCRPT=False
		return self._renBySCRPT

	#PARA VARIABLE= Whatch_Directory
	def VarDirPDF(self):
		print("entre en vardir")
		v=self._lista2.index("Whatch_Directory")
		self._dirPDF=self._lista2[v+1]
		return self._dirPDF

	#PARA VARIABLE= Directorio_de_instalacion
	def VarInstalationDir(self):
		v=self._lista2.index("Directorio_de_instalacion")
		self._Instdir=self._lista2[v+1]
		return self._Instdir

	#PARA VARIABLE= Nombre_PC_destino , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarDestinyFOLDER(self):
		v=self._lista2.index("Destiny_Directory")
		self._destFOLDER=self._lista2[v+1]
		return self._destFOLDER
	
	#PARA VARIABLE= PC_HOST_Name , permite introducir manualmente el nombre de dominio del pcen el que se ejecuta la accion
	def VarHostPC(self):
		v=self._lista2.index("PC_HOST_Name")
		self._TXTHostPCName=self._lista2[v+1]
		return self._TXTHostPCName
		
	#PARA VARIABLE= PC_Destiny_name , permite introducir manualmente el nombre de dominio del pc al que se va a enviar el archivo
	def VarDestinyPC(self):
		v=self._lista2.index("PC_Destiny_name")
		self._DestPCName=self._lista2[v+1]
		return self._DestPCName

	#PARA VARIABLE= Convertir_a_PDF
	def VarConvertToPDF(self):
		v=self._lista2.index("Convertir_a_PDF")
		_TXTConvertToPDF=self._lista2[v+1]
		if _TXTConvertToPDF=="yes" or _TXTConvertToPDF=="Yes" or _TXTConvertToPDF=="YES" or _TXTConvertToPDF=="y" or _TXTConvertToPDF=="Y":
			self._convert2PDF=True
		else:
			self._convert2PDF=False
		return self._convert2PDF
	
	#PARA VARIABLE= Usar_Unida_en_Red , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarUndEnRED(self):
		v=self._lista2.index("Usar_Unida_en_Red")
		_TXTGetDomain=self._lista2[v+1]
		if _TXTGetDomain=="yes" or _TXTGetDomain=="Yes" or _TXTGetDomain=="YES" or _TXTGetDomain=="y" or _TXTGetDomain=="Y":
			self._UnidadEnRED=True
		else:
			self._UnidadEnRED=False
		return self._UnidadEnRED
		
	#PARA VARIABLE= Get_Domain_Name , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarGetDomainName(self):
		v=self._lista2.index("Get_Domain_Name")
		_TXTGetDomain=self._lista2[v+1]
		if _TXTGetDomain=="yes" or _TXTGetDomain=="Yes" or _TXTGetDomain=="YES" or _TXTGetDomain=="y" or _TXTGetDomain=="Y":
			self._GETHostPCName=True
		else:
			self._GETHostPCName=False
		return self._GETHostPCName
	
	#PARA VARIABLE= Imagen_magick_dir , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarImgMagickDir(self):
		v=self._lista2.index("Imagen_magick_dir")
		self._dirIMAGICK=self._lista2[v+1]
		return self._dirIMAGICK

	#PARA VARIABLE= Rename_By_GUI , esta variable determina si se toma el nombre de dominio del sistema o se usa el nombre dado en este arcivo de configuracion
	def VarRenameByGUI(self):
		v=self._lista2.index("Rename_By_GUI")
		_TXTRenameByGUI=self._lista2[v+1]
		if _TXTRenameByGUI=="yes" or _TXTRenameByGUI=="Yes" or _TXTRenameByGUI=="YES" or _TXTRenameByGUI=="y" or _TXTRenameByGUI=="Y":
			self._RenameByGUI=True
		else:
			self._RenameByGUI=False
		return self._RenameByGUI

	#PARA VARIABLE= Usar_Log_File , esta variable determina si se habilita la escritura del archivo LOG
	def VarWriteLogFile(self):
		v=self._lista2.index("Usar_Log_File")
		_TXTLogFile=self._lista2[v+1]
		if _TXTLogFile=="yes" or _TXTLogFile=="Yes" or _TXTLogFile=="YES" or _TXTLogFile=="y" or _TXTLogFile=="Y":
			self._LogFile=True
		else:
			self._LogFile=False
		return self._LogFile

	#PARA VARIABLE= Use_Date_to_Move , esta variable determina si se habilita la escritura del archivo LOG
	def VarUseDate2Move(self):
		v=self._lista2.index("Use_Date_to_Move")
		_TXTUseDate2Move=self._lista2[v+1]
		if _TXTUseDate2Move=="yes" or _TXTUseDate2Move=="Yes" or _TXTUseDate2Move=="YES" or _TXTUseDate2Move=="y" or _TXTUseDate2Move=="Y":
			self._UseDate2Move=True
		else:
			self._UseDate2Move=False
		return self._UseDate2Move





	def Get(self,valor):

		if valor== "VarUseRenByScrypt":
			return self._renBySCRPT
		elif valor== "VarDirPDF":
			return self._dirPDF
		elif valor== "VarInstalationDir":
			return self._Instdir
		elif valor== "VarDestinyFOLDER":
			return self._destFOLDER
		elif valor== "VarHostPC":
			return self._TXTHostPCName
		elif valor== "VarDestinyPC":
			return self._DestPCName
		elif valor== "VarConvertToPDF":
			return self._convert2PDF
		elif valor== "VarUndEnRED":
			return self._UnidadEnRED
		elif valor== "VarGetDomainName":
			return self._GETHostPCName
		elif valor== "VarImgMagickDir":
			return self._dirIMAGICK
		elif valor== "VarRenameByGUI":
			return self._RenameByGUI
		elif valor== "VarWriteLogFile":
			return self._LogFile
		elif valor== "VarUseDate2Move":
			return self._UseDate2Move

t=VariablesSystemas()

t.VarUseRenByScrypt()
t.VarDirPDF()
t.VarInstalationDir()
t.VarDestinyFOLDER()
t.VarHostPC()
t.VarDestinyPC()
t.VarConvertToPDF()
t.VarUndEnRED()
t.VarGetDomainName()
t.VarImgMagickDir()
t.VarRenameByGUI()
t.VarWriteLogFile()
t.VarUseDate2Move()
