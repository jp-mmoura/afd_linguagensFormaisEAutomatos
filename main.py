from LinguagemFactory import LinguagemFactory
from Familias import Familia

def identificar_familia(palavra):
    familias = [
        Familia.GREGO, Familia.CIRILICO, Familia.ARABE, Familia.CJK,
        Familia.LATINO, Familia.ASSEMBLY, Familia.JAVA, Familia.JAVASCRIPT, Familia.PYTHON
    ]
    familias_detectadas = set()

    # Testa a palavra em cada família de escrita usando o autômato
    for familia in familias:
        linguagem = LinguagemFactory.get_linguagem(familia)
        if linguagem.processar_palavra(palavra):
            familias_detectadas.add(familia.value)

    # Verifica se mais de uma família foi detectada
    if len(familias_detectadas) > 1:
        print(f"Erro: A palavra '{palavra}' contém caracteres de mais de uma família de escrita: {', '.join(familias_detectadas)}.")
    elif familias_detectadas:
        familia_detectada = familias_detectadas.pop()
        print(f"A palavra '{palavra}' foi identificada como pertencente à família de escrita: {familia_detectada}.")
    else:
        print(f"A palavra '{palavra}' não foi reconhecida por nenhuma família de escrita.")

# Teste com uma entrada
palavra = input("Digite uma palavra para identificar a família de escrita: ")
identificar_familia(palavra)

