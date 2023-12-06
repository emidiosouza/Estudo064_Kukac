# Estudo 064 Kukac: Assistente de resumos de reuniões

## Descrição
Este repositório contémreferências de códigod para a criação de uma assistente de resumos de reuniões. Se tratam de indicações para um projeto abrangente que aborda a autenticação com a API do Google Drive, monitoramento de pastas, download de vídeos, extração de áudio, transcrição com o modelo Whisper, análise da transcrição com GPT-3.3 e criação de documentos no Google Docs.

## Partes do Código
1.  ([**Autenticação com Google Drive API**](#parte-1-autenticação-com-google-drive-api))
2. **Monitoramento da Pasta do Google Drive** ([Link para Código](#parte-2-monitoramento-da-pasta-do-google-drive))
3. **Download do Vídeo e Extração de Áudio** ([Link para Código](#parte-3-download-do-vídeo-e-extração-de-áudio))
4. **Transcrição de Áudio com Whisper e Análise com GPT-3.3** ([Link para Código](#parte-4-transcrição-de-áudio-com-whisper-e-análise-com-gpt-33))
5. **Criação e Upload do Documento Google Docs e Exclusão do Vídeo** ([Link para Código](#parte-6-criação-e-upload-do-documento-google-docs-e-exclusão-do-vídeo))
6. **Script Principal de Orquestração** ([Link para Código](#parte-8-script-principal-de-orquestração))

   ## Avisos Importantes
- **Segurança das Credenciais:** Certifique-se de seguir as melhores práticas de segurança para proteger suas credenciais e informações sensíveis.
- **credentials.json:** Baixe este arquivo do Google Cloud Console e armazene-o em um local seguro. Adicione ao .gitignore para evitar inclusão em repositórios Git.
- **Variáveis de Ambiente:** Considere armazenar as credenciais como variáveis de ambiente para maior segurança.
- **Gerenciadores de Segredos:** Em ambientes de nuvem, use gerenciadores de segredos como AWS Secrets Manager, Google Secret Manager ou Azure Key Vault.
- **Token token.pickle:** Proteja o arquivo token.pickle e nunca o compartilhe publicamente. Adicione ao .gitignore.



Esperamos que este projeto sirva como um guia útil. Se precisar de assistência adicional ou esclarecimentos, sinta-se à vontade para entrar em contato.
