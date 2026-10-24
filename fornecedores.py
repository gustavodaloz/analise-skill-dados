import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Leitura dos dados originais
caminho_dados = os.path.join("dados", "fornecedores.csv")
df = pd.read_csv(caminho_dados)

# 2. Definição dos pesos
pesos = {
    "preco_unitario": 0.25,
    "prazo_dias": 0.25,
    "defeitos_pct": 0.25,
    "suporte_nota": 0.25
}

# 3. Normalização das notas (escala de 1 a 10)
melhor_preco = df["preco_unitario"].min()
melhor_prazo = df["prazo_dias"].min()
melhor_defeito = df["defeitos_pct"].min()
melhor_suporte = df["suporte_nota"].max()

df_scores = pd.DataFrame()
df_scores["fornecedor"] = df["fornecedor"]

df_scores["score_preco"] = 10.0 * (melhor_preco / df["preco_unitario"])
df_scores["score_prazo"] = 10.0 * (melhor_prazo / df["prazo_dias"])
df_scores["score_qualidade"] = 10.0 * (melhor_defeito / df["defeitos_pct"])
df_scores["score_suporte"] = 10.0 * (df["suporte_nota"] / melhor_suporte)

df_scores["score_total"] = (
    df_scores["score_preco"] * pesos["preco_unitario"] +
    df_scores["score_prazo"] * pesos["prazo_dias"] +
    df_scores["score_qualidade"] * pesos["defeitos_pct"] +
    df_scores["score_suporte"] * pesos["suporte_nota"]
)

df_ranking = df_scores.sort_values(by="score_total", ascending=False).reset_index(drop=True)
vencedor = df_ranking.iloc[0]

os.makedirs("resultados", exist_ok=True)

# Paleta Cibernética / Futurista Neon
cores_neon = {
    "Delta": "#00f5d4",   # Neon Mint / Ciano (Vencedor)
    "Beta":  "#a855f7",   # Neon Purple
    "Alfa":  "#38bdf8",   # Cyber Sky Blue
    "Gama":  "#f43f5e"    # Neon Pink / Red
}

cor_fundo = "#0b0f19"
cor_card = "#111827"
cor_grid = "#1e293b"
cor_texto = "#f1f5f9"
cor_subtexto = "#94a3b8"

# ==============================================================================
# GRÁFICO 1: Painel Duplo Futurista (Ranking Geral + Critérios)
# ==============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.5), dpi=300, facecolor=cor_fundo)
ax1.set_facecolor(cor_fundo)
ax2.set_facecolor(cor_fundo)

# Subplot 1: Barras Horizontais com Glow
barras_cores = [cores_neon[f] for f in df_ranking["fornecedor"]]
barras = ax1.barh(df_ranking["fornecedor"], df_ranking["score_total"], color=barras_cores, height=0.5, edgecolor="#ffffff", linewidth=0.6)
ax1.set_xlim(0, 11)
ax1.set_xlabel("PONTUAÇÃO FINAL PONDERADA (0 a 10)", color=cor_subtexto, fontsize=10, fontweight="bold", labelpad=8)
ax1.set_title("/// DECISION MATRIX: SCORE GERAL ///", color="#00f5d4", fontsize=12, fontweight="bold", pad=14, loc="left")
ax1.tick_params(colors=cor_subtexto, labelsize=10)
for spine in ax1.spines.values():
    spine.set_color(cor_grid)
ax1.grid(axis="x", linestyle="--", color=cor_grid, alpha=0.9)

for barra in barras:
    w = barra.get_width()
    ax1.text(w + 0.25, barra.get_y() + barra.get_height() / 2, f"{w:.2f} PTS",
             va="center", ha="left", fontsize=10, fontweight="bold", color=cor_texto)

# Subplot 2: Comparativo Detalhado por Critério
criterios = ["PREÇO", "PRAZO", "QUALIDADE", "SUPORTE"]
indices = np.arange(len(criterios))
largura = 0.18

for i, forn in enumerate(df["fornecedor"]):
    linha = df_scores[df_scores["fornecedor"] == forn].iloc[0]
    valores = [
        linha["score_preco"],
        linha["score_prazo"],
        linha["score_qualidade"],
        linha["score_suporte"]
    ]
    ax2.bar(indices + i * largura, valores, width=largura, label=forn,
            color=cores_neon[forn], edgecolor="#0b0f19", linewidth=0.8)

