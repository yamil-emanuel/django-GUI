from string import Template
from utils import *

view_name="pepe"
parameters=""
view_content="nothing"
return_type="HttpResponse"
return_content="('hola')"

url_attributes=""
path=""

v={"IMPORT":"from django.http import HttpResponse",

"VIEWS":f"""
    def {view_name} (request {parameters}):
        {view_content}
        return {return_type} {return_content}
"""}



path=f"""path('{path}{url_attributes}', {view_name}, name='{view_name}'), """  

def fill():
    data=Template(open("C:\\Users\\yamil\\DJANGO-GUI\\VENV_PRUEBA2\\TODO_APP\\MODULES\\app_django\\views.py","r").read())
    print(data.substitute(v))
    print(path)
fill()