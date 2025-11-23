# Importaciones de rest_framework
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils import timezone

# Importacion de Django
from django.http import JsonResponse,FileResponse

# Importaciones Adc
import zipfile
from pathlib import Path
import os
import io

from ..carpetas.dirs import DATA_DIR

# ------- Time ---------

@api_view(["GET"])
def time(request):
    basetime = timezone.now()
    hora_actual = timezone.localtime(basetime)
    hora_str = hora_actual.strftime("%I:%M:%S:%p")

    return JsonResponse({"Hora Actual": hora_str}, status=status.HTTP_200_OK)

# ------- Zipfiles ---------

@api_view(["GET"])
def zipfiles(request):

    basedir = DATA_DIR

    if not basedir.exists():
        return JsonResponse("Error no existe la carpeta")

    
    files = [ Path(root) / name for root,_,names in os.walk(basedir) for name in names]

    memory_zip = io.BytesIO()

    with zipfile.ZipFile(memory_zip, "w", compression=zipfile.ZIP_DEFLATED) as fz:
        for p in files:
            arcname = p.relative_to(basedir)
            fz.write(p,arcname)

    memory_zip.seek(0)

    return FileResponse(memory_zip, as_attachment=True, filename=f"Data_{basedir}.zip")


