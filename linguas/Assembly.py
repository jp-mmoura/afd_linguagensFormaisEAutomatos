import re
from Linguagem import Linguagem

class Assembly(Linguagem):
    def configurar_alfabeto(self):
        return [
            r'\bMOV\b', r'\bADD\b', r'\bSUB\b', r'\bMUL\b', r'\bDIV\b', 
            r'\bJMP\b', r'\bCALL\b', r'\bRET\b', r'\bPUSH\b', r'\bPOP\b', 
            r'\bNOP\b', r'\bAND\b', r'\bOR\b', r'\bXOR\b', r'\bNOT\b', 
            r'\bCMP\b', r'\bJE\b', r'\bJNE\b', r'\bJG\b', r'\bJL\b', 
            r'\bJGE\b', r'\bJLE\b', r'\bDB\b', r'\bDW\b', r'\bDD\b', 
            r'\bDQ\b', r'\bDT\b', r'R[0-3]', r'AX\b', r'BX\b', 
            r'CX\b', r'DX\b', r'SP\b', r'BP\b', r'SI\b', r'DI\b', 
             r'\bmov\b', r'\badd\b', r'\bsub\b', r'\bmul\b', r'\bdiv\b', 
            r'\bjmp\b', r'\bcall\b', r'\bret\b', r'\bpush\b', r'\bpop\b', 
            r'\bnop\b', r'\band\b', r'\bor\b', r'\bxor\b', r'\bnot\b', 
            r'\bcmp\b', r'\bje\b', r'\bjne\b', r'\bjg\b', r'\bjl\b', 
            r'\bjge\b', r'\bjle\b', r'\bdb\b', r'\bdw\b', r'\bdd\b', 
            r'\bdq\b', r'\bdt\b', r'r[0-3]', r'ax\b', r'bx\b', 
            r'cx\b', r'dx\b', r'sp\b', r'bp\b', r'si\b', r'di\b',
            # Operadores e pontuação são comuns
        ]

    def processar_palavra(self, palavra):
        """Processa a palavra verificando se ela corresponde a algum padrão de Assembly."""
        for padrao in self.alfabeto:
            if re.search(padrao, palavra):
                print(f"'{palavra}' corresponde ao padrão de Assembly: {padrao}")
                return True
        return False
