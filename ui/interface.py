import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from python import (
    txt_to_docx,
    docx_to_txt,
    docx_to_pdf,
    pdf_to_docx,
    svg_to_png,
    pdf_to_png,
    sevenzip_to_zip,
    png_to_pdf,
    zip_to_sevenzip,
    jpg_to_png,
    png_to_ico,
    csv_to_xlsx,
    rtf_to_docx,
    rtf_to_pdf,
)
DOCUMENTOS = {
    "TXT → DOCX": (txt_to_docx, ".docx", [("Arquivos TXT", "*.txt")]),
    "RTF → DOCX": (rtf_to_docx, ".docx", [("Arquivos RTF", "*.rtf")]),
    "RTF → PDF": (rtf_to_pdf, ".pdf", [("Arquivos RTF", "*.rtf")]),
    "DOCX → TXT": (docx_to_txt, ".txt", [("Arquivos DOCX", "*.docx")]),
    "DOCX → PDF": (docx_to_pdf, ".pdf", [("Arquivos DOCX", "*.docx")]),
    "PDF → DOCX": (pdf_to_docx, ".docx", [("Arquivos PDF", "*.pdf")]),
    "CSV → XLSX": (csv_to_xlsx, ".xlsx", [("Arquivos CSV", "*.csv")]),
}
IMAGENS = {
    "SVG → PNG": (svg_to_png, ".png", [("Arquivos SVG", "*.svg")]),
    "PDF → PNG": (pdf_to_png, None, [("Arquivos PDF", "*.pdf")]),
    "PNG → PDF": (png_to_pdf, None, [("Arquivos PNG", "*.png")]),
    "JPG → PNG": (
        jpg_to_png,
        ".png",
        [("Imagens JPG", "*.jpg"), ("Imagens JPEG", "*.jpeg")],
    ),
    "PNG → ICO": (png_to_ico, ".ico", [("Arquivos PNG", "*.png")]),
}
COMPRESSAO = {
    "7Z → ZIP": (sevenzip_to_zip, ".zip", [("Arquivos 7Z", "*.7z")]),
    "ZIP → 7Z": (zip_to_sevenzip, ".7z", [("Arquivos ZIP", "*.zip")]),
}
FUNCOES_CONVERSAO = {**DOCUMENTOS, **IMAGENS, **COMPRESSAO}
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)
    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw,
            text=self.text,
            justify=tk.LEFT,
            background="#ffffe0",
            relief=tk.SOLID,
            borderwidth=1,
            font=("Segoe UI", "9", "normal"),
        )
        label.pack(ipadx=5, ipady=3)
    def hide_tip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None
