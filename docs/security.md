# Segurança

Diretrizes de segurança aplicadas neste projeto.

---

## Princípios

1. **Nenhuma credencial deve ser versionada.**
   - Arquivos `.env` estão no `.gitignore`.
   - Apenas `.env.example` com placeholders é commitado.

2. **Variáveis de ambiente para configuração.**
   - Toda configuração sensível (connection strings, API keys, instrumentation keys)
     é passada via variáveis de ambiente.
   - Em ambientes de desenvolvimento: arquivo `.env` local.
   - Em CI/CD: GitHub Secrets.
   - Em produção Azure: Azure Key Vault (recomendado como evolução).

3. **Princípio do menor privilégio.**
   - Containers rodam como usuário não-root quando possível.
   - Tokens de acesso têm escopo mínimo necessário.
   - Service accounts Kubernetes utilizam RBAC restritivo.

4. **Revisão antes de cada commit.**
   - Executar `git diff` antes de `git commit`.
   - Verificar se nenhum arquivo sensível foi incluído acidentalmente.
   - Utilizar ferramentas como `git-secrets` ou `trufflehog` para auditoria automatizada.

## Arquivos Bloqueados pelo .gitignore

- `.env`, `.env.local`, `.env.*.local`
- `*.pem`, `*.key`
- `credentials.json`, `secrets.yaml`
- `*.publishsettings`
- `*.tfvars`, `*.tfstate`

## Evolução Recomendada

| Nível | Prática | Status |
|---|---|---|
| Básico | `.gitignore` protege arquivos sensíveis | ✅ Implementado |
| Básico | `.env.example` com placeholders | ✅ Implementado |
| Intermediário | GitHub Secrets para CI/CD | 📋 Próximo passo |
| Avançado | Azure Key Vault para secrets em runtime | 📋 Evolução futura |
| Avançado | Managed Identity para autenticação sem secrets | 📋 Evolução futura |
| Avançado | Container scanning (Trivy, Snyk) | 📋 Evolução futura |

## Auditoria do Repositório de Referência

Antes de reutilizar qualquer conteúdo do repositório original da DIO
(`digitalinnovationone/Microsoft_Application_Platform`), foi realizada uma
verificação preliminar:

- **Nenhuma credencial, token ou secret** foi encontrado no repositório de referência.
- Nenhum bloco substancial de código foi copiado — o conteúdo deste projeto é autoral.
- A licença do projeto de referência foi respeitada.
