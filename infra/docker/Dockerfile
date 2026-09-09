# ============================================
# Dockerfile — Azure Application Platform Lab
# Imagem de produção para a aplicação Flask
# ============================================

# Etapa única — imagem slim para menor superfície de ataque
FROM python:3.12-slim

# Metadados
LABEL maintainer="Matheus Florindo <matheusdideusf@gmail.com>"
LABEL description="Aplicação educacional — Desafio DIO Microsoft Application Platform"

# Variáveis de ambiente com valores padrão seguros
ENV APP_PORT=8000 \
    APP_ENV=production \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências primeiro (cache de camadas Docker)
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY src/app.py .

# Criar usuário não-root por segurança
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Expor porta da aplicação
EXPOSE ${APP_PORT}

# Health check integrado ao Docker
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Iniciar com Gunicorn (WSGI server de produção)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
