from Linguagem import Linguagem

class Latino(Linguagem):
    def configurar_alfabeto(self):
        # Inclui letras latinas maiúsculas, minúsculas e acentuadas
        basico = [chr(i) for i in range(0x0041, 0x005A + 1)]  # Maiúsculas A-Z
        minusculas = [chr(i) for i in range(0x0061, 0x007A + 1)]  # Minúsculas a-z
        acentuados = [chr(i) for i in range(0x00C0, 0x00FF + 1)]  # Acentuados À-ÿ
        return basico + minusculas + acentuados
