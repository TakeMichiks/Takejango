from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

# Implementacion de Tablas Json
from ..tablas.jsontablas import tableTeachers

# Serializacion 
from ..model.serializer import TeachersSerializer

# Mongo Conections
from ..mongo.client import collectionTeachers
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

    # Guardado a Mongo
    mongo = collectionTeachers.insert_one(ser.validated_data)
    # Guardar también en TinyDB (Teachers_Data.json)
    tableTeachers.insert(ser.validated_data)

    return Response(
        {
            "message": "Profesor guardado en SQLite y en JSON",
            "sqlite_id": teacher.id,
            "data": ser.data,
            "guardao": mongo,
        },
        status=status.HTTP_201_CREATED,
    )



