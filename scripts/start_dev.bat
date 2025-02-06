.\venv\Scripts\activate
set DEV=True
uvicorn src.main:app --host 127.0.0.1 --port 14088 --reload
