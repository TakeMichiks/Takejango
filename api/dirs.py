from pathlib import Path

BASE_DIR = Path(__file__).parent
TEACHERS_DIR = Path(BASE_DIR).parent / "Data" / "Teachers"
STUDENTS_DIR = Path(BASE_DIR).parent / "Data" / "Students"
JSONTEACHERS = Path(TEACHERS_DIR).parent / "TeachersData.json"
JSONSTUDENTS = Path(STUDENTS_DIR).parent / "StudentsData.json"
