import os 
import re
from enum import Enum
from utils import *


"""PROJECT TEMPLATES"""
class UrlTags(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"from django.urls import path","offset":0,"before":"\n", "end":"\n\n"} #OK
	PATHS={"tag":"$PATHS", "previous_word":"path('admin/', admin.site.urls),","offset":0, "before":"\n	", "end":" ,"} #OK

class SettingsTags(Enum):
	INSTALLED_APPS={"tag":"$INSTALLED_APPS", "previous_word":"django.contrib.staticfiles", "offset":2 ,"before":"", "end":","} #OK
	MIDDLEWARE =  {"tag": "$MIDDLEWARE", "previous_word": "django.middleware.clickjacking.XFrameOptionsMiddleware" , "offset":2,"before":"", "end": ","} #OK
	TEMPLATES= {"tag": "$TEMPLATES" , "previous_word": "DIRS" , "offset":4,"before":"", "end": ""} #OK
	LANGUAGE_CODE= {"tag": "$LANGUAGE_CODE" , "previous_word":"LANGUAGE_CODE" , "offset":3,"before":"", "end": "", 'replace':"'en-us'"} #OK
	STATIC_URL= {"tag": "$STATIC_URL", "previous_word": "STATIC_URL", "offset":3,"before":"", "end": "", "replace":"'static/'" } #OK
	OTHERS= {"tag": "$OTHERS", "previous_word": "'django.db.models.BigAutoField'", "offset":1,"before":"", "end": ""} #OK


class InitTemplates:
	def __init__(self, project):
		self.project=project
		self.settings_file=f"{project.paths.PROJECT_DIR}/{self.project.project_name}/settings.py"
		self.urls_file=f"{project.paths.PROJECT_DIR}/{self.project.project_name}/urls.py"

	def MakeTemplates(self):
		[InjectTag(tag.value, self.settings_file) for tag in SettingsTags]
		[InjectTag(tag.value, self.urls_file ) for tag in UrlTags]




"""APP TEMPLATES"""

class ViewsTags(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"from django.shortcuts import render","offset":1,"before":"\n", "end":"\n\n"} #OK
	VIEW = {"tag":"$VIEWS", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK

class AdminFile(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"from django.contrib import admin","offset":1,"before":"\n", "end":"\n\n"} #OK
	REGISTER = {"tag":"$REGISTER", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK

class FormFile(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"","offset":1,"before":"\n", "end":"\n\n"} #OK
	FORMS = {"tag":"$FORMS", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK

class ModelsFile(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"from django.db import models","offset":1,"before":"\n", "end":"\n\n"} #OK
	MODELS = {"tag":"$MODELS", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK

class UrlsFile(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"","offset":1,"before":"\n", "end":"\n\n"} #OK
	URLS = {"tag":"$URLS", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK

class ValidatorFile(Enum):
	IMPORT={"tag":"$IMPORT", "previous_word":"","offset":1,"before":"\n", "end":"\n\n"} #OK
	VALIDATORS = {"tag":"$VALIDATORS", "previous_word":"$IMPORT","offset":1,"before":"\n", "end":"\n\n"} #OK


class InitAppTemplates:
	def __init__(self, app):
		self.app=app
		self.path=f"{self.app.paths.PROJECT_DIR}/MODULES/{self.app.app_name}/"

		self.views_file = self.path+"views.py"
		self.admin_file = self.path+"admin.py"
		self.apps_file = self.path+"apps.py"
		self.forms_file = self.path+"forms.py"
		self.models_file = self.path+"models.py"
		self.tests_file = self.path+"tests.py"
		self.urls_file = self.path+"urls.py"
		self.validators_file = self.path+"validators.py"

		#Files we will iterate through
		self.files=[self.views_file, self.admin_file, self.apps_file, self.forms_file, self.models_file, self.tests_file, self.urls_file, self.validators_file]

	def InjectTemplateTags(self):
		[InjectTag(tag.value, self.views_file) for tag in ViewsTags]
		[InjectTag(tag.value, self.admin_file) for tag in AdminFile]
		[InjectTag(tag.value, self.forms_file) for tag in FormFile]
		[InjectTag(tag.value, self.models_file) for tag in ModelsFile]
		[InjectTag(tag.value, self.urls_file) for tag in UrlsFile]
		[InjectTag(tag.value, self.validators_file) for tag in ValidatorFile]









