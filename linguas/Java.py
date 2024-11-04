import re
from Linguagem import Linguagem

class Java(Linguagem):
    def configurar_alfabeto(self):
        return [
            r'\bstatic\b',          # Modificador static
            r'\bString\b',          # Tipo de dados String
            r'\bboolean\b',         # Tipo de dados boolean
            r'System\.out\.println',  # Função System.out.println
            r'\btry\b',             # Bloco try
            r'\bcatch\b',           # Bloco catch
            r'\bthrows\b',          # Palavra-chave throws
            r'\bthrow\b',           # Palavra-chave throw
            # Operadores e pontuação são comuns
        ]

    def processar_palavra(self, palavra):
        """Processa a palavra verificando se ela corresponde a algum padrão de Java."""
        for padrao in self.alfabeto:
            if re.search(padrao, palavra):
                print(f"'{palavra}' corresponde ao padrão de Java: {padrao}")
                return True
        return False
