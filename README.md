# ☁️ Microsoft Azure Application Platform Lab

**Projeto prático desenvolvido como desafio da DIO — Microsoft Application Platform.**

[![Validate Project](https://github.com/matheusflorindo32/azure-application-platform-lab/actions/workflows/validate.yml/badge.svg)](https://github.com/matheusflorindo32/azure-application-platform-lab/actions/workflows/validate.yml)
[![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## Visão geral

Este repositório transforma os conceitos estudados na formação **Microsoft Application Platform** em um laboratório pequeno, executável e auditável. A implementação usa uma API Flask como carga de trabalho de referência para demonstrar testes automatizados, containerização com Docker, execução real em Kubernetes local, CI com GitHub Actions, fundamentos de segurança e arquitetura Azure.

O projeto evita declarar infraestrutura cloud que não tenha sido realmente provisionada. App Service, Azure Container Apps, AKS, Application Insights e Log Analytics são documentados como alternativas e conceitos estudados enquanto não houver evidência real de execução.

> **Objetivo:** demonstrar qualidade de engenharia e aprendizado verificável sem ampliar artificialmente o escopo do desafio.

## O desafio da DIO

A entrega proposta pela DIO solicita, em essência:

1. criar um repositório próprio;
2. documentar o processo em `README.md`;
3. incluir prints/evidências;
4. registrar insights e aprendizados;
5. compartilhar o repositório como projeto de portfólio.

**Referência oficial:** [digitalinnovationone/Microsoft_Application_Platform](https://github.com/digitalinnovationone/Microsoft_Application_Platform)

## O que este projeto demonstra

- API REST mínima com **Python 3.12 + Flask**;
- configuração por variáveis de ambiente;
- endpoints `/`, `/health` e `/info`;
- testes automatizados com **pytest**;
- container Docker com **Gunicorn** e execução como usuário não-root;
- health check do container;
- Kubernetes `Deployment` com 2 réplicas;
- liveness/readiness probes e requests/limits;
- workload Kubernetes com `runAsNonRoot`, UID/GID explícitos, `seccomp`, capabilities removidas e privilege escalation desabilitado;
- `Service` do tipo `LoadBalancer`;
- execução real em **Kubernetes local via Docker Desktop + kind**;
- validação do endpoint `/health` através do Service Kubernetes via `port-forward`;
- CI bloqueante com **GitHub Actions**;
- smoke test real do container chamando `/health`;
- arquitetura conceitual para App Service, Container Apps e AKS;
- fundamentos de Application Insights e Log Analytics;
- separação entre código, infraestrutura, documentação e evidências;
- boas práticas para não versionar secrets.

## Arquitetura

![Arquitetura conceitual](docs/diagrams/architecture.svg)

> O diagrama apresenta **alternativas de hospedagem estudadas**, e não três deploys Azure simultâneos.

Fluxo técnico comprovado no laboratório:

```text
Código Flask
    ↓
pytest
    ↓
Docker build
    ↓
Container + /health
    ↓
GitHub Actions
    ↓
Docker Desktop + kind
    ↓
Kubernetes Deployment (2 réplicas)
    ↓
Service + port-forward
    ↓
/health → healthy
```

A versão Mermaid e a explicação detalhada estão em [`docs/architecture.md`](docs/architecture.md).

## Stack

| Área | Tecnologia | Papel no projeto |
|---|---|---|
| Aplicação | Python 3.12 + Flask | API educacional |
| Servidor | Gunicorn | Execução WSGI no container |
| Testes | pytest | Validação dos endpoints |
| Container | Docker | Empacotamento e portabilidade |
| Orquestração | Kubernetes v1.36.1 + kind | Deployment, Service, probes e validação local |
| Runtime local | Docker Desktop + containerd image store | Execução do cluster Kubernetes local |
| Cloud | Microsoft Azure | Plataforma estudada para hospedagem |
| Observabilidade | Application Insights / Log Analytics | Telemetria e análise de logs |
| CI | GitHub Actions | Testes, lint e smoke test Docker |

## Projeto DIO × implementação autoral

| Aspecto | Referência DIO | Implementação neste repositório |
|---|---|---|
| Aplicação | Labs e exemplos educacionais | API Flask pequena e reproduzível |
| Containers | Conceitos e exemplos | Dockerfile funcional com non-root e health check |
| Kubernetes | Manifests educacionais | Deployment + Service + probes + limites + hardening + execução local comprovada |
| Segurança | Conteúdo de estudo | `.gitignore`, `.env.example`, non-root e workload restrito |
| Testes | Dependente do laboratório | pytest para os três endpoints |
| CI | Não é requisito central | GitHub Actions bloqueante |
| Arquitetura | Conteúdo da trilha | Mermaid + SVG + documentação de decisões |
| Evidências | Responsabilidade do aluno | Evidências locais, Docker, pytest, CI e Kubernetes registradas no repositório |

A comparação acima não substitui nem deprecia o material original; ela mostra como os conceitos foram reorganizados em uma entrega autoral de portfólio.

## Estrutura do repositório

```text
azure-application-platform-lab/
├── .github/workflows/
│   └── validate.yml
├── docs/
│   ├── diagrams/architecture.svg
│   ├── architecture.md
│   ├── azure-services.md
│   ├── learning-notes.md
│   ├── security.md
│   └── AUDIT_HANDOFF.md
├── evidence/
│   ├── 01-app-local.png
│   ├── 02-health-endpoint.png
│   ├── 03-info-endpoint.png
│   ├── 04-docker-running.png
│   ├── 05-docker-health.png
│   ├── 06-pytest-success.png
│   ├── 07-github-actions-success.png
│   ├── 08-kubernetes-pods.png
│   ├── 09-kubernetes-health.png
│   └── README.md
├── infra/
│   ├── azure/README.md
│   ├── docker/Dockerfile
│   └── kubernetes/
│       ├── deployment.yaml
│       └── service.yaml
├── src/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── tests/
│   └── test_app.py
├── requirements-dev.txt
├── .env.example
├── .gitignore
├── .markdownlint-cli2.jsonc
├── LICENSE
└── README.md
```

## Executar localmente

### Pré-requisitos

- Python 3.12 recomendado;
- Docker Desktop;
- `kubectl`;
- Kubernetes local habilitado no Docker Desktop com **kind** e **containerd image store** para reproduzir a validação realizada neste laboratório.

### Python

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .\.venv\Scripts\Activate.ps1

pip install -r requirements-dev.txt
pytest -q
python src/app.py
```

A aplicação ficará disponível em `http://localhost:8000`.

### Docker

```bash
docker build -f infra/docker/Dockerfile -t azure-app-platform-lab .
docker run --rm -p 8000:8000 --name azure-app-platform-lab azure-app-platform-lab
```

Em outro terminal:

```bash
curl http://localhost:8000/health
```

Resposta esperada:

```json
{
  "service": "azure-app-platform-lab",
  "status": "healthy",
  "version": "1.0.0"
}
```

### Kubernetes local — validado

A execução real foi validada em **Docker Desktop + kind**, cluster de **1 nó**, Kubernetes **v1.36.1**.

```bash
kubectl apply -f infra/kubernetes/deployment.yaml
kubectl apply -f infra/kubernetes/service.yaml
kubectl rollout status deployment/azure-app-platform-lab
kubectl get pods -l app=azure-app-platform-lab
kubectl port-forward svc/azure-app-platform-lab-svc 8080:80
```

Em outro terminal:

```powershell
Invoke-RestMethod http://localhost:8080/health
```

Resultado observado:

```text
service                status  version
azure-app-platform-lab healthy 1.0.0
```

O `Deployment` foi validado com **2 réplicas simultaneamente em estado `1/1 Running`**. As evidências estão em [`evidence/08-kubernetes-pods.png`](evidence/08-kubernetes-pods.png) e [`evidence/09-kubernetes-health.png`](evidence/09-kubernetes-health.png).

> Esta validação comprova execução Kubernetes local. Ela **não representa deploy em AKS**. Para AKS, a imagem deve ser publicada em um registry autorizado, como Azure Container Registry, e a infraestrutura Azure deve ser provisionada separadamente.

## Integração contínua

O workflow [`Validate Project`](.github/workflows/validate.yml) executa três verificações independentes:

1. **Python Tests** — instala as dependências e executa `pytest`;
2. **Markdown Lint** — valida a documentação sem mascarar falhas;
3. **Docker Smoke Test** — constrói a imagem, inicia o container e chama `/health`.

O workflow usa apenas permissão de leitura do conteúdo do repositório e não realiza deploy Azure.

## Microsoft Azure

Os serviços estudados estão documentados em [`docs/azure-services.md`](docs/azure-services.md):

| Serviço | Uso conceitual no laboratório |
|---|---|
| Azure App Service | Hospedagem PaaS de aplicações web/APIs |
| Azure Container Apps | Hospedagem gerenciada de containers |
| Azure Kubernetes Service (AKS) | Kubernetes gerenciado para cenários que realmente exigem orquestração |
| Application Insights | Telemetria de aplicações |
| Log Analytics | Centralização e consulta de logs |

Uma futura demonstração cloud deve priorizar **um único deploy real**, preferencialmente Azure Container Apps, em vez de provisionar vários serviços apenas para aumentar a lista de tecnologias. Consulte [`infra/azure/README.md`](infra/azure/README.md).

## Observabilidade

Métricas, logs e traces estão entre os sinais mais utilizados em estratégias modernas de observabilidade. Neste laboratório, Application Insights e Log Analytics são estudados como componentes da plataforma Azure; nenhuma coleta real é declarada enquanto não houver recurso provisionado e evidência correspondente.

## Segurança

O projeto aplica controles proporcionais ao escopo educacional:

- nenhuma credencial deve ser versionada;
- `.env` é ignorado e `.env.example` contém apenas placeholders;
- Docker executa a aplicação como usuário não-root;
- Kubernetes exige non-root e define `runAsUser: 1000` / `runAsGroup: 1000`, usa `RuntimeDefault` seccomp, bloqueia privilege escalation e remove Linux capabilities;
- CI possui somente `contents: read`;
- secrets Azure não são necessários para a validação atual.

Detalhes em [`docs/security.md`](docs/security.md).

## Evidências

O projeto distingue evidência automática de evidência manual.

**Comprovação automática:** GitHub Actions executa testes Python, lint e smoke test Docker.

**Comprovação manual concluída:** aplicação local, `/health`, `/info`, container Docker, health check do container, pytest local, tela do workflow e execução Kubernetes local foram registrados em screenshots reais na pasta [`evidence/`](evidence/).

A validação Kubernetes demonstra:

- cluster local Docker Desktop + kind operacional;
- node de control plane em estado `Ready`;
- `Deployment` com 2 réplicas;
- dois pods `1/1 Running`;
- liveness/readiness probes configuradas em `/health`;
- Service aplicado;
- `/health` respondendo `healthy` via `kubectl port-forward`.

O checklist detalhado está em [`evidence/README.md`](evidence/README.md).

Nenhum recurso Azure é declarado como provisionado sem evidência real.

## Aprendizados principais

- App Service, Container Apps e AKS resolvem problemas diferentes; Kubernetes não deve ser escolhido apenas por ser mais complexo.
- Testes e health checks tornam uma demonstração cloud mais verificável.
- Docker melhora portabilidade, mas uma imagem segura também precisa considerar usuário, dependências e superfície de ataque.
- `runAsNonRoot` pode exigir UID/GID numéricos explícitos para que o Kubernetes consiga validar o usuário da imagem.
- A validação com Kubernetes local permite testar Deployment, Service, probes e réplicas sem provisionar infraestrutura Azure.
- CI útil deve falhar quando uma validação obrigatória falha.
- Observabilidade deve ser planejada, mas não declarada como implementada sem telemetria real.
- Secrets pertencem a mecanismos próprios de configuração e identidade, não ao código-fonte.

Mais detalhes em [`docs/learning-notes.md`](docs/learning-notes.md).

## Leitura rápida para recrutadores

Em cerca de um minuto, os principais pontos do projeto podem ser avaliados nestes arquivos:

- **Aplicação:** [`src/app.py`](src/app.py)
- **Testes:** [`tests/test_app.py`](tests/test_app.py)
- **Container:** [`infra/docker/Dockerfile`](infra/docker/Dockerfile)
- **Kubernetes:** [`infra/kubernetes/deployment.yaml`](infra/kubernetes/deployment.yaml)
- **CI:** [`.github/workflows/validate.yml`](.github/workflows/validate.yml)
- **Arquitetura:** [`docs/architecture.md`](docs/architecture.md)
- **Segurança:** [`docs/security.md`](docs/security.md)
- **Evidências:** [`evidence/README.md`](evidence/README.md)

## Próximos passos opcionais

- [ ] realizar um deploy real no Azure Container Apps, caso exista conta/ambiente autorizado;
- [ ] registrar Application Insights/Log Analytics apenas se forem realmente configurados.

A execução local em Kubernetes, antes opcional, já foi concluída e documentada. Não há necessidade de adicionar Helm, ArgoCD, Terraform, Grafana, Kafka ou microserviços apenas para ampliar artificialmente o projeto.

## Referências

- [Microsoft Azure Documentation](https://learn.microsoft.com/azure/)
- [Azure App Service](https://learn.microsoft.com/azure/app-service/)
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
- [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/azure/aks/)
- [Application Insights](https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [The Twelve-Factor App](https://12factor.net/)
- [Digital Innovation One](https://www.dio.me/)
- [Repositório de referência da DIO](https://github.com/digitalinnovationone/Microsoft_Application_Platform)

## Autor

**Matheus Florindo** — [@matheusflorindo32](https://github.com/matheusflorindo32)

Projeto educacional autoral desenvolvido a partir do desafio **DIO Microsoft Application Platform**. Nenhum bloco substancial de código é apresentado como cópia do repositório de referência.

## Licença

Conteúdo autoral disponibilizado sob a [MIT License](LICENSE).
