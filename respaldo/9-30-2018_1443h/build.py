from GEimport import *

########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################
from functions import *
from objetos_dir import *
from system_var import *

sysVar=VariablesSystemas()
Job=FunctionsClass()
MngObj=ManejarObjFile()
print("1. Cargando las variables de entorno del archivo de configuracion")
print("2. Opteniendo el estado original de la carpeta en directorios")
MngObj.GETStateFolder(sysVar.VarDirPDF(),"BEFORE")
while 1:
	time.sleep (5)
	MngObj.CLEARListaObjAF()
	L=MngObj.GETListaObjAF()
	print("\n\n\n el valor de lista after luego de limpiarla es: >>> ",L)
	_change=Job.DirChangeDetect()
	if _change == True:
		print("valor de variable renombrar x script es: ",sysVar.VarUseRenByScrypt())
		print("3. Llamando la funcion de cabio de nombre")
		_convertToPDF=Job.CambiarNombrePDF(sysVar.VarDirPDF(), sysVar.VarConvertToPDF())
		time.sleep (5)
		Job.DirChangeDetect()
		if _convertToPDF==True:
			_error=Job.ConvertToPDF(sysVar.VarDirPDF(),sysVar.VarImgMagickDir())
		
		if _error==True:
			Job.ConvertToPDF(sysVar.VarDirPDF(),sysVar.VarImgMagickDir())
			_error=False

		Job.MoverPDF()
	else:
		print("<<<<< nada que hacer  >>>>>")
