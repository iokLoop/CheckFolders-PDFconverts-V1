import os, os.path, string, sys, time
from datetime import datetime
import img2pdf
########################
#   https://pypi.org/project/img2pdf/
########################
from wand.image import Image
########################
#  https://pypi.org/project/Wand/#description
#  http://docs.wand-py.org/en/0.4.4/
########################
#	IMPORTANDO FUNCIONES PROPIAS
#########################
from objetos_dir import *
from functions import *
from system_var import *
#_dirPDF ES LA VARIABLE QUE VA A ALMACENAR EL DIRECTORIO EN DONDE VAN A ESTAR LOS ARCHIVOS PDF EN LA CUAL VA A TRABAJAR EL SCRIPT
#_dirDES ES LA VARIABLE QUE VA A ALMACENAR 
#_orgPC ES LA VARIABLE QUE VA A ALMACENAR
#_destPC ES LA VARIABLE QUE VA A ALMACENAR
#__convert2PDF ES LA VARIABLE QUE VA A ALMACENAR 

