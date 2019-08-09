from GEimport import *
from system_var import *
#from system_var import OutPrint
# ESTA CLASE CREA EL OBJETO DEL TIPO DIRECTORIO DONDE SE ALMACENA CADA ARCHIVO Y CIERTA INFORMACION ADICIONAL
sysVar=VariablesSystemas()
class Outprint():
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
				print(_time,": ",_salida)

rework=Outprint()
class ObjFile():

	def __init__(self, nombre_archivo, ultima_modificacion, ultima_acceso, tamano_Kb, ubucacion_archivo, _TYPE):
		
		MngObj=ManejarObjFile()

		self.dicc={"_nomFILE":nombre_archivo,"_lastMOD":ultima_modificacion,"_lastACS":ultima_acceso,"_weigthKB":tamano_Kb,"_dirPDF":ubucacion_archivo}
		#rework.OutPrint("\n\nse tomo nuevo status con llamada desde un \"\"", _TYPE,"\"\"", self.dicc)
		#rework.OutPrint (self.dicc)
		if _TYPE=="BEFORE":
			MngObj.addListaObjFileBEFORE(self.dicc)
		else:
			MngObj.addListaObjFileAFTER(self.dicc)
	

class ManejarObjFile():
	# _LObjBE  = es la lista que almacena los objetos del tipo datos de arhivos BEFORE
	_LObjBE=[]
	_LObjAF=[]

	def GETListaObjBE(self):
		return self._LObjBE

	def GETListaObjAF(self):
		return self._LObjAF[:]

	def GET_ListaAfter(self):
		AA=[]
		for i in self._LObjAF:
			AA.append(i["_nomFILE"])
		return AA[:]
		AA=None

	def GET_ListaBefore(self):
		AA=[]
		#rework.OutPrint("en lista before")
		#rework.OutPrint(self._LObjBE)
		for i in self._LObjBE:
			AA.append(i["_nomFILE"])
		return AA[:]
		AA=None

	def MODListaObjBE(self,valor):
		self._LObjBE=valor

	def CLEARListaObjAF(self):
		#txt=" ".join(self._LObjAF)
		print(" Print antes del clear: ",self._LObjAF )
		self._LObjAF.clear()
		#txt=" ".join(self._LObjAF)
		print(" Print despues en el clear: ",self._LObjAF )

	def CLEARListaObjBE(self):
		#rework.OutPrint(" Print antes del clear: ",self._LObjBE )
		self._LObjBE.clear()
		#rework.OutPrint(" Print despues en el clear: ",self._LObjBE )

	def addListaObjFileBEFORE(self,_OBJ):
		#rework.OutPrint ("\n\nENTRANDO en el addlist del BEFORE y la lista BEFORE es :",self._LObjBE[:])
		self._LObjBE.append(_OBJ)
		#return self._LObjBE[:]

	def COMPROBAR(self, _object,_nombre):
		### BORRAR DESDE ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO
		AA=[]
		for i in _object:
			AA.append(i["_nomFILE"])
		txt=""
		txt=" ".join(AA[:])
		rework.OutPrint ("\nEl archivo << ",_nombre," >> tiene \" ",str(len(AA))," \" y son: \n",txt)
		AA=None
		### BORRAR HASTA ACA 1111   ESTO ES SOLO PAA COMPROVACION DE CODIGO


	def addListaObjFileAFTER(self,_OBJ):
		#rework.OutPrint ("\n\nENTRANDO en el addlist del after y la lista after es :",self._LObjAF[:])
		self.COMPROBAR(self._LObjAF[:],"Lista _LObjAF")
		
		#rework.OutPrint("\n\nel objeto a agregar en la lista es: ",_OBJ)
		
		self._LObjAF.append(_OBJ)
		
		self.COMPROBAR(self._LObjAF[:],"LUEGO DE APPEND _LObjAF")

		#rework.OutPrint ("\n\nSALIENDO DEL addlist del after y la lista after es :",self._LObjAF[:])
		#return self._LObjAF[:]
		
	def ShowObjectsListaBefore(self):
		total = 0
		linea = '-' * 40
        # Se acumulan tamaños y se muestra info de cada archivo
		for a in self._LObjBE:
			tamano=0
			rework.OutPrint(linea)
			rework.OutPrint('archivo      :', a["_nomFILE"])
			rework.OutPrint('modificado   :', a["_lastMOD"])       
			rework.OutPrint('ultimo acceso:', a["_lastACS"])
			tamano=round(int(a["_weigthKB"])/1024, 1)
			rework.OutPrint('tamano (Kb)  :', tamano)
			rework.OutPrint("Ubicacion del archivo: ",a["_dirPDF"],"\n")
			total= total+tamano

		rework.OutPrint(linea)
		rework.OutPrint(linea)
		rework.OutPrint('Num. archivos:', len(self._LObjBE))
		rework.OutPrint('Total (kb)   :', total)

	def GETStateFolder(self,_dirPDF,TYPE):
		#rework.OutPrint(_dirPDF)
		_TYPE=TYPE
		rework.OutPrint("\n\nEntre en el GETStatus desde un : \"\"", _TYPE,"\"\"")
		contenido = os.listdir(_dirPDF)  # obtiene lista con archivos/dir 
		total = 0
		archivos = 0
		formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
		linea = '-' * 40

		for elemento in contenido:
		    archivo = '{}{}{}'.format(_dirPDF,"/", elemento)
		    #rework.OutPrint(archivo)
		    #rework.OutPrint(os.access(archivo, os.X_OK))
		    #Outrework.OutPrint(os.path.isfile(archivo))
		    if os.access(archivo, os.X_OK) and os.path.isfile(archivo):
		        archivos += 1
		        estado = os.stat(archivo)  # obtiene estado del archivo
		        tamano = estado.st_size  # obtiene de estado el tamaño 
		        
		        # Obtiene del estado fechas de último acceso/modificación
		        # Como los valores de las fechas-horas vienen expresados
		        # en segundos se convierten a tipo datetime. 
		        
		        ult_acceso = datetime.fromtimestamp(estado.st_atime)
		        modificado = datetime.fromtimestamp(estado.st_mtime)
		        
		        # Se aplica el formato establecido de fecha y hora
		        
		        ult_acceso = ult_acceso.strftime(formato)
		        modificado = modificado.strftime(formato)
		        
		

		        Obj=ObjFile(elemento, modificado, ult_acceso, tamano, _dirPDF,_TYPE)