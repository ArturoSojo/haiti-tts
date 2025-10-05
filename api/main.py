# # from fastapi import FastAPI, Form
# # from redis import Redis
# # from rq.job import Job
# # from rq import Queue
# # import os

# # app = FastAPI()

# # # Conexión a Redis
# # redis_host = os.getenv("REDIS_HOST", "localhost")
# # redis_port = int(os.getenv("REDIS_PORT", 6379))
# # redis_conn = Redis(host=redis_host, port=redis_port)
# # queue = Queue("tts-tasks", connection=redis_conn)


# # @app.get("/health")
# # def health():
# #     return {"status": "ok"}


# # @app.post("/synthesize")
# # def synthesize(text: str = Form(...)):
# #     job = queue.enqueue("haiti_tts_ml.worker.synthesize", text)
# #     return {"job_id": job.id, "status": "queued"}


# # @app.get("/result/{job_id}")
# # def get_result(job_id: str):
# #     job = Job.fetch(job_id, connection=redis_conn)
# #     return {"status": job.get_status(), "result": job.result}
