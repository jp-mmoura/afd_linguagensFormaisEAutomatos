# Portugues.py
from Linguagem import Linguagem

class Portugues(Linguagem):
    def configurar_alfabeto(self):
        return ['a', 'á', 'â', 'ã', 'b', 'c', 'ç', 'd', 'e', 'é', 'ê', 'f', 'g', 'h', 'i', 'í', 'j', 
                'k', 'l', 'm', 'n', 'o', 'ó', 'ô', 'õ', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z']
    
    def configurar_transicoes(self):
        return {(estado, simbolo): 'qf' for simbolo in self.configurar_alfabeto() for estado in ['q0', 'qf']}
