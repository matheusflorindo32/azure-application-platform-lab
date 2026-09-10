# Evidências do Laboratório

Este diretório reúne evidências reais e reproduzíveis da execução do projeto.

## Estado atual

- [x] Aplicação executada localmente e registrada em screenshot
- [x] Endpoint `/health` validado localmente
- [x] Endpoint `/info` validado localmente
- [x] Docker image build concluído com sucesso
- [x] Container Docker executado localmente com status `healthy`
- [x] Endpoint `/health` validado a partir do container
- [x] Testes automatizados executados localmente com pytest
- [x] GitHub Actions executado com sucesso no repositório
- [x] Kubernetes local executado com Docker Desktop + kind
- [x] Deployment Kubernetes validado com 2 réplicas `Running`
- [x] Endpoint `/health` validado através do Service Kubernetes via `port-forward`
- [ ] Deploy Azure real realizado (opcional)
- [ ] Application Insights / Log Analytics demonstrados com evidência real (opcional)

O workflow do GitHub Actions valida testes Python, Markdown e um smoke test Docker com chamada ao endpoint `/health`.

## Evidências disponíveis

| Arquivo | Evidência |
|---|---|
| `01-app-local.png` | Aplicação Flask respondendo em `localhost:8000` |
| `02-health-endpoint.png` | Endpoint `/health` retornando status saudável |
| `03-info-endpoint.png` | Endpoint `/info` exibindo metadados não sensíveis |
| `04-docker-running.png` | Container Docker em execução com status `healthy` |
| `05-docker-health.png` | Health check da aplicação executada via Docker |
| `06-pytest-success.png` | Execução local dos três testes automatizados com sucesso |
| `07-github-actions-success.png` | Pipeline `Validate Project` concluído com sucesso |
| `08-kubernetes-pods.png` | Kubernetes local com 2 réplicas da aplicação em estado `1/1 Running` |
| `09-kubernetes-health.png` | Endpoint `/health` respondendo através do Service Kubernetes via `port-forward` |

## Validação Kubernetes local

A camada de orquestração foi validada em ambiente local utilizando **Docker Desktop**, provisionador **kind**, cluster de **1 nó** e Kubernetes **v1.36.1**.

Fluxo efetivamente executado:

```text
Imagem Docker local
    ↓
Docker Desktop + containerd image store
    ↓
Kubernetes local (kind)
    ↓
Deployment com 2 réplicas
    ↓
Pods 1/1 Running
    ↓
Service Kubernetes
    ↓
kubectl port-forward 8080:80
    ↓
GET /health → healthy
```

Comandos principais utilizados na validação:

```bash
kubectl apply -f infra/kubernetes/deployment.yaml
kubectl apply -f infra/kubernetes/service.yaml
kubectl rollout status deployment/azure-app-platform-lab
kubectl get pods -l app=azure-app-platform-lab
kubectl port-forward svc/azure-app-platform-lab-svc 8080:80
```

A resposta do endpoint validado através do Kubernetes foi:

```text
service                status  version
azure-app-platform-lab healthy 1.0.0
```

Esta execução comprova os manifests e o comportamento da aplicação em Kubernetes local. **Não representa um deploy no Azure Kubernetes Service (AKS)** e nenhum recurso Azure foi provisionado para esta validação.

## Evidências mínimas da entrega DIO

As evidências principais da entrega estão concluídas:

1. aplicação local respondendo;
2. endpoints `/health` e `/info`;
3. container Docker em execução e saudável;
4. testes automatizados com pytest;
5. GitHub Actions com os jobs aprovados;
6. Kubernetes local com 2 réplicas em execução;
7. `/health` validado através do Service Kubernetes.

## Itens opcionais

Deploy real no Azure e observabilidade com Application Insights / Log Analytics permanecem opcionais e não são declarados como executados enquanto não houver evidência real.

## Regra de integridade

Não são adicionados screenshots, URLs, métricas, recursos Azure ou resultados que não tenham sido realmente produzidos. Dados sensíveis devem ser ocultados antes de qualquer captura pública.
