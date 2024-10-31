import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from LinguagemFactory import LinguagemFactory
from Familias import Familia
import time

# Função para verificar a família de escrita com indicador de carregamento
def verificar_familia():
    # Ativa o spinner de carregamento e desativa o botão
    botao_verificar.config(state="disabled", text="Carregando...")
    root.update_idletasks()  # Atualiza a interface

    # Processamento da verificação da palavra
    palavra = entrada.get().strip()
    familias = [Familia.LATINO, Familia.CIRILICO, Familia.ARABE, Familia.GREGO, Familia.CJK]
    familias_detectadas = set()

    # Testa a palavra em cada família de escrita usando o autômato
    for familia in familias:
        linguagem = LinguagemFactory.get_linguagem(familia)
        if linguagem.processar_palavra(palavra):
            familias_detectadas.add(familia.value)

    # Verifica se mais de uma família foi detectada e exibe o resultado
    if len(familias_detectadas) > 1:
        resultado_texto.set(f"Erro: A palavra '{palavra}' contém caracteres de mais de uma família: {', '.join(familias_detectadas)}.")
    elif familias_detectadas:
        familia_detectada = familias_detectadas.pop()
        resultado_texto.set(f"A palavra '{palavra}' foi identificada como pertencente à família de escrita: {familia_detectada}.")
    else:
        resultado_texto.set(f"A palavra '{palavra}' não foi reconhecida por nenhuma família de escrita.")

    # Restaura o estado original do botão após o carregamento
    botao_verificar.config(state="normal", text="Verificar Família")

# Configuração da interface gráfica
root = ttk.Window(themename="flatly")  # Tema claro para visual moderno
root.title("Identificador de Família de Escrita")
root.geometry("800x600")
root.configure(bg="#F7F7F7")  # Fundo cinza claro

# Título
titulo = ttk.Label(root, text="Identificador de Família de Escrita", font=("Poppins", 20, "bold"), bootstyle="dark")
titulo.pack(pady=20)

# Entrada de Texto
entrada_label = ttk.Label(root, text="Digite uma palavra:", font=("Poppins", 14), background="#F7F7F7", foreground="black")
entrada_label.pack(pady=10)
entrada = ttk.Entry(root, font=("Poppins", 14), width=30)
entrada.pack(pady=10)

# Botão para Verificar
botao_verificar = ttk.Button(root, text="Verificar Família", command=verificar_familia, bootstyle="primary", width=20)
botao_verificar.pack(pady=20)

# Área de Resultado
resultado_texto = ttk.StringVar()
resultado_label = ttk.Label(root, textvariable=resultado_texto, font=("Poppins", 14), background="#F7F7F7", foreground="black")
resultado_label.pack(pady=30)

root.mainloop()