ax2.set_xticks(indices + largura * 1.5)
ax2.set_xticklabels(criterios, color=cor_subtexto, fontsize=10, fontweight="bold")
ax2.set_ylim(0, 11)
ax2.set_ylabel("NOTA NORMALIZADA (1 a 10)", color=cor_subtexto, fontsize=10, fontweight="bold", labelpad=8)
ax2.set_title("/// DESEMPENHO MULTI-CRITÉRIO ///", color="#00f5d4", fontsize=12, fontweight="bold", pad=14, loc="left")
ax2.tick_params(colors=cor_subtexto, labelsize=9)
for spine in ax2.spines.values():
    spine.set_color(cor_grid)
ax2.grid(axis="y", linestyle="--", color=cor_grid, alpha=0.9)

leg = ax2.legend(facecolor=cor_card, edgecolor=cor_grid, title="FORNECEDOR", title_fontsize=9, fontsize=8.5)
leg.get_title().set_color(cor_texto)
for text in leg.get_texts():
    text.set_color(cor_texto)

caminho_grafico1 = os.path.join("resultados", "grafico_analise_fornecedores.png")
plt.tight_layout()
plt.savefig(caminho_grafico1, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()

# ==============================================================================
# GRÁFICO 2: Radar Holográfico Futurista (Skill chart-image)
# ==============================================================================
criterios_radar = ["PREÇO", "PRAZO", "QUALIDADE", "SUPORTE"]
num_vars = len(criterios_radar)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angulos += angulos[:1]

fig, ax = plt.subplots(figsize=(7.5, 7.5), subplot_kw=dict(polar=True), dpi=300, facecolor=cor_fundo)
ax.set_facecolor(cor_fundo)

for forn in df["fornecedor"]:
    linha = df_scores[df_scores["fornecedor"] == forn].iloc[0]
    valores = [
        linha["score_preco"],
        linha["score_prazo"],
        linha["score_qualidade"],
        linha["score_suporte"]
    ]
    valores += valores[:1]
    
    lw = 3.0 if forn == vencedor["fornecedor"] else 1.8
    alpha = 0.35 if forn == vencedor["fornecedor"] else 0.10
    
    ax.plot(angulos, valores, label=forn, color=cores_neon[forn], linewidth=lw, marker="o", markersize=6)
    ax.fill(angulos, valores, color=cores_neon[forn], alpha=alpha)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(criterios_radar, fontsize=11, fontweight="bold", color=cor_texto)
ax.set_ylim(0, 10.5)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=8, color=cor_subtexto)
ax.grid(color=cor_grid, linestyle="--", linewidth=1.1)
ax.spines["polar"].set_color(cor_grid)

ax.set_title("/// PERFIL HOLOGRÁFICO DE FORNECEDORES ///",
             fontsize=12, fontweight="bold", color="#00f5d4", pad=24)

leg_radar = ax.legend(facecolor=cor_card, edgecolor=cor_grid, loc="upper right", bbox_to_anchor=(1.3, 1.15))
for text in leg_radar.get_texts():
    text.set_color(cor_texto)

caminho_grafico_radar = os.path.join("resultados", "grafico_fornecedores_radar.png")
plt.tight_layout()
plt.savefig(caminho_grafico_radar, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()

# ==============================================================================
# GRÁFICO 3: Matriz de Trade-off Futurista (Preço vs Defeitos vs Suporte)
# ==============================================================================
fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300, facecolor=cor_fundo)
ax.set_facecolor(cor_fundo)

# Zona de Eficiência Ótima com brilho ciano suave
ax.axhspan(-0.1, 1.2, color="#00f5d4", alpha=0.08, label="ZONA ALTA EFICIÊNCIA (Defeitos <= 1.2%)")

for _, row in df.iterrows():
    forn = row["fornecedor"]
    tamanho = (row["suporte_nota"] ** 2) * 9
    cor = cores_neon[forn]
    
    # Efeito Halo na bolha
    ax.scatter(row["preco_unitario"], row["defeitos_pct"], s=tamanho * 2.2, color=cor, alpha=0.15, edgecolors="none")
    ax.scatter(row["preco_unitario"], row["defeitos_pct"], s=tamanho, color=cor,
               edgecolors="#ffffff", linewidths=1.5, alpha=0.9, label=f"{forn} [Sup: {row['suporte_nota']}]")
    
    offset_y = 0.22 if forn != "Gama" else -0.38
    ax.annotate(f"◆ {forn}\nR$ {row['preco_unitario']:.0f} | {row['defeitos_pct']}% def | {row['prazo_dias']}d",
                xy=(row["preco_unitario"], row["defeitos_pct"]),
                xytext=(row["preco_unitario"] + 0.9, row["defeitos_pct"] + offset_y),
                fontsize=9, fontweight="bold", color=cor_texto)

