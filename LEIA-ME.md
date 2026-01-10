# 🛍️ Catálogo Digital | Sistema de Gerenciamento de Pedidos

<div align="center">

![GitHub license](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-red)
![MySQL](https://img.shields.io/badge/MySQL-5.7%2B-orange)
![Status](https://img.shields.io/badge/status-Active-success)

**Um sistema web moderno e intuitivo para gerenciamento de pedidos com integração WhatsApp, geração de QR Code PIX e relatórios avançados.**

[Recursos](#-recursos) • [Instalação](#-instalação-rápida) • [Documentação](#-documentação) • [Deploy](#-deploy) • [Suporte](#-suporte)

</div>

---

## 📋 Índice

- [🎯 Objetivo](#-objetivo)
- [✨ Recursos](#-recursos)
- [🚀 Instalação Rápida](#-instalação-rápida)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [⚙️ Configuração](#️-configuração)
- [🌐 Deploy](#-deploy)
- [🔐 Segurança](#-segurança)
- [📚 Rotas da API](#-rotas-da-api)
- [🛠️ Solução de Problemas](#️-solução-de-problemas)
- [📝 Histórico de Versões](#-histórico-de-versões)
- [🤝 Contribuindo](#-contribuindo)
- [📞 Suporte](#-suporte)
- [📄 Licença](#-licença)

---

## 🎯 Objetivo

Oferecer uma solução completa e intuitiva para pequenas e médias empresas gerenciarem seus pedidos, produtos e clientes de forma eficiente, com integração direta ao WhatsApp e geração automática de QR Codes para pagamento PIX.

### 📍 Para Quem?

✅ Restaurantes e Buffets  
✅ Comércios de Alimentos  
✅ Lojas de E-commerce  
✅ Serviços de Delivery  
✅ Estabelecimentos com Controle de Mesas  

---

## ✨ Recursos

### 👥 Gestão de Clientes
- Cadastro completo com dados de contato
- Filtro por data de criação
- Export/Import em Excel
- Histórico de pedidos por cliente
- Soft delete (sem perder dados)

### 📦 Catálogo de Produtos
- Upload de imagens com validação
- Definição de preços e promoções
- Categorização de produtos
- Toggle de visibilidade (ocultar/mostrar)
- Exportação em Excel

### 🛒 Sistema Inteligente de Pedidos
- Carrinho de compras interativo
- Cálculo automático de totais
- Seleção de quantidade em tempo real
- Múltiplas formas de pagamento (Dinheiro, PIX, Cartão)
- Tipos de consumo (No Local, Delivery, Retirada)
- Registro automático de mesa

### 💳 Integração PIX & QR Code
- Geração automática de QR Code para PIX
- Exibição de chave PIX (Cópia e Cola)
- Formato Brcode compatível com todos os bancos
- Link de cópia automática

### 📱 Integração WhatsApp
- Envio automático de pedidos via WhatsApp
- Formatação profissional com emojis
- Link direto para conversa com o cliente
- Suporte a múltiplos números de telefone

### 📊 Relatórios Avançados
- Visualização de todos os pedidos
- Filtros por cliente, data, forma de pagamento
- Resumo de vendas por período
- Exportação em CSV/Excel
- Totalizações automáticas

### ⭐ Pesquisa de Satisfação
- Formulário de feedback interativo
- Armazenamento de respostas
- Análise de satisfação dos clientes

---

## 🚀 Instalação Rápida

### ⚡ 5 Minutos de Setup

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/Williamsrvs/Visibility_System.git
cd "Catálogo Digital"

# 2️⃣ Crie e ative o ambiente virtual
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# 5️⃣ Configure o banco de dados
mysql -h seu-host -u seu-usuario -p seu-banco < app/schema.sql
python create_views.py

# 6️⃣ Inicie o servidor
python app.py
```

🌐 **Acesse em**: `http://localhost:5000`

---

## 📁 Estrutura do Projeto

```
Catálogo Digital/
├── 📂 app/                              # Pacote principal da aplicação
│   ├── 📄 routes.py                     # Rotas e lógica de negócio
│   ├── 📄 config.py                     # Configurações do Flask
│   ├── 📄 schema.sql                    # Estrutura do banco de dados
│   │
│   ├── 📂 static/                       # Arquivos estáticos (CSS, JS, Imagens)
│   │   ├── 📂 css/
│   │   │   ├── style.css
│   │   │   ├── sidebar.css
│   │   │   └── produto.css
│   │   ├── 📂 js/
│   │   │   └── styler.js
│   │   └── 📂 img/
│   │
│   └── 📂 templates/                    # Templates HTML (Jinja2)
│       ├── index.html                   # Página inicial (catálogo)
│       ├── pedidos.html                 # Sistema de pedidos (admin)
│       ├── pedidos_cliente.html         # Sistema de pedidos (cliente)
│       ├── produto.html                 # Gestão de produtos
│       ├── cliente.html                 # Gestão de clientes
│       └── relatorio_pedidos.html       # Relatório de pedidos
│
├── 📄 app.py                            # Arquivo principal (entry point)
├── 📄 wsgi.py                           # WSGI para produção
├── 📄 requirements.txt                  # Dependências Python
├── 📄 docker-compose.yml                # Configuração Docker
├── 📄 .env.example                      # Variáveis de ambiente (exemplo)
├── 📄 .gitignore                        # Arquivos a ignorar no Git
│
└── 📄 README.md / LEIA-ME.md           # Este arquivo
```

---

## ⚙️ Configuração

### 📋 Pré-requisitos

```bash
✅ Requerido:
- Python 3.8+
- MySQL 5.7+
- Git

📦 Pacotes do SO (Linux/Ubuntu):
sudo apt-get install python3-pip python3-venv mysql-client
```

### 🔧 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# ⚙️ FLASK
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# 🗄️ BANCO DE DADOS
MYSQL_HOST=auth-db1937.hstgr.io
MYSQL_PORT=3306
MYSQL_USER=u799109175_menu_prod
MYSQL_PASSWORD=Q1k2v1y5@2025
MYSQL_DB=u799109175_menu_prod

# 🔑 SEGURANÇA
SECRET_KEY=sua-chave-super-secreta-aqui
JWT_SECRET=sua-jwt-secret-key

# 📱 WHATSAPP
WHATSAPP_LOJISTA=5582981090042

# 💳 PIX
CHAVE_PIX=05566941478
NOME_BENEFICIARIO=WILLIAMS RODRIGUES VIEIRA SILVA
```

### 🗄️ Configuração do Banco de Dados

**Opção 1 - Script SQL:**
```bash
mysql -h seu-host -u seu-usuario -p seu-banco < app/schema.sql
```

**Opção 2 - Script Python (Recomendado):**
```bash
python create_views.py
python setup_db.py
```

---

## 🌐 Deploy

### 🐳 Docker Compose (Mais Fácil)

```bash
docker-compose up -d
```

### 🚀 Railway (Recomendado para Produção)

```bash
npm i -g @railway/cli
railway login
railway init
railway variables set MYSQL_HOST=...
git push origin main  # Deploy automático
```

### ☁️ Heroku

```bash
heroku login
heroku create seu-app-name
heroku config:set MYSQL_HOST=seu-host
git push heroku main
```

### 🖥️ Servidor VPS (Ubuntu/Debian)

#### Instalação Completa

```bash
# 1. Instalar dependências
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv mysql-client nginx git

# 2. Clonar repositório
cd /opt
sudo git clone https://github.com/Williamsrvs/Visibility_System.git
cd Visibility_System

# 3. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 4. Instalar dependências Python
pip install -r requirements.txt

# 5. Configurar .env
sudo nano .env

# 6. Inicializar banco
python create_views.py
```

#### Configurar como Serviço (Systemd)

Crie `/etc/systemd/system/catalogo-digital.service`:

```ini
[Unit]
Description=Catálogo Digital - Flask Application
After=network.target mysql.service

[Service]
Type=notify
User=www-data
WorkingDirectory=/opt/Visibility_System
Environment="PATH=/opt/Visibility_System/venv/bin"
ExecStart=/opt/Visibility_System/venv/bin/gunicorn \
  --workers 4 --bind 127.0.0.1:5000 --timeout 120 wsgi:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Ativar:
```bash
sudo systemctl daemon-reload
sudo systemctl enable catalogo-digital
sudo systemctl start catalogo-digital
```

#### Configurar Nginx (Reverse Proxy)

Crie `/etc/nginx/sites-available/catalogo-digital`:

```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name seu-dominio.com;

    ssl_certificate /etc/letsencrypt/live/seu-dominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/seu-dominio.com/privkey.pem;

    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /opt/Visibility_System/app/static/;
        expires 30d;
    }
}
```

Ativar:
```bash
sudo ln -s /etc/nginx/sites-available/catalogo-digital /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### SSL com Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d seu-dominio.com
```

---

## 🔐 Segurança

### ✅ Checklist de Segurança em Produção

- [ ] **SECRET_KEY**: Mude para valor aleatório de 32+ caracteres
- [ ] **HTTPS/SSL**: Configure certificado válido
- [ ] **Senha Forte**: Use 20+ caracteres no banco
- [ ] **Backups**: Configure backups automáticos diários
- [ ] **Firewall**: Apenas portas 80, 443 e 22 abertas
- [ ] **Debug Mode**: Desabilite em produção
- [ ] **Variáveis**: Nunca commite `.env` no Git
- [ ] **Dependências**: Mantenha pacotes atualizados
- [ ] **Logs**: Configure monitoramento centralizado
- [ ] **Rate Limiting**: Implemente em rotas críticas

---

## 📚 Rotas da API

### 🏠 Páginas Públicas

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Catálogo de produtos |
| `/produto/<id>` | GET | Detalhes do produto |
| `/filter_category/<categoria>` | GET | Filtrar por categoria |
| `/pesquisa` | GET, POST | Pesquisa de satisfação |

### 👥 Gestão de Clientes

| Rota | Método | Descrição | Auth |
|------|--------|-----------|------|
| `/cliente` | GET, POST | Listar/Criar | ✅ Login |
| `/cliente/<id>` | PUT, DELETE | Editar/Deletar | ✅ Login |
| `/cliente_excel` | GET | Export Excel | ✅ Login |

### 📦 Gestão de Produtos

| Rota | Método | Descrição | Auth |
|------|--------|-----------|------|
| `/produto` | GET, POST | Listar/Criar | ✅ Login |
| `/produto/<id>` | PUT, DELETE | Editar/Deletar | ✅ Login |
| `/produto/<id>/visibilidade` | PATCH | Toggle | ✅ Admin |
| `/produto_excel` | GET | Export Excel | ✅ Login |

### 🛒 Sistema de Pedidos

| Rota | Método | Descrição | Auth |
|------|--------|-----------|------|
| `/pedidos` | GET, POST | Listar/Criar | ✅ Admin |
| `/pedidos_cliente` | GET | Interface cliente | ❌ Pública |
| `/salvar_pedido` | POST | Salvar BD | ❌ Pública |
| `/enviar_whatsapp` | POST | Enviar WA | ✅ Admin |
| `/relatorio_pedidos` | GET | Relatório | ✅ Admin |

---

## 🛠️ Solução de Problemas

### ❌ Erro: "Connection refused" no MySQL

**Causas:**
- MySQL não está rodando
- Credenciais incorretas
- Host não é acessível

**Solução:**
```bash
# Verificar se MySQL está rodando
sudo systemctl status mysql

# Testar conexão
mysql -h seu-host -u seu-usuario -p seu-banco
```

### ❌ Erro: "ModuleNotFoundError: No module named 'flask'"

**Solução:**
```bash
# Ativar ambiente virtual
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ Erro: "413 Payload Too Large"

**Solução (nginx.conf):**
```nginx
client_max_body_size 50M;
```

### ❌ WhatsApp não funciona

**Verificar:**
1. ChromeDriver compatível com sua versão do Chrome
2. Chrome/Chromium instalado no servidor
3. Display configurado em servidor headless

**Instalar webdriver-manager:**
```bash
pip install webdriver-manager
```

### 🐢 Aplicação lenta?

**Diagnóstico:**
```bash
python diagnostic_db.py
python diagnostic.py
```

**Otimizações:**
- Adicione índices no banco
- Implemente caching (Redis)
- Pagine resultados em relatórios
- Lazy load de imagens grandes

---

## 📝 Histórico de Versões

### v1.5.0 - 2026-01-17 (Atual)
- ✅ Reorganização layout `pedidos_cliente.html`
- ✅ Responsividade completa (tablet + mobile)
- ✅ Botões mais destacados e intuitivos

### v1.4.0 - 2025-12-15
- ✅ Sistema de visibilidade de produtos
- ✅ Soft delete implementado
- ✅ Filtro ativo = 1 em todas as rotas

### v1.3.0 - 2025-11-27
- ✅ 3 bugs críticos corrigidos
- ✅ 5 novos campos adicionados

### v1.2.0 - 2025-10-10
- ✅ Integração WhatsApp completa
- ✅ Geração de QR Code PIX
- ✅ Exportação Excel

### v1.1.0 - 2025-09-01
- ✅ Carrinho de compras interativo
- ✅ Múltiplas formas de pagamento

### v1.0.0 - 2025-08-01
- ✅ MVP: Gestão de clientes, produtos, pedidos

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add some Feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código

- **Python**: PEP 8
- **JavaScript**: ES6+
- **HTML/CSS**: Indentação 4 espaços

---

## 📞 Suporte

### 🐛 Reportar Bug

Abra uma [issue](https://github.com/Williamsrvs/Visibility_System/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Screenshot/log de erro
- Seu ambiente (SO, Python, etc)

### 💡 Sugerir Melhoria

Abra uma [discussion](https://github.com/Williamsrvs/Visibility_System/discussions)!

### 📧 Contato Direto

- **WhatsApp**: [5582981090042](https://wa.me/5582981090042)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

```
MIT License

Copyright (c) 2026 Williams Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

<div align="center">

## ⭐ Gostou? Dê uma estrela! ⭐

![Stars](https://img.shields.io/github/stars/Williamsrvs/Visibility_System?style=social)
![Forks](https://img.shields.io/github/forks/Williamsrvs/Visibility_System?style=social)

**Desenvolvido com ❤️ para Williams**

**Última atualização**: 10 de janeiro de 2026

</div>
