# 🚨 GUIA DE TROUBLESHOOTING

Se algo não funcionar, siga este guia para diagnosticar e resolver.

---

## ❓ "O botão + Adicionar Produto não faz nada"

### Diagnóstico
1. Abra DevTools: **F12**
2. Vá para aba **Console**
3. Procure por erro iniciando com **"❌"**

### Soluções

**Se vir: "❌ ERRO CRÍTICO: Botão btnAddProduct não encontrado!"**
- [ ] Hard refresh: **Ctrl+Shift+R**
- [ ] Se persiste: Verifique se linha 748 do pedidos.html tem `id="btnAddProduct"`

**Se vir: TypeError em linha 1XXX**
- [ ] Copie a linha inteira do erro
- [ ] Verifique o console para ver exatamente qual elemento está null
- [ ] Pode estar faltando um elemento HTML no template

**Se não vir nenhum erro:**
- [ ] Clique no botão e observe console
- [ ] Pressione F12 > Elements (ou Inspector)
- [ ] Procure por `<button id="btnAddProduct">`
- [ ] Clique nele e veja no console se há listener

### Teste Manual
No console, digite:
```javascript
document.getElementById('btnAddProduct').click()
```

Se funciona manualmente, o problema é no event listener. Se retorna erro, o botão não existe.

---

## ❓ "O QR Code não aparece"

### Diagnóstico
1. Adicione pelo menos 1 produto ao carrinho
2. Olhe para o **painel direito** (área de resumo)
3. Procure pela seção com título "QR Code PIX"

### Soluções

**Se não vir a seção de resumo:**
- [ ] Adicione mais produtos (mínimo 2-3)
- [ ] Atualize a página (F5)
- [ ] Verifique se há erro no console (F12)

**Se a seção existe mas o QR Code não aparece:**
- [ ] F12 > Console, procure por erro com "QRCode"
- [ ] Verifique se a biblioteca está carregada:
  ```javascript
  console.log(QRCode)
  ```
- [ ] Se retorna "undefined", a biblioteca não carregou
- [ ] Solução: Aguarde um pouco e atualize a página

**Se o QR Code aparece mas o valor está errado:**
- [ ] Console > digite:
  ```javascript
  console.log(carrinho)
  ```
- [ ] Verifique se os valores dos produtos estão corretos
- [ ] Calcule manualmente e compare

### Teste Manual
No console, digite:
```javascript
updateQRCode(50.00)
```

Deve aparecer um novo QR Code com valor 50.00. Se aparece, o problema está na função que calcula o total.

---

## ❓ "Erro ao salvar: 'endereco' is not defined"

### Diagnóstico
1. Clique em "🖨️ Imprimir Pedido" ou "📱 Enviar WhatsApp"
2. Verifique o alerta que aparece

### Solução
**Este erro foi CORRIGIDO em 2024-01-10.**

Se ainda vir este erro:
- [ ] Hard refresh: **Ctrl+Shift+R**
- [ ] Feche a aba e abra novamente
- [ ] Se persiste, o arquivo `app/templates/pedidos.html` não foi atualizado

**Para verificar se foi atualizado:**
1. F12 > Console
2. Digite:
```javascript
fetch('/api/produtos').then(r => r.json()).then(d => console.log(d))
```
3. Se retorna produtos, o código está atualizado

### Se ainda tiver erro
1. F12 > Network
2. Clique em "Imprimir Pedido"
3. Procure pela requisição POST para `/salvar_pedido`
4. Clique nela > aba Response
5. Copie o erro inteiro

---

## ❓ "Pedido não salva no banco de dados"

### Diagnóstico
1. F12 > Network
2. Clique em "🖨️ Imprimir Pedido"
3. Procure por requisição POST `/salvar_pedido`
4. Clique nela e vá para aba **Response**

### Soluções

**Se Response mostra: `{"status": "sucesso", "id_pedido": XX}`**
- Pedido FOI salvo no banco ✅
- Verificar banco: `SELECT * FROM tbl_pedidos WHERE id_pedido = XX`

**Se Response mostra erro de MySQL:**
- Problema no banco de dados
- Verifique conexão MySQL
- Verifique se tabela `tbl_detalhes_pedido` tem as 5 colunas novas:
  ```sql
  DESCRIBE tbl_detalhes_pedido;
  -- Procure por: endereco, bairro, ponto_referencia, form_pgmto, tipo_consumo
  ```

**Se Response é vazio ou timeout:**
- Servidor não respondeu
- Verifique se Flask está rodando
- Verifique se MySQL está conectado

---

## ❓ "WhatsApp não abre ou mensagem está errada"

### Diagnóstico
1. Clique em "📱 Enviar WhatsApp"
2. Verifique o alerta

### Soluções

**Se alerta mostra: "✅ Pedido #0 Salvo!"**
- [ ] O ID do pedido é 0 ou undefined (erro de sincronização)
- [ ] Atualize a página e tente novamente
- [ ] Verifique Response da requisição (F12 > Network)

