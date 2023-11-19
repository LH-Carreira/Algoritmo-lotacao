import pandas as pd
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_planilha = os.path.join(diretorio_atual, 'prof.xlsx')
# Carregue a planilha original
planilha_original = pd.read_excel(caminho_planilha)

# Filtrar as linhas com base em uma condição
condicao_filtro = planilha_original[' COD_DISCPLINA'] == 2002
linhas_filtradas = planilha_original[condicao_filtro]

# Salvar as linhas filtradas em uma nova planilha
linhas_filtradas.to_excel(diretorio_atual+'planilha.xlsx', index=False)
