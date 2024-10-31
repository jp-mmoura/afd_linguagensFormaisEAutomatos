from Linguagem import Linguagem

class Grego(Linguagem):
    def configurar_alfabeto(self):
        # Inclui letras gregas maiúsculas e minúsculas
        return [chr(i) for i in range(0x0370, 0x03FF + 1)]
