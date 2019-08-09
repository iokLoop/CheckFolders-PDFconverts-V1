##usar un diccionario para estructura de base de datos almacenada en archivo binario
import pickle

class personas():

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("se a creado una nueva persona con el nombre: ",self.nombre)




class ManejarPersonas():
	
	Lpersonas=[]
	
	def __init__(self):
		
		ListaDePersonasArchivo=open(r"C:\Users\Karla\Desktop\Sublime_Text_Build_3143_x64\PROGRAMAS\app_grafica_db\db","rb")
		ListaDePersonasArchivo.seek(0)
		try:
			self.Lpersonas=pickle.load(ListaDePersonasArchivo)
			print("Se cargaron {} personas existentes en el fichero externo\n".format(len(self.Lpersonas)))

		except:
			print("el fichero esta vacio")

		finally:
			ListaDePersonasArchivo.close()
			del(ListaDePersonasArchivo)

	def agregarPersonas(self,p):
		self.Lpersonas.append(p)
		self.GuardarPersonasFicheroExterno()

	def GuardarPersonasFicheroExterno(self):
		ListaDePersonasArchivo=open(r"C:\Users\Karla\Desktop\Sublime_Text_Build_3143_x64\PROGRAMAS\app_grafica_db\db","wb+")
		pickle.dump(self.Lpersonas,ListaDePersonasArchivo)
		ListaDePersonasArchivo.close()
		del(ListaDePersonasArchivo)

	def MostrarInfoFicheroExterno(self):
		LpersonasExterno=[]
		ListaDePersonasArchivo=open(r"C:\Users\Karla\Desktop\Sublime_Text_Build_3143_x64\PROGRAMAS\app_grafica_db\db","rb")
		ListaDePersonasArchivo.seek(0)
		print("\nLa(s) persona(s) almacenada(s) en el fichero externo es(son): \n")
		self.LpersonasExterno=pickle.load(ListaDePersonasArchivo)
		for i in self.LpersonasExterno:
			print(i)

		ListaDePersonasArchivo.close()
		del(ListaDePersonasArchivo)

miLista=ManejarPersonas()
'''p=personas("alejandra", "Femenino", "39")
miLista.agregarPersonas(p)
p=personas("yoka", "TransFemenino", "35")
miLista.agregarPersonas(p)
p=personas("mario", "masculino", "10")
miLista.agregarPersonas(p)
p=personas("juan", "transmasculino", "25")
miLista.agregarPersonas(p)'''

miLista.MostrarInfoFicheroExterno()

