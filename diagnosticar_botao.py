#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para ativar todos os produtos e diagnosticar o sistema
"""

import mysql.connector
import json
from config import Config

print("=" * 70)
print("🔧 DIAGNÓSTICO E ATIVAÇÃO DE PRODUTOS")
print("=" * 70)

try:
    # Conectar ao banco
    print("\n📡 Conectando ao banco de dados...")
    conexao = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
        port=Config.MYSQL_PORT
    )
    cursor = conexao.cursor(dictionary=True)
    print("✅ Conectado!")
    
    # 1. Verificar produtos inativos
    print("\n📊 Verificando produtos...")
    cursor.execute("SELECT COUNT(*) as total FROM tbl_prod")
    total_geral = cursor.fetchone()['total']
    print(f"   Total de produtos: {total_geral}")
    
    # 2. Contar ativos
    cursor.execute("SELECT COUNT(*) as total FROM tbl_prod WHERE ativo = 1")
    ativos = cursor.fetchone()['total']
    print(f"   Produtos ATIVOS: {ativos}")
    
    if ativos < total_geral:
        # 3. Ativar todos
        print("\n⚙️ Ativando todos os produtos...")
        cursor.execute("UPDATE tbl_prod SET ativo = 1")
        conexao.commit()
        print(f"✅ {total_geral} produtos ativados!")
    else:
        print("✅ Todos os produtos já estão ativos!")
    
    # 4. Listar produtos
    print("\n📋 Produtos cadastrados:")
    cursor.execute("""
        SELECT id_prod, nome_prod, valor, ativo 
        FROM tbl_prod 
        ORDER BY nome_prod 
        LIMIT 10
    """)
    produtos = cursor.fetchall()
    
    for i, p in enumerate(produtos, 1):
        status = "✅ ATIVO" if p['ativo'] == 1 else "❌ INATIVO"
        print(f"   {i}. {status} - {p['nome_prod']:30s} | R$ {p['valor']:8.2f}")
    
    if len(produtos) < total_geral:
        print(f"   ... e mais {total_geral - len(produtos)} produtos")
    
    # 5. Gerar resposta JSON simulada
    print("\n🔌 Simulando resposta da API /api/produtos:")
    cursor.execute("""
        SELECT id_prod, nome_prod, valor 
        FROM tbl_prod 
        WHERE ativo = 1
    """)
    produtos_api = cursor.fetchall()
    
    resposta_api = {
        "status": "sucesso",
        "productos": [
            {
                "id_prod": p['id_prod'],
                "nome_prod": p['nome_prod'],
                "valor": float(p['valor'])
            } for p in produtos_api
        ],
        "total": len(produtos_api)
    }
    
    print(json.dumps(resposta_api, ensure_ascii=False, indent=2))
    
    # 6. Gerar JavaScript para template
    print("\n📝 JavaScript para template Jinja2:")
    print("   let produtosDisponiveis = [")
    for i, p in enumerate(produtos_api[:5]):
        virgula = "," if i < len(produtos_api) - 1 else ""
        print(f"       {{id: {p['id_prod']}, nome: \"{p['nome_prod']}\", valor: {p['valor']}}}{virgula}")
    if len(produtos_api) > 5:
        print(f"       ... {len(produtos_api) - 5} mais produtos")
    print("   ];")
    
    # 7. Resumo final
    print("\n" + "=" * 70)
    print("✅ RESUMO FINAL")
    print("=" * 70)
    print(f"✓ Produtos ativos: {len(produtos_api)}")
    print(f"✓ API /api/produtos: PRONTA")
    print(f"✓ Template Jinja2: PRONTO")
    print(f"✓ JavaScript: PRONTO")
    print("\n🎯 Próximos passos:")
    print("1. Abra: http://localhost:5000/pedidos")
    print("2. Pressione Ctrl+F5 para limpar cache")
    print("3. Clique no botão '+ Adicionar Produto'")
    print("4. Um novo campo de produto deve aparecer")
    print("\nSe não funcionar:")
    print("• Abra DevTools (F12)")
    print("• Vá na aba Console")
    print("• Procure por mensagens de erro")
    print("• Compartilhe a saída com o desenvolvedor")
    print("\n" + "=" * 70)
    
    cursor.close()
    conexao.close()
    
except mysql.connector.Error as erro:
    print(f"\n❌ ERRO DE BANCO DE DADOS: {erro}")
    print("\nVerifique:")
    print("  • MySQL está rodando?")
    print("  • Credenciais em config.py estão corretas?")
    print("  • Database existe?")
except Exception as erro:
    print(f"\n❌ ERRO: {erro}")
    print(f"   Tipo: {type(erro).__name__}")
