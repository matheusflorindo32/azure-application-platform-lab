# Audit Handoff

Este documento resume o estado técnico do laboratório para revisão independente.

## Escopo final

- API educacional Flask com endpoints `/`, `/health` e `/info`;
- testes automatizados com pytest;
- Docker com Gunicorn, usuário não-root e health check;
- Kubernetes Deployment + Service, probes, requests/limits e hardening básico;
- GitHub Actions para testes, Markdown lint e smoke test Docker;
- arquitetura Mermaid + SVG;
- documentação de Azure, segurança, aprendizados e evidências;
- Azure real mantido como evolução opcional até existir execução comprovada.

## Validação automatizada

O workflow `.github/workflows/validate.yml` deve bloquear falhas em três frentes:

1. testes Python;
2. lint de Markdown;
3. build e smoke test Docker com chamada ao `/health`.

O workflow não possui deploy Azure nem requer secrets cloud.

## Segurança

- `.env` não deve ser versionado;
- `.env.example` contém somente placeholders;
- container Docker executa como usuário não-root;
- workload Kubernetes exige non-root, seccomp `RuntimeDefault`, bloqueia privilege escalation e remove capabilities;
- workflow possui apenas `contents: read`;
- nenhuma credencial Azure é necessária no estado atual.

## Limites declarados

- nenhum recurso Azure é declarado como provisionado;
- Application Insights e Log Analytics são conceituais até existir telemetria real;
- screenshots locais/Docker ainda dependem do autor;
- manifests Kubernetes são didáticos e exigem imagem disponível no cluster escolhido.

## Evidências

A evidência automática é o próprio GitHub Actions. Evidências manuais devem ser adicionadas somente quando produzidas de verdade, conforme `evidence/README.md`.

## Evolução opcional recomendada

Se houver ambiente Azure autorizado, a próxima evolução de maior valor é um único deploy em Azure Container Apps, seguido de validação pública de `/health`. AKS, Helm, ArgoCD, Terraform ou ferramentas adicionais não são necessários para cumprir o desafio nem para demonstrar os conceitos centrais deste laboratório.

## Critério de auditoria

Uma revisão futura deve conferir:

- resultado do workflow mais recente;
- testes efetivamente executados;
- renderização do README e SVG;
- ausência de secrets;
- consistência entre claims do README e evidências;
- screenshots manuais antes da entrega final à DIO, caso exigidos na avaliação.
