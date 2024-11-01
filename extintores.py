# -*- coding: utf-8 -*-
"""Extintores.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y3TsppFjP91f2eEv8UN92iJdcpTQR_9Y
"""

import openpyxl
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
# ... (importar outras bibliotecas se necessário)

def ler_dados_excel(arquivo):
    # Carrega o arquivo Excel
    workbook = openpyxl.load_workbook(arquivo)
    sheet = workbook.active

    # Lê os dados das linhas, pulando o cabeçalho
    dados_extintores = []
    for row in sheet.iter_rows(min_row=2):
        dados_extintores.append({
            'numero_serie': row[0].value,
            'localizacao': row[1].value,
            'data_fabricacao': row[2].value,
            'data_vencimento': row[3].value
        })
    return dados_extintores

def verificar_vencimento(dados_extintores):
    hoje = datetime.now().date()
    extintores_vencidos = []
    extintores_proximos = []

    for extintor in dados_extintores:
        data_vencimento = extintor['data_vencimento']
        if data_vencimento <= hoje:
            extintores_vencidos.append(extintor)
        elif data_vencimento <= hoje + timedelta(days=30):
            extintores_proximos.append(extintor)

    return extentores_vencidos, extentores_proximos

def gerar_relatorio(extintores_vencidos, extentores_proximos):
    # Imprime ou salva um relatório em um arquivo com os dados dos extintores
    # ...

 def enviar_notificacao(extintores_vencidos, extentores_proximos):
    # Envia um email ou SMS para os responsáveis
    # ...

# Nome do arquivo Excel
  arquivo_excel = 'Fulanodetal.xlsx'

# Lendo os dados do Excel
 dados = ler_dados_excel(arquivo_excel)

# Verificando o vencimento
 vencidos, proximos = verificar_vencimento(dados)

# Gerando relatório
 gerar_relatorio(vencidos, proximos)

# Enviando notificações
 enviar_notificacao(vencidos, proximos)