class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("crowvert")
        self.geometry("650x500")
        self.configure(bg="#ffffff")
        self.resizable(False, False)
        self.arquivos_dict = {}
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TButton",
            font=("Segoe UI", 11, "bold"),
            padding=8,
            foreground="#ffffff",
            background="#6f42c1",  
            borderwidth=0,
        )
        style.map(
            "TButton",
            background=[("active", "#5a32a3")],
        )
        style.configure("TCombobox", font=("Segoe UI", 10), padding=5)
        style.configure(
            "Horizontal.TProgressbar",
            troughcolor="#e1e1e1",
            bordercolor="#d9d9d9",
            background="#6f42c1",
            thickness=20,
        )
        titulo = tk.Label(
            self,
            text="crowvert",
            bg="#ffffff",
            fg="#6f42c1",
            font=("Segoe UI", 20, "bold"),
        )
        titulo.pack(pady=(20, 15))
        frame_controles = tk.Frame(self, bg="#ffffff")
        frame_controles.pack(pady=10, padx=20, fill="x")
        self.btn_selecionar = ttk.Button(
            frame_controles,
            text="📂 Selecionar Arquivos",
            command=self.selecionar_arquivos,
            width=18,
        )
        self.btn_converter = ttk.Button(
            frame_controles,
            text="⚡ Converter",
            command=self.converter_arquivos,
            width=14,
        )
        self.btn_limpar = ttk.Button(
            frame_controles, text="🧹 Limpar Lista", command=self.limpar_lista, width=14
        )
        self.btn_selecionar.grid(row=0, column=0, padx=5, sticky="ew")
        self.btn_converter.grid(row=0, column=1, padx=5, sticky="ew")
        self.btn_limpar.grid(row=0, column=2, padx=5, sticky="ew")
        frame_controles.grid_columnconfigure(0, weight=1)
        frame_controles.grid_columnconfigure(1, weight=1)
        frame_controles.grid_columnconfigure(2, weight=1)
        self.categoria_var = tk.StringVar(value="DOCUMENTOS")
        self.conversao_var = tk.StringVar()
        self.categorias_dict = {
            "DOCUMENTOS": DOCUMENTOS,
            "IMAGENS": IMAGENS,
            "COMPRESSÃO": COMPRESSAO,
        }
        frame_combobox = tk.Frame(self, bg="#ffffff")
        frame_combobox.pack(pady=(0, 10), padx=20, fill="x")
        lbl_categoria = tk.Label(
            frame_combobox, text="Categoria:", bg="#ffffff", font=("Segoe UI", 11)
        )
        lbl_categoria.grid(row=0, column=0, sticky="w")
        self.combo_categoria = ttk.Combobox(
            frame_combobox,
            textvariable=self.categoria_var,
            state="readonly",
            values=list(self.categorias_dict.keys()),
            width=15,
            font=("Segoe UI", 10),
        )
        self.combo_categoria.grid(row=1, column=0, sticky="ew", padx=(0, 15))
        self.combo_categoria.bind("<<ComboboxSelected>>", self.atualizar_conversoes)
        ToolTip(self.combo_categoria, "Selecione a categoria de conversão")
        lbl_conversao = tk.Label(
            frame_combobox, text="Conversão:", bg="#ffffff", font=("Segoe UI", 11)
        )
        lbl_conversao.grid(row=0, column=1, sticky="w")
        self.combo_conversao = ttk.Combobox(
            frame_combobox,
            textvariable=self.conversao_var,
            state="readonly",
            values=list(DOCUMENTOS.keys()),
            width=30,
            font=("Segoe UI", 10),
        )
        self.combo_conversao.grid(row=1, column=1, sticky="ew")
        ToolTip(self.combo_conversao, "Selecione o tipo de conversão")
        frame_combobox.grid_columnconfigure(0, weight=1)
        frame_combobox.grid_columnconfigure(1, weight=3)
        frame_lista = tk.Frame(self, bg="#ffffff")
        frame_lista.pack(padx=20, fill="both", expand=True)
        self.scrollbar = ttk.Scrollbar(frame_lista, orient="vertical")
        self.lista_arquivos = tk.Listbox(
            frame_lista,
            height=14,
            bg="#f0f0f0",
            borderwidth=1,
            relief="solid",
            selectmode=tk.EXTENDED,
            font=("Segoe UI", 10),
            yscrollcommand=self.scrollbar.set,
            activestyle="none",
        )
        self.scrollbar.config(command=self.lista_arquivos.yview)
        self.lista_arquivos.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.barra_progresso = ttk.Progressbar(
            self,
            orient="horizontal",
            mode="determinate",
            style="Horizontal.TProgressbar",
        )
        self.barra_progresso.pack(fill="x", padx=20, pady=(15, 20), ipady=5)
        self.atualizar_conversoes()
    def atualizar_conversoes(self, event=None):
        categoria = self.categoria_var.get()
        opcoes = list(self.categorias_dict[categoria].keys())
        self.combo_conversao["values"] = opcoes
        self.conversao_var.set(opcoes[0])
    def selecionar_arquivos(self):
        option = self.conversao_var.get()
        _, _, tipos = FUNCOES_CONVERSAO.get(
            option, (None, None, [("Todos os arquivos", "*.*")])
        )
        arquivos = filedialog.askopenfilenames(filetypes=tipos)
        for caminho in arquivos:
            nome = os.path.basename(caminho)
            if nome not in self.arquivos_dict:
                self.arquivos_dict[nome] = caminho
                self.lista_arquivos.insert(tk.END, nome)
    def limpar_lista(self):
        self.lista_arquivos.delete(0, tk.END)
        self.arquivos_dict.clear()
        self.barra_progresso["value"] = 0
    def converter_arquivos(self):
        if not self.arquivos_dict:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
            return
        option = self.conversao_var.get()
        funcao_converter, extensao_saida, _ = FUNCOES_CONVERSAO.get(
            option, (None, None, None)
        )
        if funcao_converter is None:
            messagebox.showerror("Erro", "Opção de conversão inválida.")
            return
        pasta_saida = filedialog.askdirectory(title="Selecione a pasta de saída")
        if not pasta_saida:
            return
        total = len(self.arquivos_dict)
        self.barra_progresso["maximum"] = total
        self.barra_progresso["value"] = 0
        for i, (nome, caminho_entrada) in enumerate(self.arquivos_dict.items()):
            nome_base = os.path.splitext(nome)[0]
            if option == "PDF → PNG":
                caminho_saida = (
                    pasta_saida  
                )
            else:
                caminho_saida = os.path.join(
                    pasta_saida, f"{nome_base}{extensao_saida}"
                )
                contador = 1
                while os.path.exists(caminho_saida):
                    caminho_saida = os.path.join(
                        pasta_saida, f"{nome_base}_{contador}{extensao_saida}"
                    )
                    contador += 1
            try:
                funcao_converter(caminho_entrada, caminho_saida)
            except Exception as e:
                if str(e):
                    messagebox.showerror("Erro", f"Erro ao converter {nome}:\n{e}")
                else:
                    messagebox.showerror(
                        "Erro", f"Erro ao converter {nome}: erro desconhecido"
                    )
                continue
            self.barra_progresso["value"] = i + 1
            self.update_idletasks()
        messagebox.showinfo("Sucesso", f"{total} arquivo(s) convertido(s) com sucesso!")
if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
