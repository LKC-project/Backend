$env:DEV="True"
uvicorn src.main:app --host "localhost" --port 14088 --reload --timeout-graceful-shutdown 0
