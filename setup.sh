#!/bin/bash

# Script de Setup Rápido - Catálogo Digital
# Execute: bash setup.sh

set -e  # Para na primeira falha

echo "======================================"
echo "🚀 Setup Catálogo Digital"
echo "======================================"
echo ""

# 1. Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# 2. Ativar ambiente
echo "✅ Ativando ambiente virtual..."
source venv/bin/activate

# 3. Instalar dependências
echo "📥 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Criar arquivo .env
if [ ! -f .env ]; then
    echo "📝 Criando arquivo .env..."
    cp .env.example .env
    echo "⚠️  Edite o arquivo .env com suas credenciais!"
else
    echo "✅ Arquivo .env já existe"
fi

# 5. Criar pasta de uploads
echo "📁 Criando pastas necessárias..."
mkdir -p app/static/uploads
chmod 755 app/static/uploads

# 6. Resumo
echo ""
echo "======================================"
echo "✅ Setup Concluído!"
echo "======================================"
echo ""
echo "📋 Próximos passos:"
echo "1. Edite o arquivo .env com suas credenciais"
echo "2. Execute o schema do banco: mysql < app/schema.sql"
echo "3. Inicie o servidor: python app.py"
echo ""
echo "🌐 Acesse: http://localhost:5000"
echo ""
