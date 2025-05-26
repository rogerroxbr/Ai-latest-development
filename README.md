# AI Latest Development

Este projeto utiliza a [CrewAI](https://docs.crewai.com/) para criar uma equipe de agentes inteligentes capazes de pesquisar e gerar relatórios detalhados sobre tópicos relacionados a Inteligência Artificial, com foco em LLMs (Large Language Models).

## Estrutura do Projeto

```
.
├── src/
│   ├── crew.py                # Configuração dos agentes, tarefas e equipe
│   ├── main.py                # Ponto de entrada para execução local
│   ├── config/
│   │   ├── agents.yaml        # Configuração dos agentes
│   │   └── tasks.yaml         # Configuração das tarefas
│   └── tools/
│       └── custom_tool.py     # Exemplo de ferramenta customizada
├── report.md                  # Exemplo de relatório gerado
├── requirements.txt           # Dependências do projeto
├── .env                       # Variáveis de ambiente
└── .gitignore
```

## Como Executar

1. **Pré-requisitos**  
   - Python 3.13+
   - Instale as dependências:
     ```sh
     pip install -r requirements.txt
     ```
     ou
     ```sh
     pip install crewai>=0.121.0
     ```

2. **Configuração**  
   - Ajuste as configurações dos agentes e tarefas em `src/config/agents.yaml` e `src/config/tasks.yaml` conforme necessário.
   - Configure variáveis de ambiente no arquivo `.env` se necessário.

3. **Execução**  
   Execute o projeto localmente:
   ```sh
   python src/main.py
   ```

   O relatório será gerado no arquivo `report.md`.

## Personalização

- **Adicionar Ferramentas Customizadas:**  
  Implemente novas ferramentas em `src/tools/custom_tool.py` e registre-as nos agentes em `src/crew.py`.
- **Configuração dos Agentes e Tarefas:**  
  Edite `src/config/agents.yaml` e `src/config/tasks.yaml` para personalizar papéis, objetivos e fluxos de trabalho.

## Referências

- [CrewAI Documentation](https://docs.crewai.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Ollama](https://ollama.com/)

---

> Projeto para pesquisa e geração de relatórios sobre os avanços mais recentes em LLMs e Inteligência Artificial.