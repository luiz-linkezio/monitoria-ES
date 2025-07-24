# monitoria-ES

Este repositório serve como exemplo **mínimo** para demonstrar CI/CD na prática.

## Estrutura do Projeto

- `app.py`: Script Python que imprime "Hello, CI/CD!".
- `test_app.py`: Teste automatizado para validar a saída do script.
- `requirements.txt`: Dependências do projeto.
- `.github/workflows/ci.yml`: Pipeline de CI usando GitHub Actions.

## Como rodar localmente

1. Instale o Python 3.11+.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script:
   ```bash
   python app.py
   ```

## Como rodar os testes

```bash
pytest
```

## CI/CD

A cada push ou pull request para o branch `main`, o GitHub Actions executa automaticamente os testes definidos em `test_app.py`. O status do pipeline aparece na aba "Actions" do GitHub.

**CD Simulado:**
Após os testes passarem, o pipeline executa um passo de "deploy" que cria um arquivo chamado `deployed.txt` com a mensagem "Deploy realizado com sucesso!". Isso simula o processo de deploy automático, mostrando o conceito de CD na prática.

Assim, é possível mostrar na prática como mudanças no código disparam o pipeline de CI/CD, validando e "implantando" automaticamente o projeto.