import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Pontos de calibração base
x1, y1 = 0, 4
x2, y2 = 100, 20

# 2. Equação da reta: y = a*x + b
a = (y2 - y1) / (x2 - x1)
b = y1 - (a * x1)

print(f"Coeficiente a (inclinação): {a}")
print(f"Coeficiente b (intercepto): {b}")
print(f"Equação da reta: y = {a} * x + {b}\n")

# 3. Ponto de teste: 50 graus
x_teste = 50
y_teste = a * x_teste + b

if x_teste <= 30:
    classificacao = "Baixa"
elif x_teste <= 60:
    classificacao = "Média"
else:
    classificacao = "Alta"

print(f"--- Telemetria para x = {x_teste} °C ---")
print(f"Sinal de corrente: {y_teste} mA | Status: {classificacao}")

if x_teste < 0 or x_teste > 100:
    print(f"AVISO: Temperatura fora dos limites operacionais (0-100 °C)!")

if y_teste < 4 or y_teste > 20:
    print(f"AVISO: Corrente fora dos limites operacionais (4-20 mA)!")

# 4. Geração do Gráfico Futurista / Dark Mode HUD
os.makedirs("resultados", exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 6), dpi=300, facecolor="#0b0f19")
ax.set_facecolor("#0b0f19")

# Zonas operacionais com gradientes suaves de neon
ax.axvspan(0, 30, color="#00f5d4", alpha=0.08, label="ZONA BAIXA [0-30°C]")
ax.axvspan(30, 60, color="#f59e0b", alpha=0.08, label="ZONA MÉDIA [30-60°C]")
ax.axvspan(60, 100, color="#ff0055", alpha=0.08, label="ZONA ALTA [60-100°C]")

# Efeito Glow na Reta de Calibração (camadas com diferentes espessuras e transparências)
x_vals = np.linspace(0, 100, 200)
y_vals = a * x_vals + b
ax.plot(x_vals, y_vals, color="#00f0ff", linewidth=8, alpha=0.15)
ax.plot(x_vals, y_vals, color="#00f0ff", linewidth=4, alpha=0.35)
ax.plot(x_vals, y_vals, color="#ffffff", linewidth=1.8, label=f"Curva Calibração: y = {a:.2f}x + {b:.1f}")

# Linhas de Limite Elétrico (Neon Magenta com brilho sutil)
ax.axhline(4, color="#ff007f", linestyle="--", linewidth=1.3, alpha=0.85, label="Limite Mínimo (4 mA)")
ax.axhline(20, color="#ff007f", linestyle="--", linewidth=1.3, alpha=0.85, label="Limite Máximo (20 mA)")

# Ponto de Teste com Efeito de Halo Cibernético
ax.scatter([x_teste], [y_teste], s=500, color="#00f5d4", alpha=0.15, edgecolors="none")
ax.scatter([x_teste], [y_teste], s=200, color="#00f5d4", alpha=0.45, edgecolors="none")
ax.scatter([x_teste], [y_teste], s=70, color="#ffffff", edgecolors="#00f5d4", linewidths=2.2, zorder=5)

# Caixa de Anotação HUD Futurista
bbox_hud = dict(boxstyle="square,pad=0.7", facecolor="#111827", edgecolor="#00f0ff", linewidth=1.6, alpha=0.95)
ax.annotate(
    f"◆ STATUS DO SENSOR ◆\n"
    f"TEMP  : {x_teste}.0 °C\n"
    f"SINAL : {y_teste:.1f} mA\n"
    f"FAIXA : {classificacao.upper()}",
    xy=(x_teste, y_teste),
    xytext=(x_teste - 36, y_teste + 3.8),
    arrowprops=dict(arrowstyle="->", color="#00f0ff", lw=1.8),
    bbox=bbox_hud,
    color="#f1f5f9",
    fontsize=9.5,
    fontfamily="sans-serif",
    fontweight="bold"
)

# Títulos e Eixos no estilo HUD Sci-Fi
ax.set_title("/// TELEMETRIA DO SENSOR INDUSTRIAL ///\nSISTEMA AVANÇADO DE CALIBRAÇÃO TÉRMICA",
             color="#00f0ff", fontsize=13, fontweight="bold", pad=16, loc="left")
ax.set_xlabel("TEMPERATURA OPERACIONAL (°C)", color="#94a3b8", fontsize=10, fontweight="bold", labelpad=10)
ax.set_ylabel("SINAL DE CONTROLE (mA)", color="#94a3b8", fontsize=10, fontweight="bold", labelpad=10)

ax.tick_params(colors="#94a3b8", labelsize=9)
for spine in ax.spines.values():
    spine.set_color("#1e293b")
    spine.set_linewidth(1.2)

ax.set_xlim(-5, 105)
ax.set_ylim(1, 23)
ax.grid(True, linestyle="--", color="#1e293b", alpha=0.85)

leg = ax.legend(facecolor="#111827", edgecolor="#1e293b", fontsize=8.5, loc="lower right")
for text in leg.get_texts():
    text.set_color("#cbd5e1")

caminho_grafico = os.path.join("resultados", "grafico_termometro.png")
plt.tight_layout()
plt.savefig(caminho_grafico, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()

print(f"\nGráfico futurista gerado com sucesso em: {caminho_grafico}")
