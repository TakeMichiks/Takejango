# Importaciones de rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# Importacion de Django
from django.http import JsonResponse

# Importaciones Adc
from tinydb import TinyDB
import zipfile
from pathlib import Path

# Import Serializer
from .serializer import TeachersSerializer, StudentsSerializer

# Archivos json
students_db = TinyDB("Stundents_Data.json", indent=4)
teachers_db = TinyDB("Teachers_Data.json", indent=4)

# Tablas
tableStudents = students_db.table("Students")
tableTeachers = teachers_db.table("Teachers")


@api_view(["GET"])
def time(request):
    basetime = timezone.now()
    hora_actual = timezone.localtime(basetime)
    hora_str = hora_actual.strftime("%I:%M:%S:%p")

    return JsonResponse({"Hora Actual": hora_str}, status=status.HTTP_200_OK)


# ---------- Teachers ----------

@api_view(["GET"])
def teachers(request):
    all_teachers = tableTeachers.all()

    for teacher in all_teachers:
        teacher["id"] = teacher.doc_id

    # safe=False para devolver lista
    return JsonResponse(all_teachers, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
def teachersdata(request):
    ser = TeachersSerializer(data=request.data)

    if not ser.is_valid():
        # Devolver errores detallados
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # Guardar en SQLite
    teacher = ser.save()

    # Guardar también en TinyDB (Teachers_Data.json)
    tableTeachers.insert(ser.validated_data)

    return Response(
        {
            "message": "Profesor guardado en SQLite y en JSON",
            "sqlite_id": teacher.id,
            "data": ser.data,
        },
        status=status.HTTP_201_CREATED,
    )


# ---------- Students ----------

@api_view(["GET"])
def students(request):
    all_students = tableStudents.all()

    for student in all_students:
        student["id"] = student.doc_id

    return JsonResponse(all_students, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
def studentsdata(request):
    ser = StudentsSerializer(data=request.data)

    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # Guardar en SQLite
    student = ser.save()

    # Guardar también en TinyDB (Stundents_Data.json, tabla Students)
    tableStudents.insert(ser.validated_data)

    return Response(
        {
            "message": "Estudiante guardado en SQLite y en JSON",
            "sqlite_id": student.id,
            "data": ser.data,
        },
        status=status.HTTP_201_CREATED,
    )

