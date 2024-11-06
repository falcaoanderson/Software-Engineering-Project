import tkinter as tk
from tkinter import messagebox
import backend  # Importa o backend

# Classe principal para a interface geral
class SistemaVendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão de Vending Machines")
        self.root.geometry("500x400")
        
        # Inicializa o banco de dados
        backend.inicializar_banco()
        
        # Título principal
        titulo = tk.Label(self.root, text="Sistema de Gestão de Vending Machines", font=("Helvetica", 16))
        titulo.pack(pady=20)
        
        # Botões para abrir as janelas das funcionalidades
        btn_estoque = tk.Button(self.root, text="Visualizar Estoque", command=self.abrir_visualizar_estoque, width=30)
        btn_estoque.pack(pady=10)

        btn_problema = tk.Button(self.root, text="Reportar Problema", command=self.abrir_reportar_problema, width=30)
        btn_problema.pack(pady=10)

        btn_relatorios = tk.Button(self.root, text="Visualizar Relatórios", command=self.abrir_visualizar_relatorios, width=30)
        btn_relatorios.pack(pady=10)

        # Rodapé
        rodape = tk.Label(self.root, text="Desenvolvido por [Seu Nome]", font=("Helvetica", 10))
        rodape.pack(side="bottom", pady=10)

    def abrir_visualizar_estoque(self):
        JanelaVisualizarEstoque(self.root)

    def abrir_reportar_problema(self):
        JanelaReportarProblema(self.root)

    def abrir_visualizar_relatorios(self):
        JanelaVisualizarRelatorios(self.root)

# Classe para a funcionalidade de Reportar Problema
class JanelaReportarProblema:
    def __init__(self, root):
        self.janela = tk.Toplevel(root)
        self.janela.title("Reportar Problema")
        self.janela.geometry("400x300")
        
        tk.Label(self.janela, text="Reportar Problema").pack(pady=5)
        
        # Tipo de Problema
        self.tipo_problema_var = tk.StringVar()
        tk.Radiobutton(self.janela, text="Vending Machine", variable=self.tipo_problema_var, value="Vending Machine").pack()
        tk.Radiobutton(self.janela, text="Rede Social", variable=self.tipo_problema_var, value="Rede Social").pack()
        
        # Descrição do Problema
        tk.Label(self.janela, text="Descrição:").pack(pady=5)
        self.descricao_entry = tk.Text(self.janela, height=5, width=40)
        self.descricao_entry.pack()
        
        # Botão para Enviar o Problema
        enviar_btn = tk.Button(self.janela, text="Enviar Problema", command=self.enviar_problema)
        enviar_btn.pack(pady=10)

    def enviar_problema(self):
        tipo = self.tipo_problema_var.get()
        descricao = self.descricao_entry.get("1.0", "end-1c")

        if not tipo or not descricao:
            messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
            return

        # Envia os dados para o backend
        backend.adicionar_problema("Usuário 1", tipo, descricao)
        messagebox.showinfo("Reporte Enviado", "Problema reportado com sucesso!")
        self.descricao_entry.delete("1.0", "end")

# Classe para a funcionalidade de Visualizar Relatórios
class JanelaVisualizarRelatorios:
    def __init__(self, root):
        self.janela = tk.Toplevel(root)
        self.janela.title("Relatórios")
        self.janela.geometry("400x300")
        
        tk.Label(self.janela, text="Relatórios de Vendas, Estoque e Avaliações").pack(pady=20)
        
class JanelaVisualizarEstoque:
    def __init__(self, root):
        self.janela = tk.Toplevel(root)
        self.janela.title("Relatórios")
        self.janela.geometry("400x300")
        
        tk.Label(self.janela, text="Estoque").pack(pady=20)

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaVendingMachineApp(root)
    root.mainloop()
