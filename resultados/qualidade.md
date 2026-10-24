# Relatório de Conferência de Qualidade de Dados (Skill: conferir-csv)

## 1. Identificação do Arquivo e Finalidade
- **Arquivo analisado:** `dados/fornecedores_erro.csv`
- **Finalidade:** Avaliação e seleção de fornecedores via matriz de decisão.
- **Separador utilizado:** Vírgula (`,`)
- **O que cada linha representa:** Os atributos de desempenho comercial e operacional de um fornecedor específico.

---

## 2. Estrutura e Métricas Gerais
- **Total de linhas de dados:** 4
- **Total de colunas:** 5
- **Linhas duplicadas:** 0

### Colunas e Tipos de Dados Detectados:
| Coluna | Tipo Detectado | Valores Ausentes | % Ausência |
|---|---|---|---|
| `fornecedor` | `str` | 0 | 0.0% |
| `preco_unitario` | `int64` | 0 | 0.0% |
| `prazo_dias` | `int64` | 0 | 0.0% |
| `defeitos_pct` | `float64` | 0 | 0.0% |
| `suporte_nota` | `float64` | 2 | 50.0% |

---

## 3. Problemas Encontrados e Evidências
1. **Valores Ausentes na coluna `suporte_nota`:**
   - Detectados **2 valores ausentes** (50.0% da coluna).
   - Fornecedores afetados: **Beta** e **Delta**.

---

## 4. Tratamento Aplicado (Imputação pela Média)
Conforme solicitado e seguindo as boas práticas da skill `conferir-csv`:
- **Regra de Imputação:** Calculada a média aritmética dos valores válidos conhecidos:
  $$\text{Média} = \frac{8.0 (\text{Alfa}) + 6.0 (\text{Gama})}{2} = 7.0$$
- **Preenchimento:**
  - `Beta`: `suporte_nota` preenchido com **7.0**
  - `Delta`: `suporte_nota` preenchido com **7.0**
- **Preservação de Integridade:** O arquivo original `dados/fornecedores_erro.csv` **não foi alterado**.
- **Novo Arquivo Gerado:** `resultados/fornecedores_tratado.csv`.
