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
#Job.ListarDirectorio(sysVar.VarDirPDF())
print("2. Opteniendo el estado original de la carpeta en directorios")
MngObj.GETStateFolder(sysVar.VarDirPDF(),"BEFORE")

while 1:
	time.sleep (2)
	print("\n\n\n3. Verificar cambios en directorios")
	MngObj.CLEARListaObjAF()
	L=MngObj.GETListaObjAF()
	print("\n\n\n el valor de lista after luego de limpiarla es: >>> ",L)
	Job.DirChangeDetect()

	
	# print("3. Llamando las funcion de cabio de nombre")
	# print("valor de variable renombrar x script es: ",sysVar.VarUseRenByScrypt())
	# #Job.CambiarNombrePDF(sysVar.VarDirPDF(), sysVar.VarConvertToPDF(),sysVar.VarImgMagickDir())
	# MngObj.ShowObjectsListaBefore()