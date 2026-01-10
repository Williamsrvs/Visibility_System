#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste rápido para verificar produtos e endpoints
"""

import requests
import json

BASE_URL = "http://localhost:5000"

print("=" * 70)
print("🧪 TESTE RÁPIDO - Sistema de Pedidos")
print("=" * 70)

# Teste 1: Verificar rota /api/produtos
print("\n📡 Teste 1: Endpoint /api/produtos")
print("-" * 70)

try:
    response = requests.get(f"{BASE_URL}/api/produtos", timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {response.status_code}")
        print(f"   Total de produtos: {data.get('total', 0)}")
        
        if data.get('produtos'):
            print(f"\n   Primeiros produtos:")
            for prod in data['produtos'][:3]:
                print(f"   - {prod['nome_prod']} - R$ {prod['valor']}")
        else:
            print("   ❌ Nenhum produto encontrado")
    else:
        print(f"❌ Status: {response.status_code}")
        print(f"   Resposta: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("❌ Erro: Não foi possível conectar")
    print("   Certifique-se de que o Flask está rodando")
except Exception as e:
    print(f"❌ Erro: {str(e)}")

# Teste 2: Verificar rota /pedidos
print("\n\n📡 Teste 2: Página /pedidos")
print("-" * 70)

try:
    response = requests.get(f"{BASE_URL}/pedidos", timeout=5)
    
    if response.status_code == 200:
        print(f"✅ Status: {response.status_code}")
        
        # Verificar se contém produtos no HTML
        if 'produtosDisponiveis' in response.text:
            print("✅ Página contém 'produtosDisponiveis'")
            
            # Contar produtos no array
            inicio = response.text.find('produtosDisponiveis = [')
            if inicio > 0:
                fim = response.text.find('];', inicio)
                array_str = response.text[inicio:fim]
                count = array_str.count('{ id:')
                print(f"   Produtos no template: {count}")
        else:
            print("❌ Página NÃO contém 'produtosDisponiveis'")
    else:
        print(f"❌ Status: {response.status_code}")
        
except Exception as e:
    print(f"❌ Erro: {str(e)}")

print("\n" + "=" * 70)
print("📋 RESUMO")
print("=" * 70)
print("\nSe ambos os testes passaram:")
print("✅ O sistema deve funcionar corretamente")
print("✅ Clique em '+ Adicionar Produto'")
print("✅ Selecione um produto do dropdown")
print("\nSe há erro no /api/produtos:")
print("❌ Verifique se há produtos com ativo=1 no banco")
print("❌ Vá para http://localhost:5000/produto e cadastre produtos")

print()
