from string import Template
from config import *
from utils import *


def format_template(data:list)->str:
	if len(data)>0:
		data=[f"'{element}'" for element in data]
		return f"{(',').join(data)},"
	else:
		return ""

def format_string(string:str)->None:
	if len(string)>0:
		return f"'{string}'"
	else:
		return ""

class ProjectTemplateFiller:

	def __init__(self,project,
		apps_installed:list=[],
		middleware_installed:list=[],
		templates:str="",
		language_code:str="'en-us'",
		static_url:str="'static/'",
		others:list=[],
		url_import:list=[],
		paths_import:list=[]
		):

		self.settings_file=project.init_templates.settings_file
		self.urls_file=project.init_templates.urls_file



		self.apps_installed=apps_installed
		self.middleware_installed=middleware_installed
		self.templates=templates
		self.language_code=language_code
		self.static_url=static_url
		self.others=others

		self.url_import=url_import
		self.paths_import=paths_import

		self.project_settings_py={
			"INSTALLED_APPS":format_template(self.apps_installed),
			"MIDDLEWARE":format_template(self.middleware_installed),
			"TEMPLATES":format_string(self.templates),
			"LANGUAGE_CODE":format_string(self.language_code),
			"STATIC_URL":format_string(self.static_url),
			"OTHERS":format_template(self.others)

		}

		self.project_urls_py={
			"IMPORT":format_template(self.url_import),
			"PATHS":format_template(self.paths_import)
		}

	def fill(self):
		self.InjectSettings()
		self.InjectUrls()


	def InjectSettings(self):
		data=Template(open(self.settings_file,"r").read())
		write(data.substitute(self.project_settings_py),self.settings_file)
		print("settings.py file uploaded")

	def InjectUrls(self):
		data=Template(open(self.urls_file,"r").read())
		write(data.substitute(self.project_urls_py),self.urls_file)
		print("urls.py file uploaded")



