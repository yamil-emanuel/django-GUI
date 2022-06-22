import os 
from enum import Enum


class CONFIG (Enum):
	BASE_PATH=os.getcwd()

class InitialDependencies(Enum):
	VENV="virtualenv"
	REQUESTS="requests"
	DJANGO="Django"

class InstallInitialRequieriments:
	def __init__(self, requieriment:InitialDependencies):
		self.requieriment=requieriment


	def Install(self):
		os.system(f"pip install {self.requieriment}")
		print(f"Installing {self.requieriment}")

class VirtualEnviroment:
	def __init__(self, VENV_NAME):
		self.VENV_NAME=VENV_NAME
	
	def create(self):
		if os.path.isdir(f"{CONFIG.BASE_PATH.value}/{self.VENV_NAME}"):
			print("VirtualEnviroment already exists.")
		else:
			print(f"Creating virtual enviroment : {self.VENV_NAME} .")
			os.system(f"virtualenv {self.VENV_NAME}")


	def activate(self):
		print(f"Activating virtual enviroment : {self.VENV_NAME} ")
		os.chdir("..")
		os.chdir(f"{CONFIG.BASE_PATH.value}/{self.VENV_NAME}/Scripts")
		os.startfile("activate")
		os.chdir("..")

class DIR:
	def __init__(self, venv:VirtualEnviroment):
		self.venv=venv
		self.PROJECT_DIR=f"{CONFIG.BASE_PATH.value}/{self.venv.VENV_NAME}/{self.venv.VENV_NAME}"
		self.VENV_DIR=f"{CONFIG.BASE_PATH.value}/{self.venv.VENV_NAME}"

class Navigator:
	def navigate_to(path):
		os.system("..")
		os.chdir(path)

class RunServer:
	def __init__(self, venv:VirtualEnviroment):
		self.venv=venv

	def run(self):
		self.venv.activate()
		os.chdir(DIR.PROJECT_DIR)
		os.system("python manage.py runserver")
		print("Running")

class CreateProject:
	def __init__(self, venv:VirtualEnviroment, paths=DIR):
		self.venv=venv
		self.paths=paths

	def create (self):

		if os.path.isdir(self.paths.PROJECT_DIR): #If path exists
			print("Project already exists.")
		else:
			print(f"Creating project : {self.venv.VENV_NAME}")
			os.chdir(f"{self.paths.VENV_DIR}")
			os.system(f"django-admin startproject {self.venv.VENV_NAME}")

class ComplementaryFolders:
	#CREATE YOUR FOLDER HERE

	def __init__(self, paths:DIR):
		self.paths=paths
		self.modules={"name":"MODULES", "path":f"{self.paths.PROJECT_DIR}"}
		self.static={"name":"static", "path": f"{self.paths.PROJECT_DIR}"}
		self.assets={"name":'assets',"path":f"{self.paths.PROJECT_DIR}\\static"}
		self.css={"name":'css',"path":f"{self.paths.PROJECT_DIR}\\static\\assets"}
		self.js={"name":'js',"path":f"{self.paths.PROJECT_DIR}\\static\\assets"}
		self.img={"name":'img',"path":f"{self.paths.PROJECT_DIR}\\static\\assets"}
		self.TEMPLATES={"name":"templates", "path": f"{self.paths.PROJECT_DIR}"}

		self.order=[self.static, self.TEMPLATES, self.assets, self.modules, self.css, self.js, self.img]

	def CreateFolders(self):
		for folder in self.order:
			if type(folder) == dict and folder["name"]!=None:
				#os.chdir("..")
				path = f"{folder['path']}"
				name= f"{folder['name']}"
				try:
					os.chdir(path)
					os.makedirs(name)
					print(f"Folder {name} created.")
				except FileExistsError:
					print(f"Folder {name} already exists.")

