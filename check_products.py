#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se a rota /pedidos_cliente está funcionando
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from config import db_config
import mysql.connector

print("="*60)
print("🔍 TESTE DE CONEXÃO E PRODUTOS")
print("="*60)

print(f"\n📡 Configuração de conexão:")
print(f"   Host: {db_config['host']}")
print(f"   User: {db_config['user']}")
print(f"   Database: {db_config['database']}")
print(f"   Port: {db_config['port']}")

try:
    print("\n⏳ Conectando ao banco de dados...")
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        port=db_config['port']
    )
    
    print("✅ Conexão bem-sucedida!")
    
    cur = conn.cursor(dictionary=True)
    
    # Teste 1: Verificar produtos ativos
    print("\n📦 TESTE 1: Produtos ativos")
    cur.execute("SELECT COUNT(*) as total FROM tbl_prod WHERE ativo = 1")
    result = cur.fetchone()
    total = result['total'] if result else 0
    print(f"   Total de produtos ativos: {total}")
    
    # Teste 2: Buscar 5 primeiros produtos (como a rota faz)
    print("\n📦 TESTE 2: Estrutura de dados retornada pela rota")
    cur.execute("SELECT id_prod, nome_prod, valor FROM tbl_prod WHERE ativo = 1 ORDER BY nome_prod ASC LIMIT 5")
    produtos = cur.fetchall()
    
    if produtos:
        print(f"   Encontrados {len(produtos)} produtos")
        for i, p in enumerate(produtos, 1):
            print(f"\n   Produto {i}:")
            print(f"     - id_prod: {p['id_prod']}")
            print(f"     - nome_prod: {p['nome_prod']}")
            print(f"     - valor: {p['valor']}")
    else:
        print("   ⚠️ Nenhum produto ativo encontrado!")
    
    # Teste 3: Verificar clientes
    print("\n👥 TESTE 3: Clientes")
    cur.execute("SELECT COUNT(*) as total FROM tbl_cliente")
    result = cur.fetchone()
    total_clientes = result['total'] if result else 0
    print(f"   Total de clientes: {total_clientes}")
    
    cur.close()
    conn.close()
    
    print("\n" + "="*60)
    print("✅ TUDO OK! A rota /pedidos_cliente deve funcionar")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ ERRO DE CONEXÃO: {e}")
    print("\n💡 Possíveis soluções:")
    print("   1. Verificar se o banco de dados está online")
    print("   2. Verificar as credenciais em config.py")
    print("   3. Verificar se as tabelas tbl_prod e tbl_cliente existem")
    
    import traceback
    traceback.print_exc()
