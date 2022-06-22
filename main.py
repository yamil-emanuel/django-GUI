from project import *
from app import *
from template import *

class Project:
	"""Project controller, creates virtual enviroment, initializes the project and runs the server """

	def __init__(self, project_name:str):
		self.project_name=project_name
		self.venv=VirtualEnviroment(self.project_name)#Crea Entorno virtual
		self.paths=DIR(self.venv) #CREAR ROUTING PARA EL PROYECTO
		self.complementaryFolders=ComplementaryFolders(self.paths)


	def start(self):

		self.venv.create()
		self.venv.activate()
		CreateProject(self.venv, self.paths).create() #Creating project + routing
		self.complementaryFolders.CreateFolders() 
		InitTemplates(self).MakeTemplates() #Inject

	def run_server(self):
		self.venv.activate()

class APP:
	""" Manages all the apps of the project """
	def __init__(self, project:Project, app_name:str):
		self.project=project
		self.app_name=app_name


	def CreateApp(self):
		app=CreateApp(venv=self.project.venv, paths=self.project.paths, app_name=self.app_name) 
		app.create()
		ConfigureAPP(app).SetRouting()
		ComplementaryFiles(app).create()

class Template:
	"""Manages the templates, create"""
	def __init__(self, app:APP):
		self.app=app
	
class TemplateFiller:
	def __init___(self, template:Template, app:APP):
		pass


"""HOW TO INIT """
project_name="PRUEBA2"
project=Project(project_name) #ASIGN PROJECT NAME
project.start() #START


