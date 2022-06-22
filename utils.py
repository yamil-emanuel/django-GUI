import os

def createfile (path:str,file_name:str, content=""):
	os.chdir(path)
	with open(file_name , "w", encoding="utf-8") as f:
		f.write("")
		print(f"{path}/{file_name} CREATED")


def write(data,name):
	with open(name, "w") as f:
		f.write(data)


def InjectTag( tag:dict, file):

	with open(file, "r", encoding="utf-8") as f:
		data=str(f.read())
		if "replace" in tag.keys():
			data=data.replace(tag["replace"],"")

		if tag["tag"] not in data:
			previous_word=tag["previous_word"]
			offset = tag["offset"]
			previous_word_length =len(previous_word)
			i=data.index(previous_word) #where the last word is
			if tag["end"]!="":
				file_data=data[:(i+previous_word_length+offset)] +tag["before"] + tag["tag"] + tag["end"] + data[(i+previous_word_length+offset):]
				write(file_data, file)
			else:
				file_data=data[:(i+previous_word_length+offset)] +tag["before"] + tag["tag"] + data[(i+previous_word_length+offset):]
				write(file_data, file)

