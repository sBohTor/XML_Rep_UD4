import json
import datetime
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print(f"JSON inválido: {error}")
    return False
from datetime import datetime
def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False
with open("SebastianBohorquez_Ex_UD4_LMSGI/Ejercicio1/datos.json") as json_file:
    data = json.load(json_file)
if "fecha_nacimiento" in data:
    if validate_date_format(data["fecha_nacimiento"]):
        print("Fecha de nacimiento válida")
    else:
        print("Fecha de nacimiento inválida")
else:
    print("No se encontró la clave 'fecha_nacimiento' en el JSON")