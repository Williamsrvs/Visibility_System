# 🛍️ Catálogo Digital - Sistema de Pedidos

Sistema web moderno para gerenciamento de pedidos, integrado com WhatsApp e gerador de relatórios.

## 📋 Funcionalidades

✅ **Gestão de Clientes**
- Cadastro e gerenciamento de clientes
- Filtro por data de criação
- Download em Excel

✅ **Catálogo de Produtos**
- Upload de imagens de produtos
- Definição de valores e promoções
- Exportação em Excel

✅ **Sistema de Pedidos**
- Carrinho de compras interativo
- Seleção de produtos por cliente
- Cálculo automático de totais
- QR Code PIX para pagamento
- Envio via WhatsApp com Selenium

✅ **Relatórios**
- Visualização de todos os pedidos
- Resumo por cliente
- Exportação em CSV
- Totalizações por período

✅ **Pesquisa de Satisfação**
- Formulário de feedback
- Armazenamento de respostas

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- MySQL 5.7+
- Git

### Passos de Instalação

1. **Clone ou baixe o projeto:**
```bash
git clone <seu-repositorio>
cd "Catálogo Digital"
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais do banco de dados e configurações.

6. **Execute o script de inicialização do banco:**
```bash
# Conecte ao seu MySQL e execute:
mysql -u seu_usuario -p < app/schema.sql
```

Ou use o script Python de criação de views:
```bash
python create_views.py
```

7. **Inicie o servidor:**
```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
Catálogo Digital/
├── app/
│   ├── config.py              # Configurações do Flask
│   ├── routes.py              # Rotas e lógica principal
│   ├── schema.sql             # Script de criação de banco de dados
│   ├── views_pedidos.sql      # Views para relatórios
│   ├── static/
│   │   ├── css/               # Arquivos CSS
│   │   ├── js/                # Arquivos JavaScript
│   │   └── img/               # Imagens
│   └── templates/             # Templates HTML
│       ├── index.html
│       ├── pedidos.html
│       ├── relatorio_pedidos.html
│       └── ...
├── app.py                     # Arquivo principal
├── requirements.txt           # Dependências Python
├── .env.example              # Variáveis de ambiente (exemplo)
├── .gitignore                # Arquivos a ignorar no Git
├── Procfile                  # Configuração para Heroku/Railway
├── README.md                 # Este arquivo
└── create_views.py           # Script para criar views

```

## ⚙️ Configuração

### Variáveis de Ambiente (.env)

```env
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

MYSQL_HOST=seu-host
MYSQL_PORT=3306
MYSQL_USER=seu-usuario
MYSQL_PASSWORD=sua-senha
MYSQL_DB=seu-banco

SECRET_KEY=sua-chave-secreta
WHATSAPP_LOJISTA=55XX999999999
```

### Configuração do Banco de Dados

O arquivo `app/schema.sql` contém toda a estrutura do banco de dados. Execute-o em seu servidor MySQL:

```bash
mysql -h seu-host -u seu-usuario -p seu-banco < app/schema.sql
```

## 🌐 Deploy

### Heroku / Railway

1. **Instale o CLI da plataforma**

2. **Crie um arquivo `.env` com as variáveis de produção**

3. **Deploy:**
```bash
# Heroku
heroku login
heroku create seu-app-name
git push heroku main

# Railway
railway link
railway deploy
```

### Servidor VPS (Ubuntu/Debian)

1. **Instale as dependências:**
```bash
sudo apt update
sudo apt install python3-pip python3-venv mysql-client
```

2. **Clone o repositório:**
```bash
git clone <seu-repositorio> /opt/catalogo-digital
cd /opt/catalogo-digital
```

3. **Configure o ambiente:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Configure o serviço (systemd):**

Crie `/etc/systemd/system/catalogo-digital.service`:
```ini
[Unit]
Description=Catálogo Digital Flask App
After=network.target

[Service]
User=www-data
WorkingDirectory=/opt/catalogo-digital
Environment="PATH=/opt/catalogo-digital/venv/bin"
ExecStart=/opt/catalogo-digital/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

5. **Configure com Nginx (reverso proxy):**

```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

6. **Inicie o serviço:**
```bash
sudo systemctl start catalogo-digital
sudo systemctl enable catalogo-digital
```

## 🔐 Segurança em Produção

- [ ] Mude a `SECRET_KEY` no arquivo de configuração
- [ ] Configure SSL/TLS com Let's Encrypt
- [ ] Ative autenticação de usuários
- [ ] Use variáveis de ambiente para credenciais
- [ ] Configure firewall para aceitar apenas portas necessárias
- [ ] Faça backups regulares do banco de dados
- [ ] Mantenha as dependências atualizadas

## 📚 Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/cliente` | GET, POST | Gestão de clientes |
| `/produto` | GET, POST, PUT, DELETE | Gestão de produtos |
| `/pedidos` | GET, POST | Sistema de pedidos |
| `/salvar_pedido` | POST | Salva pedido no banco |
| `/enviar_whatsapp` | POST | Envia pedido via WhatsApp |
| `/relatorio_pedidos` | GET | Exibe relatório de pedidos |
| `/pesquisa` | GET, POST | Pesquisa de satisfação |
| `/contato` | GET, POST | Formulário de contato |
| `/produto_excel` | GET | Exporta produtos em Excel |
| `/cliente_excel` | GET | Exporta clientes em Excel |

## 🐛 Troubleshooting

### Erro: "Unknown column 'valor_total'"
Execute o script SQL do schema novamente ou adicione a coluna manualmente:
```sql
ALTER TABLE tbl_pedidos ADD COLUMN valor_total DECIMAL(10,2);
ALTER TABLE tbl_detalhes_pedido ADD COLUMN valor_total DECIMAL(10,2);
```

### Erro: "Connection refused" ao conectar ao MySQL
Verifique se:
- O servidor MySQL está rodando
- As credenciais no `.env` estão corretas
- O host está acessível

### WhatsApp não está funcionando
- Certifique-se de que o ChromeDriver está compatível com sua versão do Chrome
- O `webdriver-manager` baixa automaticamente a versão correta

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, abra uma issue no repositório.

## 📄 Licença

Este projeto é fornecido como está. Use livremente.

---

**Desenvolvido com ❤️ para Williams**

Última atualização: 27 de novembro de 2025
# sistema_buffet_luisa_gourmet
