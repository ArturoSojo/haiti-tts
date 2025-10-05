Cómo probar
- Ejecuta Redis localmente:
docker run -d -p 6379:6379 --name redis redis


- Ejecuta el worker en ml/:
poetry run rq worker tts-tasks


- Ejecuta la API en api/:
poetry run uvicorn main:app --reload


- Haz un POST a /synthesize con texto:
curl -X POST -F "text=Bonjour Ayiti!" http://localhost:8000/synthesize




