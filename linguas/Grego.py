from Linguagem import Linguagem

class Grego(Linguagem):
    def configurar_alfabeto(self):
        # Inclui letras gregas maiúsculas, minúsculas e acentuadas
        return list("αβγδεζηθικλμνξοπρστυφχψωάέήίόύώϊϋΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΌΎΏΪΫ")
