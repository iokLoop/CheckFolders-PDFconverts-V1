from GEimport import *
# ESTA CLASE CREA EL OBJETO DEL TIPO DIRECTORIO DONDE SE ALMACENA CADA ARCHIVO Y CIERTA INFORMACION ADICIONAL

#sysVar=VariablesSystemas()
#Job=Functions()



class ObjFile():

	def __init__(self, nombre_archivo, ultima_modificacion, ultima_acceso, tamano_Kb, ubucacion_archivo, _TYPE):
		
		MngObj=ManejarObjFile()

		self.dicc={"_nomFILE":nombre_archivo,"_lastMOD":ultima_modificacion,"_lastACS":ultima_acceso,"_weigthKB":tamano_Kb,"_dirPDF":ubucacion_archivo}
		#print("se a creado el nuevo objeto archivo : ", self.dicc["_nomFILE"])
		#print (self.dicc)
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
		return self._LObjAF
		
	def addListaObjFileBEFORE(self,_OBJ):
	
		self._LObjBE.append(_OBJ)
		return self._LObjBE[:]

	def addListaObjFileAFTER(self,_OBJ):
	
		self._LObjAF.append(_OBJ)
		return self._LObjAF[:]
		
	def ShowObjectsListaBefore(self):
		
		total = 0
		linea = '-' * 40
        # Se acumulan tamaños y se muestra info de cada archivo
		for a in self._LObjBE:
			tamano=0
			print(linea)
			print('archivo      :', a["_nomFILE"])
			print('modificado   :', a["_lastMOD"])       
			print('ultimo acceso:', a["_lastACS"])
			tamano=round(int(a["_weigthKB"])/1024, 1)
			print('tamano (Kb)  :', tamano)
			print("Ubicacion del archivo: ",a["_dirPDF"],"\n")
			total= total+tamano

		print(linea)
		print(linea)
		print('Num. archivos:', len(self._LObjBE))
		print('Total (kb)   :', total)

	def GETStateFolder(self,_dirPDF,TYPE):
		#print(_dirPDF)
		_TYPE=TYPE
		contenido = os.listdir(_dirPDF)  # obtiene lista con archivos/dir 
		total = 0
		archivos = 0
		formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
		linea = '-' * 40

		for elemento in contenido:
		    archivo = '{}{}{}'.format(_dirPDF,"/", elemento)
		    print(archivo)
		    #print(os.access(archivo, os.X_OK))
		    #print(os.path.isfile(archivo))
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