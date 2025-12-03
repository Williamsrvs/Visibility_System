#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir a estrutura da tabela tbl_pedidos
Adiciona as colunas faltantes: valor_total e status_pedido
"""

import mysql.connector
from mysql.connector import Error
import sys

# Configuração do banco de dados
db_config = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'u799109175_menu_prod',
    'password': 'Q1k2v1y5@2025',  
    'database': 'u799109175_menu_prod',  
    'port': 3306
}

def conectar_banco():
    """Conecta ao banco de dados"""
    try:
        conexao = mysql.connector.connect(**db_config)
        if conexao.is_connected():
            print("✅ Conectado ao banco de dados com sucesso!")
            return conexao
    except Error as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        sys.exit(1)

def verificar_colunas(cursor):
    """Verifica quais colunas existem na tabela tbl_pedidos"""
    try:
        cursor.execute("DESCRIBE u799109175_menu_prod.tbl_pedidos;")
        colunas = cursor.fetchall()
        nomes_colunas = [col[0] for col in colunas]
        
        print("\n📊 Colunas existentes em tbl_pedidos:")
        for col in nomes_colunas:
            print(f"   ✓ {col}")
        
        return nomes_colunas
    except Error as e:
        print(f"❌ Erro ao verificar colunas: {e}")
        return []

def adicionar_coluna(cursor, nome_coluna, definicao):
    """Adiciona uma coluna à tabela se ela não existir"""
    try:
        cursor.execute(f"""
            ALTER TABLE u799109175_menu_prod.tbl_pedidos
            ADD COLUMN {nome_coluna} {definicao}
        """)
        print(f"✅ Coluna '{nome_coluna}' adicionada com sucesso!")
        return True
    except Error as e:
        if "Duplicate column name" in str(e):
            print(f"⚠️  Coluna '{nome_coluna}' já existe, pulando...")
            return False
        else:
            print(f"❌ Erro ao adicionar coluna '{nome_coluna}': {e}")
            raise

def main():
    print("=" * 60)
    print("🔧 Ferramenta de Correção do Banco de Dados")
    print("=" * 60)
    
    # Conectar ao banco
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # Verificar colunas existentes
        colunas_existentes = verificar_colunas(cursor)
        
        print("\n🔍 Verificando colunas faltantes...")
        colunas_necessarias = {
            'valor_total': 'DECIMAL(10,2)',
            'status_pedido': "VARCHAR(50) DEFAULT 'pendente'"
        }
        
        colunas_faltantes = {}
        for coluna, definicao in colunas_necessarias.items():
            if coluna not in colunas_existentes:
                colunas_faltantes[coluna] = definicao
        
        if colunas_faltantes:
            print(f"\n⚠️  Colunas faltantes encontradas:")
            for coluna in colunas_faltantes:
                print(f"   ✗ {coluna}")
            
            print("\n➕ Adicionando colunas faltantes...")
            for coluna, definicao in colunas_faltantes.items():
                adicionar_coluna(cursor, coluna, definicao)
            
            # Confirmar mudanças
            conexao.commit()
            print("\n✅ Todas as colunas foram adicionadas com sucesso!")
        else:
            print("\n✅ Todas as colunas necessárias já existem!")
        
        # Verificar novamente
        print("\n📊 Estrutura final de tbl_pedidos:")
        verificar_colunas(cursor)
        
        print("\n" + "=" * 60)
        print("✅ Banco de dados corrigido com sucesso!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        conexao.rollback()
        sys.exit(1)
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    main()
