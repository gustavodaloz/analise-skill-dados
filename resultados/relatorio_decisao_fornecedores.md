# Relatório de Seleção de Fornecedores (Decision Matrix & Futuristic Visuals)

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
| 1º | **Delta** | 7.73 | 10.00 | 10.00 | 10.00 | **9.43** |
| 2º | Beta | 8.50 | 8.00 | 5.00 | 9.47 | 7.74 |
| 3º | Alfa | 9.44 | 5.00 | 2.50 | 8.42 | 6.34 |
| 4º | Gama | 10.00 | 3.33 | 1.25 | 6.32 | 5.22 |

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
- **Vencedor Recomendado:** **Delta** (Pontuação: **9.43/10**).
- **Veredito:** Domínio absoluto nos quesitos de agilidade (4 dias), confiabilidade (apenas 0,5% de defeitos) e suporte (nota 9,5).
