from GEimport import *
sysVar=VariablesSystemas()
Job=Functions()
MngObj=ManejarObjFile()

print("1. Cargando las variables de entorno del archivo de configuracion")
Job.ListarDirectorio(sysVar.VarDirPDF())
print("2. Opteniendo el estado original de la carpeta en directorios")
MngObj.GETStateFolder(sysVar.VarDirPDF(),"BEFORE")

while 1:
	time.sleep (1)
	print("3. Verificar cambios en directorios")
	Job.DirChangeDetect()

	
	print("3. Llamando la funcion de cabio de nombre")
	print("valor de variable renombrar x script es: ",sysVar.VarUseRenByScrypt())
	#Job.CambiarNombrePDF(sysVar.VarDirPDF(), sysVar.VarConvertToPDF(),sysVar.VarImgMagickDir())
	MngObj.ShowObjectsListaBefore()