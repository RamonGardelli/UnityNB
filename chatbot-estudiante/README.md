# RASA
Este repositorio almacena un chatbot implementado con el framework RASA para un trabajo práctico de la materia Diseño de Sistemas de Software.

# Train model
# console
rasa train --domain ./domain

# Probar en consola
rasa shell

# RASA Test para correr los tests stories (salida en results)
rasa test

# Server
rasa run --enable-api

# Si tira error, re-entrenar el modelo!

# Consultarle a la api:

method: POST
url: localhost:5005/webhooks/rest/webhook
Content-Type: application/json

body: 
{
  "sender": "Maxi",
  "message": "Hola amigo"
}

# Respuesta esperada:
[
    {
        "recipient_id": "Maxi",
        "text": "Como dice que le va"
    },
    {
        "recipient_id": "Maxi",
        "text": "Que onda compañero como estás?"
    }
]