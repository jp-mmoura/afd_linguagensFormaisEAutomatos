import re
from Linguagem import Linguagem

class JavaScript(Linguagem):
    def configurar_alfabeto(self):
        return [
            r'\bfunction\b',  # Definição de função
            r'\bvar\b',       # Declaração de variável com var
            r'\blet\b',       # Declaração de variável com let
            r'\bconst\b',     # Declaração de variável com const
            r'console\.log',  # Função console.log
            r'\bnew\b',       # Palavra-chave new
            # Operadores e pontuação são comuns
        ]

    def processar_palavra(self, palavra):
        """Processa a palavra verificando se ela corresponde a algum padrão de JavaScript."""
        for padrao in self.alfabeto:
            if re.search(padrao, palavra):
                print(f"'{palavra}' corresponde ao padrão de JavaScript: {padrao}")
                return True
        return False
