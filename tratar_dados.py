import os
import pandas as pd

# 1. Leitura do arquivo com dados faltantes (NUNCA alterando a pasta dados/)
caminho_original = os.path.join("dados", "fornecedores_erro.csv")
df = pd.read_csv(caminho_original)

print("=== DADOS ANTES DO PREENCHIMENTO ===")
print(df[["fornecedor", "suporte_nota"]])

# 2. Cálculo da média dos valores existentes na coluna suporte_nota
# Valores existentes: Alfa = 8.0, Gama = 6.0 -> Média = (8.0 + 6.0) / 2 = 7.0
media_suporte = df["suporte_nota"].mean()
print(f"\nMédia calculada dos valores válidos: {media_suporte:.2f}")

# 3. Preenchimento dos dados faltantes (NaN) com a média
df["suporte_nota"] = df["suporte_nota"].fillna(media_suporte)

print("\n=== DADOS APÓS O PREENCHIMENTO COM A MÉDIA ===")
print(df[["fornecedor", "suporte_nota"]])

# 4. Salvando a base tratada dentro da pasta resultados/
os.makedirs("resultados", exist_ok=True)
caminho_tratado = os.path.join("resultados", "fornecedores_tratado.csv")
df.to_csv(caminho_tratado, index=False)

print(f"\nArquivo tratado salvo com sucesso em: {caminho_tratado}")
print("O arquivo original em dados/fornecedores_erro.csv permaneceu 100% intacto.")

