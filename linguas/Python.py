import re
from Linguagem import Linguagem

class Python(Linguagem):
    def configurar_alfabeto(self):
        return [
            r'\bdef\b',  # Definição de função
            # Operadores e pontuação são comuns
        ]


    def processar_palavra(self, palavra):
        """Processa a palavra verificando se ela corresponde a algum padrão de Python."""
        for padrao in self.alfabeto:
            if re.search(padrao, palavra):
                print(f"'{palavra}' corresponde ao padrão de Python: {padrao}")
                return True
        return False
