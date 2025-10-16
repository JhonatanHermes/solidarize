# 🕊️ Solidarize – Sistema de Controle de Doações

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-ativo-success.svg)]()

O **Solidarize** é um sistema web desenvolvido em **Python (Flask)** e **SQLite** para facilitar a **gestão de campanhas beneficentes**, o **cadastro de doadores** e o **registro de doações** em tempo real.  
Foi criado como parte do **Projeto Integrador – Laboratório de Programação (UNISA)**, aplicando conceitos de **engenharia de software**, **programação estruturada**, **banco de dados** e **boas práticas de documentação**.

---

## 🧭 Sumário
- [🚀 Funcionalidades](#-funcionalidades)
- [🧠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Instalação e Execução](#️-instalação-e-execução)
- [🔐 Acesso ao Sistema](#-acesso-ao-sistema)
- [📊 Relatórios](#-relatórios)
- [📂 Estrutura de Pastas](#-estrutura-de-pastas)
- [🎯 Objetivo](#-objetivo)
- [🧾 Licença](#-licença)
- [💬 Contato](#-contato)

---

## 🚀 Funcionalidades

✅ Cadastro e gerenciamento de **doadores**  
✅ Criação e acompanhamento de **campanhas beneficentes**  
✅ Registro de **doações** com valor, data e observação  
✅ **Login e autenticação** de usuários com Flask-Login e Bcrypt  
✅ **Dashboard** com total arrecadado e número de doações  
✅ **Relatório mensal em PDF** com total e listagem detalhada  
✅ Interface responsiva com **Bootstrap 5**

---

## 🧠 Tecnologias Utilizadas

| Categoria | Tecnologia |
|------------|-------------|
| Linguagem  | [Python 3.12](https://www.python.org/) |
| Framework  | [Flask](https://flask.palletsprojects.com/) |
| Banco de Dados | [SQLite](https://www.sqlite.org/) |
| Front-end | [Bootstrap 5](https://getbootstrap.com/) |
| Segurança | Flask-Login · Flask-Bcrypt |
| Relatórios | [ReportLab](https://www.reportlab.com/) |
| Versionamento | Git + GitHub |

---

## ⚙️ Instalação e Execução

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seuusuario/solidarize.git
cd solidarize
2️⃣ Crie o ambiente virtual
bash
Copiar código
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
3️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Configure as variáveis de ambiente
bash
Copiar código
cp .env.example .env
Opcional: altere a SECRET_KEY para uma string aleatória forte.

5️⃣ Execute o projeto
bash
Copiar código
python app.py
Acesse em: http://127.0.0.1:5000

🔐 Acesso ao Sistema
Crie o primeiro usuário em: /register

Faça login em: /login

Após o login, o painel principal mostrará o total arrecadado e o número de doações.

📊 Relatórios
O Solidarize permite gerar relatórios mensais em PDF, com total arrecadado e lista detalhada das doações.
Para gerar o relatório, acesse o menu superior → “PDF Mensal” ou utilize a rota manual:

sql
Copiar código
/reports/monthly?year=2025&month=10
O arquivo será baixado automaticamente.

📂 Estrutura de Pastas
bash
Copiar código
solidarize/
├── app.py                # Factory e registro de blueprints
├── config.py             # Configurações e variáveis de ambiente
├── extensions.py         # Extensões (db, login, bcrypt)
├── models.py             # Modelos: User, Donor, Campaign, Donation
├── auth.py               # Autenticação e login
├── donors.py             # CRUD de doadores
├── campaigns.py          # CRUD de campanhas
├── donations.py          # CRUD de doações
├── reports.py            # Relatório mensal em PDF
├── templates/            # HTMLs com Bootstrap
├── static/style.css      # Estilos básicos
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
🎯 Objetivo
Promover eficiência, transparência e acessibilidade na gestão de doações para pequenas ONGs, igrejas, campanhas e comunidades solidárias — reduzindo erros manuais e aumentando a confiança nas arrecadações.

💬 Contato
📧 Autor: Jhonatan Hermes Lucco Costa
🏫 Instituição: Universidade Santo Amaro – UNISA
💻 Orientador: Prof. Davi Lazer Grave Teixeira de Andrade

💡 “Solidariedade é quando a dor do outro dói em você.”
— Dom Hélder Câmara
