from django.urls import path
from . import views

urlpatterns = [
    path("time", views.time, name="Time"),
    path("teachers/data", views.teachersdata, name="TeachersDataGET"),
    path("teachers/datapost", views.teachersdata, name="TeachersDataPOST"),
    path("students/data", views.students, name="TeachersDataGET"),
    path("students/datapost", views.studentsdata, name="TeachersDataPOST"),
]