**Se WhatsApp abre mas mensagem está incompleta:**
- [ ] Verifique se todos os campos foram preenchidos
- [ ] Alguns campos podem estar vazios (N/A)
- [ ] Isso é normal, é o campo opcional

**Se WhatsApp não abre:**
- [ ] Verificar número do lojista está correto: `5582981090042`
- [ ] F12 > Console, procure por erro
- [ ] Teste a URL manualmente:
  ```javascript
  console.log(window.location.href)
  ```

### Teste Manual
No console, digite:
```javascript
fetch('/enviar_whatsapp', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        whatsapp_numero: '5582981090042',
        mensagem: 'Teste'
    })
}).then(r => r.json()).then(d => console.log(d))
```

---

## ❓ "Formulário perde dados quando atualizo a página"

### Solução
Isso é **comportamento normal**. O formulário não salva dados entre páginas.

Se quiser persistência:
- Dados são salvos no banco quando clica "Imprimir" ou "Enviar WhatsApp"
- Após salvar, o carrinho é limpo (isso é correto)

---

## ❓ "Recebi erro 500"

### Diagnóstico
1. F12 > Console
2. Procure por erro que começa com "ERROR" ou "500"
3. Copie o erro inteiro

### Soluções

**Erro 500 no /salvar_pedido:**
- [ ] Verifique MySQL está online
- [ ] Verifique se tabela `tbl_detalhes_pedido` existe
- [ ] Verifique se colunas novas existem:
  ```sql
  ALTER TABLE tbl_detalhes_pedido 
  ADD COLUMN IF NOT EXISTS endereco VARCHAR(255),
  ADD COLUMN IF NOT EXISTS bairro VARCHAR(100),
  ADD COLUMN IF NOT EXISTS ponto_referencia VARCHAR(255),
  ADD COLUMN IF NOT EXISTS form_pgmto VARCHAR(50),
  ADD COLUMN IF NOT EXISTS tipo_consumo VARCHAR(50);
  ```

**Erro 500 em /api/produtos:**
- [ ] Verifique se tabela `tbl_prod` existe
- [ ] Verifique se há produtos com `ativo = 1`

---

## ✅ TESTES RÁPIDOS

### Teste 1: Servidor está respondendo?
Console:
```javascript
fetch('http://localhost:5000/api/produtos')
    .then(r => console.log(`Status: ${r.status}`))
```

### Teste 2: Banco de dados está conectado?
Terminal (SSH no servidor):
```bash
mysql -h auth-db1937.hstgr.io -u seu_usuario -p
USE seu_banco;
SELECT COUNT(*) FROM tbl_prod;
```

### Teste 3: Frontend está atualizado?
Console:
```javascript
// Se retorna >0, está OK
document.getElementById('btnAddProduct') ? console.log('✅ OK') : console.log('❌ ERRO')
```

---

## 📞 SE NADA FUNCIONAR

Reúna as seguintes informações e compartilhe:

1. **Screenshot do erro** (F12 > Console)
2. **Qual ação fez:** (ex: Cliquei em "+ Adicionar Produto")
3. **O que esperava:** (ex: Novo campo deveria aparecer)
4. **O que aconteceu:** (ex: Nada aconteceu / Erro apareceu)
5. **Network tab** do F12 (screenshot da requisição que falhou)
6. **Versão do navegador:** (ex: Chrome 120)

Com essas informações, será possível diagnosticar o problema rapidamente.

---

## 🔍 COMANDOS SQL ÚTEIS

### Ver últimos pedidos salvos
```sql
SELECT id_pedido, nome_cliente, endereco, bairro, form_pgmto, tipo_consumo
FROM tbl_detalhes_pedido
ORDER BY id_pedido DESC
LIMIT 10;
```

### Verificar estrutura da tabela
```sql
DESCRIBE tbl_detalhes_pedido;
```

### Limpar pedidos de teste
```sql
DELETE FROM tbl_detalhes_pedido WHERE id_pedido > 100;
DELETE FROM tbl_pedidos WHERE id_pedido > 100;
```

### Verificar quantos produtos estão ativos
```sql
SELECT COUNT(*) as total_ativos 
FROM tbl_prod 
WHERE ativo = 1;
```

---

## 📝 LOG DAS CORREÇÕES

| Data | Problema | Solução |
|------|----------|---------|
| 2024-01-10 | Botão não encontrado | Corrigido ID de 'btn-add-product' para 'btnAddProduct' |
| 2024-01-10 | NameError: endereco undefined | Adicionado 5 campos ao fetch e backend |
| 2024-01-10 | QR Code não atualizava | Resolvido após corrigir fluxo de dados |
| 2024-01-10 | Impressão não salvava | Resolvido após corrigir sincronização |

---

**Última atualização:** 2024-01-10
**Versão:** 1.0
