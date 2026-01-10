#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar se a rota /pedidos está retornando produtos
"""

import requests
import json
from datetime import datetime

# Configurar a URL
BASE_URL = "http://localhost:5000"
ENDPOINT = "/pedidos"

print("=" * 60)
print("🧪 TESTE: Verificar se /pedidos retorna produtos")
print("=" * 60)
print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print()

try:
    # Fazer requisição
    print(f"📡 Conectando em: {BASE_URL}{ENDPOINT}")
    response = requests.get(f"{BASE_URL}{ENDPOINT}", timeout=5)
    
    print(f"✅ Conexão estabelecida!")
    print(f"📊 Status Code: {response.status_code}")
    print()
    
    if response.status_code == 200:
        print("✅ Página carregou com sucesso!")
        print()
        
        # Verificar se contém produtos
        html = response.text
        
        if 'produtosDisponiveis = [' in html:
            print("✅ Encontrado: 'produtosDisponiveis = ['")
            
            # Extrair a parte do array
            inicio = html.find('produtosDisponiveis = [') + len('produtosDisponiveis = [')
            fim = html.find('];', inicio)
            
            if fim > inicio:
                array_str = html[inicio:fim]
                
                # Contar quantos produtos
                produto_count = array_str.count('{ id:')
                print(f"📦 Total de produtos encontrados: {produto_count}")
                
                if produto_count == 0:
                    print("\n⚠️ AVISO: Array de produtos está vazio!")
                    print("\nPrimeiros 200 caracteres do array:")
                    print(array_str[:200])
                else:
                    print(f"\n✅ Array contém {produto_count} produto(s)")
            else:
                print("⚠️ Não foi possível encontrar o fechamento do array")
        else:
            print("❌ Não encontrado: 'produtosDisponiveis = ['")
            print("\nVerifique se a variável está no HTML")
        
        print("\n" + "=" * 60)
        print("CONCLUSÃO:")
        print("=" * 60)
        
        if 'produtosDisponiveis = [' in html and html[inicio:fim].count('{ id:') > 0:
            print("✅ TUDO OK! Os produtos estão sendo carregados corretamente.")
        else:
            print("❌ PROBLEMA: Os produtos NÃO estão sendo carregados.")
            print("\nPossíveis causas:")
            print("1. A tabela tbl_prod não tem produtos com ativo=1")
            print("2. A conexão com o banco de dados está falhando")
            print("3. O template Jinja2 não está iterando sobre 'produtos'")
            
    else:
        print(f"❌ Erro HTTP: {response.status_code}")
        
except requests.exceptions.ConnectionError:
    print(f"❌ Erro: Não foi possível conectar em {BASE_URL}")
    print("\nVerifique se:")
    print("1. A aplicação Flask está rodando")
    print("2. A porta 5000 está correta")
    print("3. Não há firewall bloqueando a conexão")
    
except requests.exceptions.Timeout:
    print(f"❌ Erro: Timeout ao conectar em {BASE_URL}")
    
except Exception as e:
    print(f"❌ Erro: {type(e).__name__}: {str(e)}")

print()
