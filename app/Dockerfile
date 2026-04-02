FROM python:3.11-slim

WORKDIR /app

# Layer caching: requirements changes less often than app code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Security: never run containers as root
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

HEALTHCHECK --interval= --timeout=5s --retries= \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Production WSGI server, not Flask dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "app:app"]