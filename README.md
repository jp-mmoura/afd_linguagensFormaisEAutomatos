# Identificador de Família de Escrita

Este projeto é um sistema para identificar a família de escrita de uma palavra, como latino, cirílico, árabe, grego e CJK. A aplicação possui uma interface gráfica e pode ser executada como um executável independente.

## Pré-requisitos

1. **Instalar Python**:
   - Acesse [a página oficial do Python](https://www.python.org/downloads/) e baixe a versão mais recente do Python.
   - **Durante a instalação, marque a opção "Add Python to PATH"** para facilitar a execução do Python no terminal.

2. **Clonar o repositório**:
   - Clone o repositório para sua máquina:
     ```bash
     git clone https://github.com/jp-mmoura/afd_linguagensFormaisEAutomatos.git
     ```
   - Entre na pasta do projeto:
     ```bash
     cd afd_linguagensFormaisEAutomatos
     ```

## Configuração do Ambiente

1. **Criar e Ativar o Ambiente Virtual**:
   - Para criar um ambiente virtual, execute:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - **macOS e Linux**:
       ```bash
       source venv/bin/activate
       ```

2. **Instalar Dependências**:
   - Instale as dependências necessárias com o comando:
     ```bash
     pip install -r requirements.txt
     ```

## Executando o Programa

1. **Execução direta (via Python)**:
   - Com o ambiente virtual ativado, execute a interface gráfica do projeto ou a versão de terminal:
   
     ```bash
     python identificador_gui.py
     ```
       ```bash
     python main.py
     ```

2. **Geração de Executável**:
   - Para criar um executável que funcione de forma independente do Python:
    
     - Gere o executável:
       ```bash
       pyinstaller --onefile --windowed identificador_gui.py
       ```
   - O executável será criado na pasta `dist` e poderá ser distribuído sem necessidade de instalar o Python.

## Instruções de Uso

1. Abra a interface gráfica do sistema.
2. Digite uma palavra na entrada e clique em "Verificar Família".
3. O sistema identificará a família de escrita e exibirá o resultado na tela. Em caso de erro, o sistema avisará se houver caracteres de mais de uma família na palavra.

## Estrutura do Projeto

- `identificador_gui.py`: Interface gráfica para o sistema.
- `main.py`: Módulo principal para rodar no terminal (opcional).
- `LinguagemFactory.py`: Fábrica que gerencia as diferentes famílias de escrita.
- `Familias`: Pasta que contém as classes para cada família de escrita (Latino, Cirílico, Árabe, Grego, CJK).

## Contribuições e Suporte

Sinta-se à vontade para enviar PRs com melhorias ou abrir uma issue caso tenha dúvidas ou problemas com o projeto.

---

Agora seus colegas terão todas as informações necessárias para configurar e rodar o sistema de identificação de escrita com facilidade!
