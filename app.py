#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arquivo principal da aplicação Flask
Point of entry para executar o servidor
"""

import os
import sys

# Adicionar o diretório app ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from routes import app, criar_tabelas

if __name__ == '__main__':
    # Criar tabelas ao iniciar
    criar_tabelas()
    
    # Determinar ambiente (desenvolvimento ou produção)
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print("\n" + "="*60)
    print("🚀 Iniciando Catálogo Digital")
    print("="*60)
    print(f"Ambiente: {'DESENVOLVIMENTO' if debug_mode else 'PRODUÇÃO'}")
    print(f"Servidor: http://{host}:{port}")
    print("="*60 + "\n")
    
    # Executar aplicação
    app.run(
        host=host,
        port=port,
        debug=debug_mode,
        use_reloader=debug_mode
    )
