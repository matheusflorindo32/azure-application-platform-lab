# Evidências do Laboratório

Este diretório reúne apenas evidências reais e reproduzíveis da execução do projeto.

## Estado atual

- [x] GitHub Actions executado com sucesso no repositório
- [ ] Aplicação executada localmente pelo autor e registrada em screenshot
- [ ] Docker build/run registrado em screenshot pelo autor
- [ ] Kubernetes local executado e registrado, caso o autor deseje demonstrá-lo
- [ ] Deploy Azure real realizado
- [ ] Application Insights / Log Analytics demonstrados com evidência real

O workflow do GitHub Actions valida automaticamente testes Python, Markdown e um smoke test Docker com chamada ao endpoint `/health`. Screenshots manuais ainda não foram fabricados nem marcados como concluídos.

## Organização recomendada

```text
evidence/
├── README.md
├── local/
├── docker/
├── ci/
└── azure/
```

O Git não mantém diretórios vazios; crie as subpastas quando houver uma evidência real para adicionar.

## Evidências mínimas para a entrega DIO

Para complementar a documentação exigida pelo desafio, priorize quatro capturas simples:

1. aplicação local respondendo;
2. endpoint `/health`;
3. container Docker em execução;
4. GitHub Actions com os jobs aprovados.

Sugestão de nomes:

- `local/01-app-local.png`
- `local/02-health-endpoint.png`
- `docker/03-docker-run.png`
- `ci/04-github-actions.png`

## Regra de integridade

Não adicione screenshots, URLs, métricas, recursos Azure ou resultados que não tenham sido realmente produzidos. Dados sensíveis devem ser ocultados antes de qualquer captura pública.
