import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def operacao(cargaH):
    cargaHemM = cargaH * 60  # Carga horária em minutos
    qtdAulas = cargaHemM / 50  # Quantidade de aulas
    vcpDaMat = cargaH * 0.25  # Limiar de decisão (25% da matéria)
    return vcpDaMat, qtdAulas

def calcular():
    try:
        materia = materia_entry.get()
        cargaH = int(cargaH_entry.get())
        faltas = int(faltas_entry.get())

        if cargaH <= 0 or faltas < 0:
            messagebox.showerror("Erro", "A carga horária deve ser positiva e as faltas não podem ser negativas.")
            return

        vcp, qtdAulas = operacao(cargaH)

        if faltas < vcp:
            podeFaltar = vcp - faltas
            resultado_text = (f"A matéria de {materia.lower()} tem {cargaH} horas e há {qtdAulas:.0f} aula(s).\n"
                            f"Você ainda pode faltar {podeFaltar:.0f} aula(s).")
            exibir_resultado(resultado_text, "ok.jpg")

        elif faltas == vcp:
            resultado_text = (f"A matéria de {materia.lower()} tem {cargaH} horas e há {qtdAulas:.0f} aulas.\n"
                            "Você não pode mais faltar.")
            exibir_resultado(resultado_text, "alert.jpg")

        else:  # faltas > vcp
            faltasAmais = faltas - vcp
            resultado_text = (f"A matéria de {materia.lower()} tem {cargaH} horas e há {qtdAulas:.0f} aulas.\n"
                            f"Você ultrapassou o limite de {vcp:.0f} falta(s) permitidas com {faltasAmais:.0f} falta(s) a mais.")
            exibir_resultado(resultado_text, "error.jpeg")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para carga horária e faltas.")

def exibir_resultado(texto, imagem_caminho):
    resultado_label.config(text=texto)
    imagem = Image.open(imagem_caminho)
    imagem = imagem.resize((300, 300))
    imagem_tk = ImageTk.PhotoImage(imagem)
    imagem_label.config(image=imagem_tk)
    imagem_label.image = imagem_tk

# Janela principal
root = tk.Tk()
root.title("Verificador de Faltas")
root.geometry("800x1000")

# Frame de entrada
tk.Label(root, text="Nome da Matéria:").pack(pady=5)
materia_entry = tk.Entry(root)
materia_entry.pack(pady=5)

tk.Label(root, text="Carga Horária:").pack(pady=5)
cargaH_entry = tk.Entry(root)
cargaH_entry.pack(pady=5)

tk.Label(root, text="Quantidade de Faltas:").pack(pady=5)
faltas_entry = tk.Entry(root)
faltas_entry.pack(pady=5)

# Botão de calcular
tk.Button(root, text="Calcular", command=calcular).pack(pady=20)

# Frame de resultado
resultado_label = tk.Label(root, text="", wraplength=400, justify="center")
resultado_label.pack(pady=10)

imagem_label = tk.Label(root)
imagem_label.pack(pady=10)

# Executar a janela principal
root.mainloop()