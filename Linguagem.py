# Linguagem.py
from abc import ABC, abstractmethod

class Linguagem(ABC):
    def __init__(self):
        self.estados = ['q0', 'qf']
        self.transicoes = self.configurar_transicoes()
        self.alfabeto = self.configurar_alfabeto()
        self.estado_inicial = 'q0'
        self.estados_finais = ['qf']
    
    @abstractmethod
    def configurar_alfabeto(self):
        """Define o alfabeto da linguagem específica."""
        pass

    @abstractmethod
    def configurar_transicoes(self):
        """Define as transições da linguagem específica."""
        pass
