from django.urls import path
from .routes import views
from .routes import teachers
from .routes import students
from .routes import auth

urlpatterns = [
    path("time", views.time, name="Time"),
    path("teachers/data", teachers.teachersdata, name="TeachersDataGET"),
    path("teachers/datapost", teachers.teachersdata, name="TeachersDataPOST"),
    path("students/data", students.students, name="TeachersDataGET"),
    path("students/datapost", students.studentsdata, name="TeachersDataPOST"),
    path("SegureData", views.zipfiles, name="SegureData"),
    path("register", auth.register, name="register"),
    path("login", auth.login, name="Login"),
]
