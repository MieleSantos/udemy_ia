
# udemy_ia

## Descrição
Este projeto consiste em uma API desenvolvida com **FastAPI**, **Poetry**, **streamlit**  e **Docker**, que explora funcionalidades da OpenAI. A API oferece cinco principais rotas:

1. **Chat de texto**: Para interação com modelos de linguagem.
2. **Moderação**: Para análise e moderação de conteúdo.
3. **Geração de imagens**: Para criar imagens a partir de descrições textuais.
4. **Transcrição de áudio**: Para transcrever áudio para texto.
5. **Tradução de áudio**: Para tradução de áudio.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework para criação de aplicações web e APIs.
- **Poetry**: Gerenciador de dependências e empacotamento.
- **Docker**: Containeração para simplificar a distribuição e execução do projeto.
- **OpenAI API**: Para acesso às funcionalidades de IA.
- **Streamlit**: Biblioteca para criação de interfaces web.

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

3. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
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
     docker compose up --build -d
     ```

6. Acesse a url http://localhost:5601 para acessar a interface do streamlit.

## Estrutura do Projeto

```
├── app/
│   ├── api/
│   │   ├── routers.py    
│   │   └── v1/
│   │       ├── audio_router.py        # Rota para áudio
│   │       ├── text_router.py         # Rota para chat de texto
│   │       ├── vision_router.py       # Rota para geração de imagem   
│   ├── services/
│   │   └── openai_service.py          # Serviços da OpenAI
├── front/
│   ├── main.py
│   └── page/
        ├── controller/
│       │   ├── controller.py
│       ├── audio_page.py
│       ├── image_page.py
│       ├── moderation_page.py
│       ├── text_page.py
│       ├── transcricao_page.py
│       └── translations_page.py
├── Dockerfile
├── pyproject.toml
└── README.md
```



# Video de demonstração do projeto
[![Watch the video](https://youtu.be/lnaHsoK3sVA)](https://youtu.be/lnaHsoK3sVA)


## Licença

Este projeto está licenciado sob a MIT License.


