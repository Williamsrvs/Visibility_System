#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para adicionar coluna 'ativo' na tabela tbl_prod
para implementar soft delete sem quebrar referências de chaves estrangeiras
"""

import mysql.connector
from config import db_config
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Conectar ao banco
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    
    logging.info("✅ Conectado ao banco de dados")
    
    # Verificar se a coluna já existe
    cur.execute("""
        SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'tbl_prod' AND COLUMN_NAME = 'ativo'
    """)
    
    if cur.fetchone():
        logging.info("⚠️ Coluna 'ativo' já existe na tabela tbl_prod")
    else:
        # Adicionar coluna se não existir
        cur.execute("""
            ALTER TABLE tbl_prod 
            ADD COLUMN ativo TINYINT DEFAULT 1 
            AFTER imagem_url
        """)
        conn.commit()
        logging.info("✅ Coluna 'ativo' adicionada com sucesso")
        
        # Verificar quantos produtos foram marcados como ativos
        cur.execute("SELECT COUNT(*) as total FROM tbl_prod WHERE ativo = 1")
        total = cur.fetchone()[0]
        logging.info(f"📊 {total} produtos estão ativos")
    
    cur.close()
    conn.close()
    logging.info("✅ Script executado com sucesso!")
    
except mysql.connector.Error as err:
    if err.errno == 1054:
        logging.error("❌ Erro: Coluna já existe ou banco não conectado")
    else:
        logging.error(f"❌ Erro no banco de dados: {err}")
except Exception as e:
    logging.error(f"❌ Erro inesperado: {e}")
