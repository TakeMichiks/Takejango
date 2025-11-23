from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.parent / "Data" 

JSONTEACHERS = DATA_DIR / "TeachersData.json"
JSONSTUDENTS = DATA_DIR / "StudentsData.json"
JSONUSER = DATA_DIR / "user.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
