# define todas las variables del sistema

#_dirPDF ES LA VARIABLE QUE VA A ALMACENAR EL DIRECTORIO EN DONDE VAN A ESTAR LOS ARCHIVOS PDF EN LA CUAL VA A TRABAJAR EL SCRIPT
#_dirDES ES LA VARIABLE QUE VA A ALMACENAR 
#_orgPC ES LA VARIABLE QUE VA A ALMACENAR
#_destPC ES LA VARIABLE QUE VA A ALMACENAR
#__convert2PDF ES LA VARIABLE QUE VA A ALMACENAR 

class VariablesSystemas():
	#TXT ES LA VARIABLE QUE ALMACENA EL NOMBRE DEL ARCHIVO DE TEXTO CON LA CONFIGURACION DE PARAMETROS
	TXT="data.conf"
	def __init__(self):
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

	#PARA VARIABLE= Destiny_Directory , define 
	def VarDirOBJ(self):
		v=self._lista2.index("Destiny_Directory")
		_dirDES=self._lista2[v+1]
		return _dirDES

	#PARA VARIABLE= Nombre_PC_origen , define el nombre de dominio del pc en el que se esta ejecutndo el script
	def VarOrigenPC(self):
		v=self._lista2.index("Nombre_PC_origen")
		_orgPC=self._lista2[v+1]
		return _orgPC

	#PARA VARIABLE= Nombre_PC_destino , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarDestinyPC(self):
		v=self._lista2.index("Nombre_PC_destino")
		_destPC=self._lista2[v+1]
		return _destPC

	#PARA VARIABLE= Convertir_a_PDF
	def VarConvertToPDF(self):
		v=self._lista2.index("Convertir_a_PDF")
		_TXTConvertToPDF=self._lista2[v+1]
		if _TXTConvertToPDF=="yes" or _TXTConvertToPDF=="Yes" or _TXTConvertToPDF=="YES" or _TXTConvertToPDF=="y" or _TXTConvertToPDF=="Y":
			_convert2PDF=True
		else:
			_convert2PDF=False
		return _convert2PDF

	#PARA VARIABLE= Imagen_magick_dir , define el nombre de dominio del pc al que se va a enviar el archivo
	def VarImgMagickDir(self):
		v=self._lista2.index("Imagen_magick_dir")
		_dirIMAGICK=self._lista2[v+1]
		return _dirIMAGICK