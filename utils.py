import os

def createfile (path:str,file_name:str, content=""):
	os.chdir(path)
	with open(file_name , "w", encoding="utf-8") as f:
		f.write("")
		print(f"{path}/{file_name} CREATED")
