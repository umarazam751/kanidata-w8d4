FROM python:3.11-slim

WORKDIR /app

# Cache deps separately from code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then the source
COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "pipeline.py"]