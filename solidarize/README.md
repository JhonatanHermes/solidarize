# Solidarize (Flask + SQLite)

Sistema simples de controle de doações (doadores, campanhas e doações), com autenticação e relatório mensal em PDF.

## Requisitos
- Python 3.10+
- Pip + venv

## Instalação
```bash
cd solidarize
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Opcional: edite SECRET_KEY no .env
```

## Execução
```bash
# Executar o app
python -m flask --app app:create_app run
# ou
python app.py
```

## Usuário inicial
- Acesse /register para criar o primeiro usuário.

## Relatório PDF
- Em sessão autenticada, clique em **PDF Mensal** (rota: `/reports/monthly?year=YYYY&month=MM`).
```