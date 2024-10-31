from Familias import Familia
from linguas.Latino import Latino
from linguas.Cirilico import Cirilico
from linguas.Arabe import Arabe
from linguas.Grego import Grego
from linguas.CJK import CJK

class LinguagemFactory:
    @staticmethod
    def get_linguagem(familia: Familia):
        if familia == Familia.LATINO:
            return Latino()
        elif familia == Familia.CIRILICO:
            return Cirilico()
        elif familia == Familia.ARABE:
            return Arabe()
        elif familia == Familia.GREGO:
            return Grego()
        elif familia == Familia.CJK:
            return CJK()
        else:
            raise ValueError("Família de idioma não suportada.")
