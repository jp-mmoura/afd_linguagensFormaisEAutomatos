# Espanhol.py
from Linguagem import Linguagem

class Espanhol(Linguagem):
    def configurar_alfabeto(self):
        return ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 
                'n', 'ñ', 'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z']
    
    def configurar_transicoes(self):
        return {(estado, simbolo): 'qf' for simbolo in self.configurar_alfabeto() for estado in ['q0', 'qf']}
