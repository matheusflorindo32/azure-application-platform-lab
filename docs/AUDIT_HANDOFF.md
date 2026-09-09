# Audit Handoff — Documento para Segunda Auditoria

Este documento resume o escopo, decisões e limitações do projeto para
facilitar uma auditoria independente.

---

## Escopo Criado

- Repositório público no GitHub como entrega do desafio DIO Microsoft Application Platform.
- Documentação profissional: README, arquitetura, learning notes, serviços Azure, segurança.
- Aplicação mínima educacional em Python Flask.
- Infraestrutura como código: Dockerfile, Kubernetes manifests (deployment + service).
- Checklist de evidências para preenchimento posterior pelo autor.
- Workflow de CI para validação básica (lint de Markdown, build Docker).

## Decisões Tomadas

| Decisão | Justificativa |
|---|---|
| Python Flask como aplicação | Leve, minimalista, sem dependências complexas — ideal para fins didáticos |
| Nenhum deploy Azure executado | Evitar fabricar evidências; etapas Azure ficam como "pendente de execução" |
| MIT License para conteúdo autoral | Licença permissiva e compatível com portfólio |
| Separação `src/` vs `infra/` vs `docs/` | Organização profissional de monorepo |
| Badges apenas verdadeiros | Nenhum badge de build/deploy sem pipeline real |
| Commits semânticos organizados | Profissionalismo e rastreabilidade |

## Arquivos Principais

- `README.md` — Documentação principal premium
- `src/app.py` — Aplicação Flask de exemplo
- `infra/docker/Dockerfile` — Containerização da aplicação
- `infra/kubernetes/deployment.yaml` — Manifest de Deployment
- `infra/kubernetes/service.yaml` — Manifest de Service
- `docs/architecture.md` — Arquitetura conceitual com Mermaid
- `docs/learning-notes.md` — Aprendizados do laboratório
- `docs/azure-services.md` — Tabela de referência de serviços Azure
- `docs/security.md` — Diretrizes de segurança
- `evidence/README.md` — Checklist de evidências
- `.github/workflows/validate.yml` — CI de validação

## Limitações

- **Nenhum recurso Azure foi provisionado.** Toda referência a serviços Azure é conceitual.
- **Nenhum deploy foi executado.** Etapas de deploy dependem de execução manual.
- **Evidências (screenshots) estão pendentes.** O checklist em `evidence/README.md` está vazio.
- **CI não inclui deploy Azure** — apenas validação local (lint + Docker build).

## Itens Pendentes de Ação do Autor

- [ ] Executar aplicação localmente e capturar screenshot
- [ ] Realizar Docker build e Docker run
- [ ] Provisionar recursos Azure (se desejado)
- [ ] Executar deploy em Azure App Service ou Container Apps
- [ ] Configurar Application Insights e capturar métricas
- [ ] Consultar Log Analytics e capturar resultado
- [ ] Preencher checklist de evidências com screenshots reais
- [ ] Adicionar topics ao repositório GitHub (manual via Settings)

## Pontos para Revisão

- Verificar se o Mermaid renderiza corretamente no GitHub.
- Confirmar que nenhuma credencial ou dado pessoal foi versionado.
- Validar links no README (referência DIO, perfil do autor).
- Revisar ortografia e consistência da documentação.

## Possíveis Melhorias

- Adicionar testes unitários à aplicação Flask.
- Implementar multi-stage Docker build.
- Criar template de IaC (Bicep ou Terraform) para provisionamento Azure.
- Adicionar Helm chart como alternativa aos manifests Kubernetes.
- Implementar health checks avançados no Kubernetes.
- Adicionar container scanning (Trivy) no CI.
