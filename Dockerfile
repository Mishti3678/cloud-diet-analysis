From python:3.10-slim

WORKDIR /app

COPY flask_app.py .
COPY input.txt .

RUN pip install flask

Expose 5000

CMD ["python", "flask_app.py"]
