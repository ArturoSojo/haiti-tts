# haiti-tts
poetry run uvicorn main:app --reload
poetry run rq worker tts-tasks