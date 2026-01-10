#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor de teste simples - sem reloader para evitar problemas no Windows
"""
import sys
import os

# Adicionar o diretório app ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from routes import app

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Iniciando Servidor de Teste")
    print("="*60)
    print("🌐 URL: http://localhost:5000")
    print("📍 Rota de testes: /pedidos_cliente")
    print("="*60 + "\n")
    
    # Rodar sem reloader para evitar problemas de socket no Windows
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False,  # Desabilitar debug
        use_reloader=False  # Desabilitar reloader
    )
