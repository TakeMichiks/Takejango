from django.urls import path
from .routes import views
from .routes import teachers
from .routes import students
from .routes import auth

urlpatterns = [
    # Urls for views
    path("time", views.time, name="Time"),
    path("SegureData", views.zipfiles, name="SegureData"),

    # Urls for students
    path("students/data", students.students, name="TeachersDataGET"),
    path("students/datapost", students.studentsdata, name="TeachersDataPOST"),

    # Urls for Teachers
    path("teachers/data", teachers.teachersdata, name="TeachersDataGET"),
    path("teachers/datapost", teachers.teachersdata, name="TeachersDataPOST"),

    # Urls for Auth
    path("register", auth.register, name="register"),
    path("login", auth.login, name="Login"),
]
