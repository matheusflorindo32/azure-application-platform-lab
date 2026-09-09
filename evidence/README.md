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
- [ ] Kubernetes local executado e registrado (opcional)
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

## Evidências mínimas da entrega DIO

As evidências principais da entrega estão concluídas:

1. aplicação local respondendo;
2. endpoint `/health`;
3. container Docker em execução;
4. testes automatizados;
5. GitHub Actions com os jobs aprovados.

## Itens opcionais

Kubernetes local, deploy real no Azure e observabilidade com Application Insights / Log Analytics permanecem opcionais e não são declarados como executados enquanto não houver evidência real.

## Regra de integridade

Não são adicionados screenshots, URLs, métricas, recursos Azure ou resultados que não tenham sido realmente produzidos. Dados sensíveis devem ser ocultados antes de qualquer captura pública.
