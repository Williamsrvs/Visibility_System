# 🔧 Configuração do PIX - Catálogo Digital

## 📋 Passos para Configurar o Gerador de QR Code PIX

### 1️⃣ Localizar o Arquivo
Abra o arquivo: **`app/templates/pedidos.html`**

### 2️⃣ Encontrar a Seção de Configuração
Procure por estas linhas (por volta da linha 1065-1067):

```javascript
// ⚠️ CONFIGURAÇÃO: Chave PIX do recebedor
const CHAVE_PIX = '00000000000000000000000'; // Altere para sua chave PIX (CPF, CNPJ, email ou telefone)
const NOME_BENEFICIARIO = 'NOME DO LOJISTA'; // Altere para seu nome/razão social
```

### 3️⃣ Configurar Sua Chave PIX

Substitua o valor de **CHAVE_PIX** com uma das opções:

| Tipo | Exemplo | 
|------|---------|
| **CPF** | `12345678900` |
| **CNPJ** | `12345678000195` |
| **Email** | `seu.email@example.com` |
| **Telefone** | `5582987654321` (código país + DDD + número) |
| **Chave Aleatória** | (fornecida pelo seu banco) |

**Exemplo de configuração:**
```javascript
const CHAVE_PIX = '82987654321'; // CPF do lojista
const NOME_BENEFICIARIO = 'LANCHONETE DELICIA'; // Nome da empresa/pessoa
```

### 4️⃣ Encontrar Sua Chave PIX

**No seu banco:**
1. Acesse o app do seu banco
2. Procure por **PIX** > **Minhas Chaves**
3. Selecione uma das chaves cadastradas (ou crie uma nova)

**Para novo cadastro:**
- Abra o aplicativo do seu banco
- Vá em **PIX** > **Minhas Chaves** > **Criar nova chave**
- Escolha o tipo (CPF, CNPJ, Email ou Telefone)

---

## ✅ Como Funciona Agora

### Alterações Implementadas:

1. **✅ Botão de Adicionar Produto - CORRIGIDO**
   - Agora funciona corretamente ao clicar
   - Permite adicionar múltiplos produtos ao carrinho

2. **✅ QR Code PIX - IMPLEMENTADO**
   - Ao adicionar produtos, um QR Code é gerado automaticamente
   - O QR Code aparece no painel direito (Resumo do Pedido)
   - Mostra a chave PIX em formato de "Cópia e Cola" para transferência manual

3. **✅ Painel de Informações do Cliente - MELHORADO**
   - Campo "Ponto de Referência" corrigido (tinha ID duplicado)
   - Todos os campos agora funcionam corretamente:
     - Endereço
     - Bairro
     - Ponto de Referência
     - Forma de Pagamento
     - Tipo de Consumo

---

## 🧪 Testando a Funcionalidade

1. **Adicionar Produto:**
   - Clique em **"+ Adicionar Produto"**
   - Selecione um produto do dropdown
   - Digite a quantidade
   - O preço será preenchido automaticamente
   - Clique em **"Adicionar ao Pedido"**

2. **QR Code PIX:**
   - Conforme adicionar produtos, o valor total é atualizado no resumo
   - Um **QR Code PIX** aparecerá automaticamente
   - A **chave PIX** estará disponível em formato de cópia e cola

3. **Enviar via WhatsApp:**
   - Preencha os dados do cliente
   - Clique em **"📱 Enviar via WhatsApp"**
   - Uma mensagem será preparada com todos os dados do pedido

4. **Imprimir Pedido:**
   - Clique em **"🖨️ Imprimir Pedido"**
   - O pedido será salvo no banco de dados
   - Uma janela de impressão será aberta

---

## ⚠️ Importante

- A **chave PIX** deve estar **cadastrada e ativa** no seu banco
- O **QR Code gerado** é válido apenas para a chave PIX configurada
- Sempre confira os dados antes de confirmar um pedido

---

## 🆘 Problemas Comuns

### "QR Code não aparece"
- ✅ Verifique se a chave PIX foi configurada corretamente
- ✅ Verifique se adicionou produtos ao carrinho (valor deve ser > 0)

### "Botão de adicionar não funciona"
- ✅ A correção foi feita no arquivo. Atualize o navegador (Ctrl + F5)

### "Chave PIX não funciona"
- ✅ Verifique se a chave está cadastrada no seu banco
- ✅ Verifique a formatação (sem espaços ou caracteres especiais)

---

## 📞 Suporte

Para mais informações sobre PIX, visite: https://www.bcb.gov.br/pix

---

**Última atualização:** 10 de janeiro de 2026
