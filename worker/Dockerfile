FROM python:3.11-slim

RUN useradd -ms /bin/bash appuser
WORKDIR /home/appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY worker.py .

USER appuser
CMD ["python", "worker.py"]