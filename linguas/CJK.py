from Linguagem import Linguagem

class CJK(Linguagem):
    def configurar_alfabeto(self):
        # Inclui Hiragana, Katakana, Kanji e Hangul
        hiragana = [chr(i) for i in range(0x3040, 0x309F + 1)]
        katakana = [chr(i) for i in range(0x30A0, 0x30FF + 1)]
        kanji = [chr(i) for i in range(0x4E00, 0x9FFF + 1)]
        hangul = [chr(i) for i in range(0xAC00, 0xD7A3 + 1)]
        return hiragana + katakana + kanji + hangul
