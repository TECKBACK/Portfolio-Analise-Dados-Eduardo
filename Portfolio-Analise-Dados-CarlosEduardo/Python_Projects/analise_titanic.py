#==========================================================
# PORTFÓLIO DE ANÁLISE DE DADOS (Python)
# Autor: Eduardo
# Ferramentas: Python, Pandas, Seaborn.
# Contexto: Análise de banco de dados do Titanic
#==========================================================



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# 1. CONFIGURAÇÃO INICIAL, CARREGAMENTO E LIMPEZA
# ==============================================================================

# Configurar estilo dos gráficos
sns.set_theme(style="whitegrid")

# Carregar os dados
url_dados = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
print("--- Lendo dados direto da internet... ---")
df_titanic = pd.read_csv(url_dados)

# --- ETAPA DE LIMPEZA DE DADOS ---
# Preencher idades faltando com a média
media_idade_geral = df_titanic['age'].mean()
df_titanic['age'].fillna(media_idade_geral, inplace=True)

# Remover coluna com muitos dados faltantes
df_titanic.drop('deck', axis=1, inplace=True)

print("Dados carregados e limpos com sucesso!")
print(f"Dimensões do Dataset: {df_titanic.shape[0]} linhas e {df_titanic.shape[1]} colunas.")

# Inspeção Inicial
print("\n--- Primeiras 5 linhas ---")
print(df_titanic.head())
print("\n--- Informações Técnicas ---")
df_titanic.info()


# ==============================================================================
# 2. ANÁLISE ESTATÍSTICA E AGRUPAMENTOS
# ==============================================================================

print("\n" + "="*40)
print("ANÁLISE 1: SOBREVIVÊNCIA POR GÊNERO")
print("="*40)

# Filtros e Contagens
homens_total = df_titanic[df_titanic['sex'] == 'male']
homens_mortos = df_titanic[(df_titanic['sex'] == 'male') & (df_titanic['survived'] == 0)]
mulheres_sobreviventes = df_titanic[(df_titanic['sex'] == 'female') & (df_titanic['survived'] == 1)]

# Cálculos Totais
num_homens_total = homens_total.shape[0]
num_homens_sobreviventes = num_homens_total - homens_mortos.shape[0]
num_mulheres_total = df_titanic[df_titanic['sex'] == 'female'].shape[0]
num_mulheres_sobreviventes_total = mulheres_sobreviventes.shape[0]

# Cálculo de Taxas (%)
taxa_mulheres = (num_mulheres_sobreviventes_total / num_mulheres_total) * 100
taxa_homens = (num_homens_sobreviventes / num_homens_total) * 100

print(f'Total de Homens: {num_homens_total} | Sobreviventes: {num_homens_sobreviventes}')
print(f'Total de Mulheres: {num_mulheres_total} | Sobreviventes: {num_mulheres_sobreviventes_total}')
print(f'\n--- TAXAS DE SOBREVIVÊNCIA ---')
print(f'Mulheres: {taxa_mulheres:.2f}%')
print(f'Homens:   {taxa_homens:.2f}%')
print('CONCLUSÃO: A regra "mulheres e crianças primeiro" parece ter sido seguida.')


print("\n" + "="*40)
print("ANÁLISE 2: PERFIL POR CLASSE (GROUP BY)")
print("="*40)

# Média de idade e tarifa por classe
medias_por_classe = df_titanic.groupby('pclass')[['age', 'fare']].mean()
print("--- Médias por Classe (Idade e Tarifa) ---")
print(medias_por_classe)

# Idade mínima e máxima por sexo
print("\n--- Idade Mínima e Máxima por Sexo ---")
idades_extremas = df_titanic.groupby('sex')['age'].agg(['min', 'max'])
print(idades_extremas)


# ==============================================================================
# 3. VISUALIZAÇÃO DE DADOS (GRÁFICOS)
# ==============================================================================

# Gráfico 1: Distribuição de Idades
plt.figure(figsize=(8, 5))
sns.histplot(data=df_titanic, x="age", kde=True)
plt.title('Distribuição de Idades no Titanic')
plt.xlabel('Idade')
plt.ylabel('Contagem de Pessoas')
plt.show()

# Gráfico 2: Distribuição de Tarifas
plt.figure(figsize=(8, 5))
sns.histplot(data=df_titanic, x="fare", bins=50, kde=False, color='green')
plt.title('Distribuição de Tarifas no Titanic')
plt.xlabel('Tarifa Paga')
plt.ylabel('Contagem')
plt.show()

# Gráfico 3: Sobrevivência por Gênero (Barras)
plt.figure(figsize=(6, 5))
sns.countplot(data=df_titanic, x='sex', hue='survived', palette='coolwarm')
plt.title('Contagem de Sobreviventes por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem de Pessoas')
plt.legend(title='Sobreviveu?', labels=['Não', 'Sim'])
plt.show()

# Gráfico 4: Relação Idade vs Tarifa vs Classe (Dispersão)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_titanic, x='age', y='fare', hue='pclass', palette='viridis', alpha=0.7)
plt.title('Relação: Idade x Tarifa x Classe')
plt.xlabel('Idade')
plt.ylabel('Tarifa Paga')
plt.legend(title='Classe')
plt.show()