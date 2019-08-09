from GEimport import *
from multiprocessing import Process, Queue
########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################

from functions import *
from objetos_dir import *
from system_var import *
#print (system_var.__file__)
print("la variable __name__ en Built es  : ",__name__)
print("la variable __file__ en Built es : ",__file__)
#print("la variable __path__ en Built es : ",__path__)
sysVar=VariablesSystemas()
Job=FunctionsClass()
MngObj=ManejarObjFile()
print("1. Cargando las variables de entorno del archivo de configuracion")
print("2. Opteniendo el estado original de la carpeta en directorios")
MngObj.GETStateFolder(sysVar.Get("VarDirPDF"),"BEFORE")
while 1:
	time.sleep (5)
	MngObj.CLEARListaObjAF()
	L=MngObj.GETListaObjAF()
	print("\n\n\n el valor de lista after luego de limpiarla es: >>> ",L)
	_change=Job.DirChangeDetect()
	#_list=MngObj.GET_ListaBefore()
	if _change == True :
		print("valor de variable renombrar x script es: ",sysVar.Get("VarUseRenByScrypt"))
		print("3. Llamando la funcion de cabio de nombre")
		_convertToPDF=Job.CambiarNombrePDF(sysVar.Get("VarDirPDF"), sysVar.Get("VarConvertToPDF"))
		time.sleep (5)
		Job.DirChangeDetect()
		if _convertToPDF==True:
			#lanzando funciones como subproceso con el objetivo de forzar la ejecucion de la misma antes de continuar con la siguiente
			# queue = Queue()
			_error=Job.ConvertToPDF(sysVar.Get("VarDirPDF"),sysVar.Get("VarImgMagickDir"))
			# _subProcess = Process(target=Job.ConvertToPDF, args=(sysVar.Get("VarDirPDF"), sysVar.Get("VarImgMagickDir")))
			# _subProcess.start()
			# _subProcess.join()
			# _error = queue.get()
			
		
		if _error==True:
			# queue = Queue()
			Job.ConvertToPDF(sysVar.Get("VarDirPDF"),sysVar.Get("VarImgMagickDir"))
			# _subProcess = Process(target=Job.ConvertToPDF, args=(sysVar.Get("VarDirPDF"), sysVar.Get("VarImgMagickDir")))
			# _subProcess.start()
			# _subProcess.join()
			#_error = queue.get()
			
			_error=False

		Job.MoverPDF()
	else:
		print("<<<<< nada que hacer  >>>>>")
