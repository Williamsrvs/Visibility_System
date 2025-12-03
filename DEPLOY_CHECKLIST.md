# Checklist de Deploy - Catálogo Digital

## ✅ Checklist Pre-Deploy

### 🔍 Verificações Iniciais
- [ ] Todas as dependências instaladas: `pip install -r requirements.txt`
- [ ] Arquivo `.env` configurado com valores de produção
- [ ] Banco de dados criado e populado com schema
- [ ] Testes locais executados: `python app.py`

### 🗄️ Banco de Dados
- [ ] MySQL/MariaDB instalado e rodando
- [ ] Database `u799109175_menu_prod` criado
- [ ] Schema aplicado: `mysql < app/schema.sql`
- [ ] Views criadas: `python create_views.py`
- [ ] Backup do banco realizado
- [ ] Usuário com permissões corretas criado

### 🛡️ Segurança
- [ ] `SECRET_KEY` alterado no `config.py` (valor único e forte)
- [ ] Credenciais do banco não expostas no repositório
- [ ] `.env` adicionado ao `.gitignore`
- [ ] Certificado SSL configurado (HTTPS)
- [ ] CORS configurado se necessário

### 📁 Arquivos e Pastas
- [ ] Pasta `static/uploads` com permissões de escrita
- [ ] Pasta `logs` criada (ou definida no config)
- [ ] Permissões corretas: `chmod 755` para diretórios, `644` para arquivos

### 🌐 Configuração Web
- [ ] Nginx/Apache reverso proxy configurado
- [ ] Porta 5000 (ou definida) aberta no firewall
- [ ] HTTPS redirecionando HTTP
- [ ] Headers de segurança configurados

### 🤖 WhatsApp/Selenium
- [ ] ChromeDriver baixado automaticamente por `webdriver-manager`
- [ ] Número WhatsApp do lojista configurado no `.env`
- [ ] Teste de envio via WhatsApp realizado

### 📊 Monitoramento
- [ ] Logging configurado e testado
- [ ] Arquivo `app_errors.log` monitorado
- [ ] Health check endpoint verificado

---

## 🚀 Deploy Checklist

### Opção 1: Heroku
```bash
[ ] heroku login
[ ] heroku create seu-app-name
[ ] heroku config:set MYSQL_HOST=seu-host
[ ] heroku config:set MYSQL_USER=seu-usuario
[ ] heroku config:set MYSQL_PASSWORD=sua-senha
[ ] git push heroku main
[ ] heroku open
[ ] heroku logs --tail
```

### Opção 2: Railway
```bash
[ ] railway login
[ ] railway init
[ ] railway link
[ ] railway deploy
[ ] railway open
```

### Opção 3: VPS (Ubuntu/Debian)
```bash
[ ] git clone repositorio
[ ] python3 -m venv venv
[ ] source venv/bin/activate
[ ] pip install -r requirements.txt
[ ] systemctl start catalogo-digital
[ ] systemctl enable catalogo-digital
[ ] nginx -t
[ ] systemctl reload nginx
```

---

## ✅ Pós-Deploy Checklist

### 🔍 Verificações
- [ ] Site acessível via HTTPS
- [ ] Login funcionando
- [ ] Cadastro de clientes funcionando
- [ ] Cadastro de produtos funcionando
- [ ] Sistema de pedidos funcionando
- [ ] Envio via WhatsApp funcionando
- [ ] Relatórios carregando corretamente
- [ ] Exportação em Excel funcionando
- [ ] Banco de dados salvando dados corretamente

### 📊 Monitoramento
- [ ] Logs sendo registrados
- [ ] Performance dentro do esperado
- [ ] Sem erros 500
- [ ] Sem vazamento de memória

### 🆘 Rollback
- [ ] Backup do banco antes de deploy
- [ ] Versão anterior do código disponível
- [ ] Plano de rollback preparado

---

## 📞 Troubleshooting Pós-Deploy

### Erro 502 Bad Gateway
```bash
# Verifique se o app está rodando
ps aux | grep python
# Reinicie o serviço
systemctl restart catalogo-digital
```

### Erro 500 Internal Server Error
```bash
# Verifique os logs
tail -f app_errors.log
# Verifique conexão com banco
python diagnostic.py
```

### WhatsApp não funcionando
```bash
# Verifique ChromeDriver
ls -la .wdm/
# Teste manualmente
python create_views.py
```

### Banco de dados lento
```sql
-- Adicione índices
CREATE INDEX idx_pedidos_cliente ON tbl_pedidos(id_cliente);
CREATE INDEX idx_detalhes_pedido ON tbl_detalhes_pedido(id_pedido);
-- Analise a tabela
ANALYZE TABLE tbl_pedidos, tbl_detalhes_pedido;
```

---

## 🔄 Manutenção Periódica

### Diária
- [ ] Verificar logs de erro
- [ ] Confirmar que o site está acessível

### Semanal
- [ ] Backup do banco de dados
- [ ] Revisão de performance
- [ ] Atualização de dependências críticas

### Mensal
- [ ] Limpeza de logs antigos
- [ ] Auditoria de segurança
- [ ] Planejamento de melhorias

---

## 📚 Referências

- [Flask Deployment Guides](https://flask.palletsprojects.com/en/latest/deploying/)
- [Gunicorn Documentation](https://gunicorn.org/)
- [Nginx Configuration](https://nginx.org/en/docs/)
- [MySQL Best Practices](https://dev.mysql.com/doc/)

---

**Última atualização: 27 de novembro de 2025**
