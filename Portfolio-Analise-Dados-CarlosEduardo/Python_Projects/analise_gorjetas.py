#==========================================================
# PORTFÓLIO DE ANÁLISE DE DADOS (Python)
# Autor: Eduardo
# Ferramentas: Python, Pandas, Seaborn.
# Contexto: Análise de banco de dados de um restaurante
#==========================================================



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# 1. CONFIGURAÇÃO INICIAL E CARREGAMENTO
# ==============================================================================

# Carregar o dataset
url_tips = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df_tips = pd.read_csv(url_tips)

# Configurar o estilo do Seaborn
sns.set_theme(style="whitegrid")

print("--- Dataset 'Tips' Carregado ---")

# Inspeção inicial dos dados (Movido para o início para melhor organização)
print("\n--- Informações do Dataset ---")
df_tips.info()
print("\n--- Primeiras 5 linhas ---")
print(df_tips.head())

# ==============================================================================
# 2. ANÁLISE DE NEGÓCIO
# ==============================================================================

# ------------------------------------------------------------------------------
# PERGUNTA 1: Qual dia da semana dá mais faturamento?
# ------------------------------------------------------------------------------
print("\n--- Análise 1: Faturamento por Dia ---")

# Agrupar por dia e somar as colunas numéricas
diamaislucro = df_tips.groupby('day').sum(numeric_only=True)

# Encontrar o valor máximo e o dia correspondente
valor_maximo = diamaislucro['total_bill'].max()
dia_com_maior_lucro_nome = diamaislucro['total_bill'].idxmax()

print(f"Maior faturamento: R${valor_maximo:.2f} no dia {dia_com_maior_lucro_nome}")

# Gráfico: Faturamento por dia
plt.figure(figsize=(8, 5)) # Define um tamanho para o gráfico
sns.barplot(data=diamaislucro, x='total_bill', y=diamaislucro.index, orient='h', palette='viridis')
plt.title('Faturamento total por dia da semana')
plt.xlabel('Total faturado (R$)')
plt.ylabel('Dia da semana')
plt.show()


# ------------------------------------------------------------------------------
# PERGUNTA 2: Existe uma relação entre o valor total da conta e a gorjeta?
# ------------------------------------------------------------------------------
print("\n--- Análise 2: Relação Conta vs Gorjeta ---")

# Gráfico: Dispersão (Scatterplot)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip")
plt.title('Relação entre Total da Conta e Gorjeta')
plt.xlabel('Total da conta (R$)')
plt.ylabel('Gorjeta')
plt.show()

print("Resposta: Gráfico com alinhamento positivo, indicando que existe relação.")


# ------------------------------------------------------------------------------
# PERGUNTA 3: Jantar vs Almoço - Quem dá melhores gorjetas?
# ------------------------------------------------------------------------------
print("\n--- Análise 3: Gorjetas no Almoço vs Jantar ---")

# Calcular a média de gorjetas por horário
jantarmediatip = df_tips.groupby('time')['tip'].mean() # Especifiquei a coluna 'tip' para limpar a saída
print(f'Média de gorjetas:\n{jantarmediatip}')

# Gráfico: Comparação de médias
plt.figure(figsize=(6, 5))
sns.barplot(data=df_tips, x="time", y="tip", palette="muted")
plt.title('Média de Gorjeta: Almoço vs Jantar')
plt.xlabel('Período')
plt.ylabel('Média da Gorjeta')
plt.show()

print("Resposta: A gorjeta é, em média, ligeiramente maior no jantar.")


# ------------------------------------------------------------------------------
# PERGUNTA 4: Fumadores gastam mais?
# ------------------------------------------------------------------------------
print("\n--- Análise 4: Gastos de Fumadores vs Não Fumadores ---")

# Calcular a média de gasto total por condição de fumador
fumantes = df_tips.groupby('smoker')['total_bill'].mean()
print(f'Média de gastos:\n{fumantes}')

# Gráfico: Comparação de gastos
plt.figure(figsize=(6, 5))
sns.barplot(data=df_tips, x="smoker", y="total_bill", palette="pastel")
plt.title('Gasto Médio: Fumador vs Não Fumador')
plt.xlabel('Fumador')
plt.ylabel('Total da Conta (Média)')
plt.show()

print("Resposta: A conta é maior quando o cliente é fumador.")