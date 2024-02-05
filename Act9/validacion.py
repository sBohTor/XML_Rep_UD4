import json
from pickle import FALSE
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
     "Alumnado": {
       "type": "object",
       "properties": {
         "Alumno": {
           "type": "array",
           "items": {
             "type": "object",
             "properties": {
               "NIF": {
                 "type": "string",
                 "pattern": "string"
               },
               "Resultado": {
                 "type": "string",
                 "enum": ["apto", "No apto"]
               },
               "Observaciones": {
                 "type": "string"
               },
               "IP": {
                 "type": "string",
                 "format": "ipv4"
               },
               "MAC": {
                 "type": "string",
                 "pattern": "string"
               }
             },
             "required": ["NIF", "Resultado", "Observaciones"],
             "additionalProperties": FALSE
           }
         }
       },
       "required": ["Alumno"],
       "additionalProperties": FALSE
     }
  },
  "required": ["Alumnado"],
  "additionalProperties": FALSE
 }

# Archivo JSON a validar
archivo_json = '''
{
  "Alumnado": {
    "Alumno": [
      {
        "NIF": [
          "12345678Z"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          "Buen estudiante"
        ],
        "IP": [
          "192.168.1.1"
        ]
      },
      {
        "NIF": [
          "23456789A"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Estudiante regular"
        ],
        "MAC": [
          "00:11:22:33:44:55"
        ]
      },
      {
        "NIF": [
          "34567890B"
        ],
        "Resultado": [
          "apto"
        ],
        "IP": [
          "192.168.1.2"
        ]
      },
      {
        "NIF": [
          "45678901C"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Estudiante con problemas de comportamiento"
        ],
        "MAC": [
          "66:77:88:99:AA:BB"
        ]
      },
      {
        "NIF": [
          "56789012D"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          "Estudiante destacado"
        ],
        "IP": [
          "192.168.1.3"
        ]
      }
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.