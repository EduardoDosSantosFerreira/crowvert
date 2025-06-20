# 🪶 crowvert

> Conversor de arquivos moderno, rápido e eficiente — com interface amigável, suporte a múltiplos formatos e ideal para tarefas do dia a dia.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-orange)

---

## ✨ Visão Geral

**crowvert** é um aplicativo desktop escrito em **Python**, com **interface gráfica via Tkinter/PyQt5**, desenvolvido para facilitar a **conversão de arquivos em massa**.

Criado para usuários que precisam de **agilidade**, **simplicidade** e **um visual agradável**, sem complicações técnicas. O foco é produtividade com elegância.

---

## 🚀 Funcionalidades

✅ Conversão de `.txt` para `.docx`  
✅ Extração `.7z` para `.zip`  
✅ Conversão de `.docx` para `.pdf`  
✅ Conversão de `.pdf` para `.docx`  
✅ Conversão de `.svg` para `.png`  
🎯 Interface leve com **PyQt5/Tkinter**  
💾 Histórico e controle de conversões  
🔧 Modular e fácil de manter

---

## 📁 Estrutura do Projeto

```bash
crowvert/
├── build/                # Arquivos gerados pela compilação
├── dist/                 # Executável final
├── src/
│   ├── assets/           # Imagens, ícones e recursos
│   ├── converters/       # Conversores organizados por tipo
│   ├── ui/               # Interface Tkinter/PyQt5
│   ├── utils/            # Funções auxiliares e helpers
│   └── crowvert.py           # Ponto de entrada da aplicação
├── crowvert.spec             # Configuração do PyInstaller
├── version.txt           # Metadados do executável
├── .gitattributes        # Força o GitHub a reconhecer como Python
└── README.md             # Este arquivo
```

---

## 🛠️ Requisitos

* Python `3.11+`
* Pip

### 📦 Instale as dependências:

```bash
pip install -r requirements.txt
```

(Se ainda não tiver esse arquivo, crie com os pacotes que está usando, ex: `docx`, `py7zr`, `docx2pdf`, `pdf2docx`, `cairosvg` etc.)

---

## 🧪 Como Rodar

```bash
python src/crowvert.py
```

Ou crie um executável com:

```bash
pyinstaller --onefile --windowed --icon=src/assets/img/profile_icons/crowvert.ico --version-file=version.txt crowvert.py
```

---

## 🌐 Página do Projeto

[🔗 Veja a página no GitHub Pages](https://eduardodossantosferreira.github.io/crowvert/)

---

## 👨‍💻 Autor

Desenvolvido por [Eduardo dos Santos Ferreira](https://github.com/EduardoDosSantosFerreira)
📧 [eduardodossantosferreira@gmail.com](mailto:eduardodossantosferreira@gmail.com)

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

⭐ Se curtir o projeto, **deixe uma estrela!**

```

---

Se quiser, posso também montar o conteúdo do `requirements.txt` com base nas bibliotecas que você usou — quer? Ou prefere gerar o [`.gitattributes`](f) pra corrigir a linguagem mostrada no GitHub?
```
