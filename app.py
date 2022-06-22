from string import Template
from templates.project_base import *
from templates.app_base import *
from project import * 
from utils import *
from config import *

class CreateApp:
	def __init__(self, venv:VirtualEnviroment, app_name, paths:DIR):
		self.venv=venv
		self.app_name=app_name
		self.paths=paths
		self.app_file=f"{self.paths.PROJECT_DIR}/MODULES/{self.app_name}/apps.py"
		


	def create(self):
		if os.path.isdir(f"{self.paths.PROJECT_DIR}/MODULES/{self.app_name}"):
			print(f"App {self.app_name} already exists.")
		else:
			print(f"Creating APP : {self.app_name}")
			os.chdir(f"{self.paths.PROJECT_DIR}/MODULES/")
			os.system(f"django-admin startapp {self.app_name}")

	def config(self):
		ConfigureAPP(self).SetRouting()
		ConfigureAPP(self).InstallApp()

class ConfigureAPP(CreateApp):
	def __init__(self, app):
		self.app=app

	def SetRouting(self):
		#Overrides APP name in MODULES/APP_NAME/app.py 
		with open ( self.app.app_file , "r", encoding="utf-8") as f:
			data=f.read()
			if f"MODULES.{self.app.app_name}" not in data:

				print(f"Configuring apps.py : {self.app.app_name}")

				data=data.replace(f"{self.app.app_name}" , f"MODULES.{self.app.app_name}")

				with open(self.app.app_file, 'w') as file:
					file.write(data)
			else:
				print("apps.py already configured")

	def InstallApp(self):
		print("INSTALLING APP")
		apps_installed.append(f"MODULES.{self.app.app_name}")

class ComplementaryFiles(CreateApp):
	def __init__(self, app:CreateApp):
		self.app=app
		self.path=f"{self.app.paths.PROJECT_DIR}/MODULES/{self.app.app_name}"

		self.files=["urls.py","validators.py","forms.py","app_config.py"]

	def create(self):
		for file in self.files:
			createfile(self.path, file)
			



