import tkinter as tk
import google.generativeai as genai
import threading

# Configurar a API key do Google Gemini
genai.configure(api_key="Insira aqui sua API Key do google gemini")

# Função para gerar respostas usando a API do Gemini
def generate_response():
    user_input = input_field.get()

    # Exibir o texto de carregamento
    loading_label.pack()  # Mostrar o indicador de carregamento
    result_text.delete(1.0, tk.END)  # Limpar texto anterior

    # Selecionar o modelo correto
    model = genai.GenerativeModel('gemini-pro')

    # Gerar a resposta usando o modelo Gemini
    response = model.generate_content(user_input)

    # Exibir a resposta na interface gráfica
    result_text.delete(1.0, tk.END)  # Limpar texto anterior
    result_text.insert(tk.END, response.text)  # Adicionar a nova resposta
    loading_label.pack_forget()  # Ocultar o indicador de carregamento

# Função para capturar a tecla "Enter"
def on_enter(event):
    # Usar threading para evitar congelamento da interface
    threading.Thread(target=generate_response).start()

# Configurar a interface gráfica
root = tk.Tk()
root.title("Assistente de Codificação com Google Gemini")
root.geometry("800x600")  # Tamanho ajustado para 800x600
root.configure(bg="#1A1A1A")  # Cor de fundo definida

# Campo de entrada para o texto do usuário
input_field = tk.Entry(root, width=50, font=("Sans Serif", 12), bg="#2E2E2E", fg="white")
input_field.pack(pady=10)
input_field.bind("<Return>", on_enter)  # Bind para a tecla "Enter"

# Botão para gerar resposta
submit_button = tk.Button(root, text="Gerar Resposta", command=on_enter, bg="#2E2E2E", fg="white", font=("Sans Serif", 12, "bold"))
submit_button.pack(pady=10)

# Frame para exibir o resultado
result_frame = tk.Frame(root, bg="#1A1A1A")
result_frame.pack(fill="both", expand=True)

# Campo de texto para exibir o resultado
result_text = tk.Text(result_frame, wrap="word", font=("Sans Serif", 12), bg="#2E2E2E", fg="white")
result_text.pack(fill="both", expand=True)

# Label para indicar carregamento
loading_label = tk.Label(root, text="Carregando...", font=("Sans Serif", 12), bg="#1A1A1A", fg="white")

# Iniciar a interface gráfica
try:
    root.mainloop()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
