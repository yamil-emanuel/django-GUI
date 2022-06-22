import os 
import re
from enum import Enum


def write(data,n):
	with open(n, "w") as f:
		f.write(data)


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
		[self.InjectTag(tag.value, self.settings_file) for tag in SettingsTags]
		[self.InjectTag(tag.value, self.urls_file ) for tag in UrlTags]


	def InjectTag(self, tag:dict, file):

		with open(file, "r", encoding="utf-8") as f:
			data=f.read()

			if "replace" in tag.keys():
				data=str(data).replace(tag["replace"],"")
			
			previous_word=tag["previous_word"]
			offset = tag["offset"]
			previous_word_length =len(previous_word)
			i=str(data).index(previous_word) #where the last word is
			if tag["end"]!="":
				file_data=(str(data)[:(i+previous_word_length+offset)] +tag["before"] + tag["tag"] + tag["end"] + str(data)[(i+previous_word_length+offset):])
				write(file_data, file)
			else:
				file_data=(str(data)[:(i+previous_word_length+offset)] +tag["before"] + tag["tag"] + str(data)[(i+previous_word_length+offset):])
				write(file_data, file)




	def InjectTemplateTags(self):
		pass




class APPTemplates:
	def __init__(self):
		pass

	def InjectTemplateTags(self):
		pass

