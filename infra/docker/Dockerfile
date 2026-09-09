FROM python:3.12-slim

LABEL maintainer="Matheus Florindo"
LABEL description="Aplicação educacional — Desafio DIO Microsoft Application Platform"

ENV APP_PORT=8000 \
    APP_ENV=production \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
