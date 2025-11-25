from tinydb import TinyDB
from ..carpetas.dirs import JSONSTUDENTS,JSONTEACHERS,JSONUSER,JSONDATA

# Archivos json
students_db = TinyDB(JSONSTUDENTS, indent=4)
teachers_db = TinyDB(JSONTEACHERS, indent=4)
user_db = TinyDB(JSONUSER, indent=4)
data_db = TinyDB(JSONDATA, indent=4)

# Tablas
tableStudents = students_db.table("Students")
tableTeachers = teachers_db.table("Teachers")
tableUser = user_db.table("user")
tablaData = data_db.table("Data")
