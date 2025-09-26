import os
import numpy as np
import matplotlib.pyplot as plt

# Create a folder if it doesn't exist
output_folder = "charts"
os.makedirs(output_folder, exist_ok=True)

# File path to save
output_path = os.path.join(output_folder, "equity_growth_rr_comparison.png")

# Recreate the chart
initial_capital = 100000
trades = 20
scenarios = {
    "70% Win, RR=0.8": {"win_rate": 0.7, "rr": 0.8},
    "40% Win, RR=2.5": {"win_rate": 0.4, "rr": 2.5},
}

plt.figure(figsize=(9, 5))
for label, params in scenarios.items():
    capital = [initial_capital]
    equity = initial_capital
    for _ in range(trades):
        if np.random.rand() < params["win_rate"]:
            equity += equity * 0.01 * params["rr"]
        else:
            equity -= equity * 0.01
        capital.append(equity)
    plt.plot(range(trades + 1), capital, marker="o", label=label)

plt.title("Equity Growth Over 20 Trades", fontsize=14)
plt.xlabel("Number of Trades", fontsize=12)
plt.ylabel("Account Equity", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save locally in charts folder
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Chart saved to: {output_path}")
