import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from LinguagemFactory import LinguagemFactory
from Familias import Familia
import time

def verificar_familia():
    botao_verificar.config(state="disabled", text="Carregando...")
    root.update_idletasks()

    palavra = entrada.get().strip()
    familias = [
        Familia.LATINO, Familia.CIRILICO, Familia.ARABE, Familia.GREGO,
        Familia.CJK, Familia.ASSEMBLY, Familia.JAVA, Familia.JAVASCRIPT, Familia.PYTHON
    ]
    familias_detectadas = set()

    for familia in familias:
        linguagem = LinguagemFactory.get_linguagem(familia)
        if linguagem.processar_palavra(palavra):
            familias_detectadas.add(familia.value)

    if len(familias_detectadas) > 1:
        resultado_texto.set(f"Erro: A palavra '{palavra}' contém caracteres de mais de uma família: {', '.join(familias_detectadas)}.")
    elif familias_detectadas:
        familia_detectada = familias_detectadas.pop()
        resultado_texto.set(f"A palavra '{palavra}' foi identificada como pertencente à família de escrita: {familia_detectada}.")
    else:
        resultado_texto.set(f"A palavra '{palavra}' não foi reconhecida por nenhuma família de escrita.")

    botao_verificar.config(state="normal", text="Verificar Família")

root = ttk.Window(themename="flatly")
root.title("Identificador de Família de Escrita")
root.geometry("800x600")
root.configure(bg="#F7F7F7")

titulo = ttk.Label(root, text="Identificador de Família de Escrita", font=("Poppins", 20, "bold"), bootstyle="dark")
titulo.pack(pady=20)

entrada_label = ttk.Label(root, text="Digite uma palavra:", font=("Poppins", 14), background="#F7F7F7", foreground="black")
entrada_label.pack(pady=10)
entrada = ttk.Entry(root, font=("Poppins", 14), width=30)
entrada.pack(pady=10)

botao_verificar = ttk.Button(root, text="Verificar Família", command=verificar_familia, bootstyle="primary", width=20)
botao_verificar.pack(pady=20)

resultado_texto = ttk.StringVar()
resultado_label = ttk.Label(root, textvariable=resultado_texto, font=("Poppins", 14), background="#F7F7F7", foreground="black")
resultado_label.pack(pady=30)

root.mainloop()

