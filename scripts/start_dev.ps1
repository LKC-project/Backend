$env:ENV="DEV"
uvicorn src.main:app --host "localhost" --port 14088 --reload --ssl-keyfile=localhost-key.pem --ssl-certfile=localhost.pem --timeout-graceful-shutdown 0
