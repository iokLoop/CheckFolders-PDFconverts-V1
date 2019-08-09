''' para instalar PIL es necesario
	https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/
	https://pypi.python.org/pypi/Pillow/5.0.0#downloads
	https://github.com/bnmnetp/cImage
	carpeta en windows donde esta python   C:\Users\Karla\AppData\Local\Programs\Python\Python36\Lib\site-packages
		uso
		http://docs.python-guide.org/en/latest/scenarios/imaging/
		http://python-para-impacientes.blogspot.com/2014/12/fundamentos-para-procesar-imagenes-con_16.html
		
'''
#convertir png a .ico


from PIL import Image
filename = r'py.png'
img = Image.open(filename)
#img.save('logo.ico')
#Opcionalmente, puede especificar los tamaños de icono que desee:

icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save('logo.ico', sizes=icon_sizes)
'''Los documentos Pillow dicen que, por defecto, generará tamaños [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)] y se ignorará cualquier tamaño más grande que el tamaño original o 255.
	Sí, está en la sección de solo lectura de los documentos, pero funciona hasta cierto punto.'''

