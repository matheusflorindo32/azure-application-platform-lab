# Azure — Etapa opcional

Este diretório documenta a evolução opcional do laboratório para um deploy real na Microsoft Azure.

## Escopo recomendado

A opção preferencial para uma futura evidência prática é **Azure Container Apps**, porque mantém o foco em containers sem introduzir a complexidade operacional de um cluster AKS apenas para fins de demonstração.

Fluxo sugerido:

1. publicar a imagem em um registry autorizado;
2. criar o Azure Container App;
3. configurar as variáveis de ambiente necessárias;
4. validar `/health` na URL pública;
5. habilitar observabilidade somente se fizer sentido para a conta utilizada;
6. registrar prints reais em `evidence/azure/`.

## Estado atual

Nenhum recurso Azure é declarado como provisionado neste repositório. A documentação de App Service, Container Apps, AKS, Application Insights e Log Analytics representa estudo arquitetural enquanto não houver evidência real de execução.

Não versione subscriptions, tokens, connection strings, client secrets ou qualquer outra credencial.
