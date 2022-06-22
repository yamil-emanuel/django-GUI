from project import *
from app import *
from template import *
from config import *


class Project:
	"""Project controller, creates virtual enviroment, initializes the project and runs the server """

	def __init__(self, venv_name:str="VENV_DJANGO_GUI", project_name:str="django_project"):
		self.venv_name=venv_name
		self.project_name=project_name
		self.venv=VirtualEnviroment(self.venv_name)#Crea Entorno virtual
		self.paths=DIR(self.venv, self.project_name) #CREAR ROUTING PARA EL PROYECTO
		self.complementaryFolders=ComplementaryFolders(self.paths)
		self.init_templates=InitTemplates(self)


	def start(self):

		self.venv.create()
		self.venv.activate()
		CreateProject(self.venv, self.paths).create() #Creating project + routing
		self.complementaryFolders.CreateFolders() 
		self.init_templates.MakeTemplates() #Inject template tags in base files

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
		app.config()
		ComplementaryFiles(app).create()
		InitAppTemplates(app).InjectTemplateTags()



class Template:
	"""Manages the templates, create"""
	def __init__(self, app:APP, project:Project):
		self.app=app
		self.project=project
	
class TemplateFiller:
	def __init___(self):
		pass


"""HOW TO INIT """
project=Project(VENV_NAME, PROJECT_NAME) #ASIGN PROJECT NAME
project.start() #START

"""CREATING APPS"""
app_list=["app_django"]
apps=[APP(project,app).CreateApp() for app in app_list]


"""FILLING DJANGO PROJECT FILLES (settings&URL)"""
ProjectTemplateFiller(project, 
	apps_installed=apps_installed,
	middleware_installed=middleware_installed,
	templates=templates,
	language_code=language_code,
	static_url=static_url,
	others=others,
	url_import=url_import,
	paths_import=paths_import).fill()