ax.set_title("/// TRADE-OFF ANALYSIS: CUSTO vs QUALIDADE ///",
             color="#00f5d4", fontsize=12, fontweight="bold", pad=16, loc="left")
ax.set_xlabel("PREÇO UNITÁRIO (R$) - [MENOR É MELHOR]", color=cor_subtexto, fontsize=10, fontweight="bold", labelpad=10)
ax.set_ylabel("TAXA DE DEFEITOS (%) - [MENOR É MELHOR]", color=cor_subtexto, fontsize=10, fontweight="bold", labelpad=10)
ax.set_xlim(80, 120)
ax.set_ylim(-0.3, 5.0)

ax.tick_params(colors=cor_subtexto, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(cor_grid)
ax.grid(True, linestyle="--", color=cor_grid, alpha=0.85)

leg_to = ax.legend(facecolor=cor_card, edgecolor=cor_grid, loc="upper left", fontsize=8.5)
for text in leg_to.get_texts():
    text.set_color(cor_texto)

caminho_grafico_tradeoff = os.path.join("resultados", "grafico_fornecedores_tradeoff.png")
plt.tight_layout()
plt.savefig(caminho_grafico_tradeoff, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()

# 4. Atualização do Relatório Markdown
caminho_relatorio = os.path.join("resultados", "relatorio_decisao_fornecedores.md")

relatorio_conteudo = f"""# Relatório de Seleção de Fornecedores (Decision Matrix & Futuristic Visuals)

## 1. Contexto e Objetivo
Este relatório consolida a análise comparativa de fornecedores utilizando:
- **decision-matrix**: estruturação de critérios ponderados e normalização das notas.
- **chart-image**: gráficos no estilo *Dark Mode / HUD Sci-Fi*, priorizando legibilidade, contraste em neon e estética futurista.

---

## 2. Dados Originais dos Fornecedores
Fonte: `dados/fornecedores.csv`

| Fornecedor | Preço Unitário (R$) | Prazo de Entrega (dias) | Taxa de Defeitos (%) | Nota de Suporte (0-10) |
|---|---|---|---|---|
| Alfa | R$ 90,00 | 8 | 2,0% | 8,0 |
| Beta | R$ 100,00 | 5 | 1,0% | 9,0 |
| Gama | R$ 85,00 | 12 | 4,0% | 6,0 |
| Delta | R$ 110,00 | 4 | 0,5% | 9,5 |

---

## 3. Matriz de Pontuação e Ranking Final
Pesos de 25% para cada critério (Preço, Prazo, Qualidade e Suporte):

| Posição | Fornecedor | Nota Preço | Nota Prazo | Nota Qualidade | Nota Suporte | Pontuação Final |
|---|---|---|---|---|---|---|
"""

for pos, (_, row) in enumerate(df_ranking.iterrows(), start=1):
    destaque = "**" if pos == 1 else ""
    relatorio_conteudo += f"| {pos}º | {destaque}{row['fornecedor']}{destaque} | {row['score_preco']:.2f} | {row['score_prazo']:.2f} | {row['score_qualidade']:.2f} | {row['score_suporte']:.2f} | {destaque}{row['score_total']:.2f}{destaque} |\n"

relatorio_conteudo += f"""
---

## 4. Visualizações Futuristas Geradas
As visualizações foram desenhadas com visual *Cyberpunk HUD* em alta resolução (300 DPI):

1. **Painel de Score e Critérios:** `resultados/grafico_analise_fornecedores.png`
   - Exibição de barras com neon cyan para o vencedor e detalhes por critério.
2. **Radar Holográfico:** `resultados/grafico_fornecedores_radar.png`
   - Perfil multidimensional com malha polar escura e preenchimento translúcido.
3. **Matriz de Trade-off (Custo vs Qualidade):** `resultados/grafico_fornecedores_tradeoff.png`
   - Dispersão com halos cibernéticos e delimitação da Zona de Alta Eficiência.

---

## 5. Recomendação Final
- **Vencedor Recomendado:** **{vencedor['fornecedor']}** (Pontuação: **{vencedor['score_total']:.2f}/10**).
- **Veredito:** Domínio absoluto nos quesitos de agilidade (4 dias), confiabilidade (apenas 0,5% de defeitos) e suporte (nota 9,5).
"""

with open(caminho_relatorio, "w", encoding="utf-8") as f:
    f.write(relatorio_conteudo)

print(f"\nGráficos futuristas e relatório gerados com sucesso na pasta resultados/:")
print(f"1. {caminho_grafico1}")
print(f"2. {caminho_grafico_radar}")
print(f"3. {caminho_grafico_tradeoff}")
print(f"4. {caminho_relatorio}")
