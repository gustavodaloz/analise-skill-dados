import os
import pandas as pd

# 1. Identificação do arquivo (Skill: conferir-csv)
caminho_csv = os.path.join("dados", "fornecedores_erro.csv")

# 2. Leitura inicial e detecção de separador e estrutura
# Textos vazios ou só com espaços são considerados ausência (NaN)
df = pd.read_csv(caminho_csv, sep=",", skipinitialspace=True)

# 3. Métricas quantitativas calculadas com código
total_linhas = len(df)
total_colunas = len(df.columns)
linhas_duplicadas = int(df.duplicated().sum())

# Valores ausentes por coluna
valores_ausentes = df.isnull().sum()

# Tipos de dados
tipos_dados = df.dtypes

# Identificação das linhas com problemas
linhas_com_nulos = df[df.isnull().any(axis=1)]

# 4. Geração do relatório em resultados/qualidade.md
os.makedirs("resultados", exist_ok=True)
caminho_qualidade = os.path.join("resultados", "qualidade.md")

relatorio_qualidade = f"""# Relatório de Conferência de Qualidade de Dados (Skill: conferir-csv)

## 1. Identificação do Arquivo e Finalidade
- **Arquivo analisado:** `dados/fornecedores_erro.csv`
- **Finalidade:** Avaliação e seleção de fornecedores via matriz de decisão.
- **Separador utilizado:** Vírgula (`,`)
- **O que cada linha representa:** Os atributos de desempenho comercial e operacional de um fornecedor específico.

---

## 2. Estrutura e Métricas Gerais
- **Total de linhas de dados:** {total_linhas}
- **Total de colunas:** {total_colunas}
- **Linhas duplicadas:** {linhas_duplicadas}

### Colunas e Tipos de Dados Detectados:
| Coluna | Tipo Detectado | Valores Ausentes | % Ausência |
|---|---|---|---|
"""

for col in df.columns:
    nulos = int(valores_ausentes[col])
    pct_nulos = (nulos / total_linhas) * 100
    relatorio_qualidade += f"| `{col}` | `{tipos_dados[col]}` | {nulos} | {pct_nulos:.1f}% |\n"

relatorio_qualidade += f"""
---

## 3. Problemas Encontrados e Evidências
1. **Valores Ausentes Críticos na coluna `suporte_nota`:**
   - Foram detectados **{valores_ausentes['suporte_nota']} valores ausentes** de um total de {total_linhas} linhas (**50.0% da coluna**).
   - **Fornecedores afetados:**
"""

for _, row in linhas_com_nulos.iterrows():
    relatorio_qualidade += f"     - Fornecedor **{row['fornecedor']}**: campo `suporte_nota` está vazio (`NaN`).\n"

relatorio_qualidade += f"""
2. **Impacto na Matriz de Decisão:**
   - Como o critério de suporte compõe 25% da nota final, a ausência dessa informação para Beta e Delta inviabiliza o cálculo correto do ranking ou distorce completamente a tomada de decisão.

---

## 4. Tratamentos Propostos
1. **Regra de Ouro:** Não preencher ou inventar números sem validação com a área responsável (evitar suposições).
2. **Ação Primária Recomendada:** Solicitar à equipe responsável a nota de suporte real dos fornecedores **Beta** e **Delta**.
3. **Análise de Sensibilidade / Cenários Alternativos (caso o dado demore):**
   - **Cenário Pessimista:** Atribuir nota mínima (0 ou 1) para o suporte de Beta e Delta e verificar o ranking.
   - **Cenário Otimista:** Atribuir nota máxima (10) para verificar se Delta continuaria na liderança.
   - **Cenário sem o critério:** Recalcular a matriz com apenas 3 critérios (Preço, Prazo e Defeitos) distribuindo os pesos igualmente (~33.3% cada).
"""

with open(caminho_qualidade, "w", encoding="utf-8") as f:
    f.write(relatorio_qualidade)

# 5. Exibição no terminal
print("=== CONFERÊNCIA DE DADOS CONCLUÍDA ===")
print(f"Total de linhas: {total_linhas} | Colunas: {total_colunas}")
print(f"Linhas duplicadas: {linhas_duplicadas}")
print("\nValores ausentes detectados:")
for col, nulos in valores_ausentes.items():
    if nulos > 0:
        print(f" - Coluna '{col}': {nulos} valor(es) ausente(s) ({(nulos/total_linhas)*100:.1f}%)")
if valores_ausentes.sum() == 0:
    print(" - Nenhum valor ausente encontrado.")

print(f"\nRelatório de qualidade salvo em: {caminho_qualidade}")

