"""
Azure Application Platform Lab — Aplicação Educacional

Aplicação web mínima em Flask para demonstrar:
- Containerização com Docker
- Deploy em Azure App Service / Container Apps
- Orquestração com Kubernetes / AKS
- Observabilidade com Application Insights

Autor: Matheus Florindo
Projeto: Desafio DIO — Microsoft Application Platform
"""

import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuração via variáveis de ambiente (12-Factor App)
APP_PORT = int(os.getenv("APP_PORT", 8000))
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    """Endpoint principal — página de boas-vindas."""
    return jsonify({
        "message": "Azure Application Platform Lab",
        "status": "running",
        "environment": APP_ENV,
        "docs": "/health"
    })


@app.route("/health")
def health():
    """Health check — utilizado por Kubernetes liveness/readiness probes."""
    return jsonify({
        "status": "healthy",
        "service": "azure-app-platform-lab",
        "version": "1.0.0"
    })


@app.route("/info")
def info():
    """Informações do ambiente — útil para validação de deploy."""
    return jsonify({
        "app": "Azure Application Platform Lab",
        "version": "1.0.0",
        "environment": APP_ENV,
        "python_port": APP_PORT,
        "description": "Projeto educacional — Desafio DIO Microsoft Application Platform"
    })


if __name__ == "__main__":
    # Em produção, utilizar Gunicorn ou outro WSGI server.
    # Ex: gunicorn app:app --bind 0.0.0.0:8000
    app.run(host="0.0.0.0", port=APP_PORT, debug=(APP_ENV == "development"))
