FROM python:3.11-slim

# non-root user
RUN useradd -ms /bin/bash appuser
WORKDIR /home/appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
