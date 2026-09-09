# Notas de Aprendizado

Registro dos principais aprendizados obtidos durante o estudo da
Microsoft Application Platform na formação DIO.

---

## Azure App Service vs. Azure Container Apps

| Aspecto | App Service | Container Apps |
|---|---|---|
| Modelo | PaaS tradicional | Serverless para containers |
| Scaling | Vertical e horizontal (manual/auto) | Horizontal automático (KEDA) |
| Containers | Suporte, mas não é o foco principal | Nativo para containers |
| Complexidade | Baixa — deploy direto de código | Média — requer imagem Docker |
| Custo em idle | Paga pelo plano ativo | Pode escalar a zero |
| Melhor para | Apps web tradicionais, APIs simples | Microserviços, event-driven |

**Conclusão:** App Service é a escolha mais direta quando se precisa de PaaS simples.
Container Apps é preferível quando a aplicação já é containerizada e precisa de
auto-scaling baseado em eventos.

## Quando Utilizar AKS

Azure Kubernetes Service é indicado quando:

- A aplicação possui múltiplos microserviços com necessidades distintas de scaling.
- É necessário controle granular sobre networking, storage e scheduling.
- A equipe já possui experiência com Kubernetes.
- O cenário exige personalização que PaaS não oferece (operators, CRDs, service mesh).

**Trade-off:** AKS oferece máximo controle, mas também máxima responsabilidade
operacional. Para laboratórios e aplicações simples, App Service ou Container Apps
são mais eficientes.

## Vantagens da Containerização

- **Portabilidade:** "funciona na minha máquina" → funciona em qualquer lugar.
- **Reprodutibilidade:** o ambiente é declarado no Dockerfile e versionado.
- **Isolamento:** dependências não conflitam entre aplicações.
- **CI/CD:** imagens Docker são artefatos imutáveis e auditáveis.
- **Densidade:** múltiplos containers compartilham o mesmo host com overhead menor que VMs.

## Importância da Observabilidade

- **Application Insights** coleta métricas de performance, traces distribuídos e exceções automaticamente.
- **Log Analytics** centraliza logs de todos os recursos Azure em um workspace unificado.
- Sem observabilidade, problemas em produção são diagnosticados por tentativa e erro.
- A combinação de métricas + logs + traces forma os três pilares da observabilidade moderna.

## CI/CD — Integração e Entrega Contínua

- GitHub Actions permite automatizar validação, build e deploy.
- Pipelines devem ser incrementais: primeiro lint/testes, depois build, depois deploy.
- **Nunca armazene secrets no código** — use GitHub Secrets ou Azure Key Vault.
- Pipelines fictícios de deploy (que não executam realmente) não devem ser criados
  apenas para aparência.

## Segurança de Secrets

- Credenciais jamais devem ser commitadas no repositório.
- Utilizar variáveis de ambiente (`.env`) localmente e GitHub Secrets / Azure Key Vault
  em ambientes remotos.
- `.gitignore` deve bloquear arquivos `.env`, `*.pem`, `*.key`.
- Revisar o `git diff` antes de cada commit para garantir que nenhum dado sensível
  foi incluído acidentalmente.

## Cloud-Native

- Aplicações cloud-native são projetadas para rodar em ambientes distribuídos.
- Os 12 Factors (Twelve-Factor App) são uma referência útil para design cloud-native.
- Containerização, configuração por variáveis de ambiente e statelessness são
  princípios centrais.
