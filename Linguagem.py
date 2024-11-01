from abc import ABC, abstractmethod

class Linguagem(ABC):
    def __init__(self):
        self.estados = ['q0', 'qf']  # Estado inicial e estado final
        self.estado_inicial = 'q0'
        self.estados_finais = ['qf']
        self.alfabeto = self.configurar_alfabeto()
        self.transicoes = self.configurar_transicoes()

        # Exibir alfabeto e transições para depuração
        print(f"Alfabeto configurado para {self.__class__.__name__}: {self.alfabeto}")
        print(f"Transições configuradas para {self.__class__.__name__}: {self.transicoes}")

    @abstractmethod
    def configurar_alfabeto(self):
        """Define o alfabeto específico da linguagem."""
        pass

    def configurar_transicoes(self):
        """Define as transições para cada símbolo no alfabeto, permitindo transições de qualquer estado."""
        transicoes = {}
        for simbolo in self.alfabeto:
            # Transições de todos os estados para 'qf' com qualquer símbolo do alfabeto
            for estado in self.estados:
                transicoes[(estado, simbolo)] = 'qf'
                transicoes[(estado, simbolo.lower())] = 'qf'
                transicoes[(estado, simbolo.upper())] = 'qf'
        return transicoes

    def processar_palavra(self, palavra):
        """Processa a palavra pelo autômato, verificando se ela é aceita."""
        estado_atual = self.estado_inicial
        for simbolo in palavra:
            # Verifica se o símbolo está nas transições diretamente
            print(f"Processando símbolo: '{simbolo}' no estado: {estado_atual}")
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
                print(f"Transição encontrada para '{simbolo}', novo estado: {estado_atual}")
            else:
                print(f"Erro: símbolo '{simbolo}' não encontrado nas transições configuradas.")
                return False  # Transição não encontrada, palavra rejeitada
        # Verifica se o estado final é aceitável
        resultado = estado_atual in self.estados_finais
        print(f"Resultado final: {'Aceito' if resultado else 'Rejeitado'}")
        return resultado
