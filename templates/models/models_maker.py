from enum import Enum

class ModelOptions:
	def __init__(self, null:bool=False, blank:bool=False, choices:list=[], db_column:bool=False, db_index:bool=False, default:str="",
	 editable:bool=True, error_messages:str, help_text:str, primary_key:bool=False,
		unique:bool=False, unique_for_date:bool=False, unique_for_month:bool=False, unique_for_year:bool=False, verbose_name:bool=False, validators:list=[])
	null=[True, False]
	blank=[True, False]
	#choices
	db_column=""
	db_index="True"
	default=""
	editable=
	error_messages=
	help_text=""
	primary_key=[None,True]
	unique=[True,False]
	unique_for_date=[True,False]
	unique_for_month=[True, False]
	unique_for_year=[True,False]
	verbose_name=""
	validators=""




class ModelField(Enum):
	AutoField=f""
	CharField=f"models.Charfield(max_length=)"
	DateField=f"models.DateField(auto_now="
	DateTimeField=""
	EmailField=""
	IntegerField=""		
	TextField=""
	ForeignKey=""

class FieldOptions(ModelField):
	def __init__(self, fields):
		self.fields=fields

