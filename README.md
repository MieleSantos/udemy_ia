# udemy_ia

## Descrição
Este projeto consiste em uma API desenvolvida com **FastAPI**, **Poetry** e **Docker**, que explora funcionalidades da OpenAI. A API oferece três principais rotas:

1. **Chat de texto**: Para interação com modelos de linguagem.
2. **Moderação**: Para análise e moderação de conteúdo.
3. **Geração de imagens**: Para criar imagens a partir de descrições textuais.
4. **Transcrição de audio**: Para transcrever audio para texto.
5. **Tradução de audio**: Para tradução audio.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework para criação de aplicações web e APIs.
- **Poetry**: Gerenciador de dependências e empacotamento.
- **Docker**: Containeração para simplificar a distribuição e execução do projeto.
- **OpenAI API**: Para acesso às funcionalidades de IA.

---

## Configuração do Ambiente

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Configure o Poetry**:
   Certifique-se de ter o Poetry instalado. Em seguida, instale as dependências:
   ```bash
   poetry install
   ```

3. **Configure o arquivo `.env`**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```env
   OPENAI_API_KEY=<sua_chave_da_openai>
   ```

4. **Execute a aplicação**:
   Com o Poetry:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

5. **Use o Docker (opcional)**:
   
   - Construa a imagem:
     ```bash
     docker build -t openai-api-project .
     ```
   - Execute o contêiner:
     ```bash
     docker run -p 8000:8000 --env-file .env openai-api-project
     ```

---

## Estrutura do Projeto

```
├── <NOME_DO_PROJETO>/
│   ├── api/
|   |   ├── routers.py    
│   │   └── v1/
│   │       ├── audio_router.py        # Rota para audio
│   │       ├── text_router.py        # Rota para chat de texto
│   │       ├── vision_router.py        # Rota para gera imagem   
│   ├── services/
│   │   └── openai_service.py # Serviços da OpenAI
│   └── Dockerfile              # Configuração do Docker
```

---

## Uso da API

A documentação interativa da API está disponível em:
```
http://127.0.0.1:8080/docs
```

### Exemplo de Requisições

#### 1. Chat de Texto
Endpoint: `POST api/v1/text/chat`

```json
{
  "message": "Olá, como você está?"
}
```

#### 2. Moderação
Endpoint: `POST api/v1/text/moderation`

```json
{
  "content": "Texto a ser moderado."
}
```

#### 3. Geração de Imagens
Endpoint: `POST  api/v1/image`

```json
{
  "description": "Um gato astronauta na lua."
}
```

---


---

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

