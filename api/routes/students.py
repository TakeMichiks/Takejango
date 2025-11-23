from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

from ..model.serializer import StudentsSerializer
from ..tablas.jsontablas import tableStudents 

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
