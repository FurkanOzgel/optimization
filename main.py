from parser import load_multiple_stocks
import cvxpy as cp
import numpy as np

def konno_yamazaki(returns, mu, target_return):
    T, N = returns.shape
    R = returns.values
    mu_vec = mu.values

    w = cp.Variable(N)
    z = cp.Variable(T)

    portfolio_returns = R @ w
    mean_portfolio_return = mu_vec @ w

    objective = cp.Minimize(cp.sum(z))

    constraints = [
        z >= portfolio_returns - mean_portfolio_return,
        z >= -(portfolio_returns - mean_portfolio_return),
        cp.sum(w) == 1,
        w >= 0,
        mean_portfolio_return >= target_return
    ]

    problem = cp.Problem(objective, constraints)
    problem.solve()

    return w.value


# 1. Fiyat verisi
prices_train = load_multiple_stocks("train_data")
prices_test  = load_multiple_stocks("test_data")

# 2. Getiriler
returns = prices_train.pct_change(fill_method=None).dropna()
returns_test = prices_test.pct_change(fill_method=None).dropna()

# 3. Ortalama getiriler
mu = returns.mean()

# Ödev gereksinimine göre: min, ortalama ve max getiri hedefleri
R_min = mu.min()
R_mean = mu.mean()
R_max = mu.max()

targets = {
    "min": R_min,
    "mean": R_mean,
    "max": R_max
}


weights = {}

for name, target in targets.items():
    w = konno_yamazaki(returns, mu, target)
    weights[name] = w
    actual_return = mu.values @ w

print()
print("=" * 60)
print("TEST VERİSİ ÜZERİNDE PERFORMANS")
print("=" * 60)

for name, wgt in weights.items():
    realized_returns = returns_test.values @ wgt
    print(f"{name:5s} model - Ortalama Getiri: {realized_returns.mean():.6f}")

print()
print("=" * 60)
print("TEST VERİSİ ÜZERİNDE RİSK (MAD)")
print("=" * 60)

for name, wgt in weights.items():
    r = returns_test.values @ wgt
    risk = np.mean(np.abs(r - r.mean()))
    print(f"{name:5s} model - Risk (MAD): {risk:.6f}")

print()
print("=" * 60)
print("PORTFÖY BİLEŞİMLERİ")
print("=" * 60)

asset_names = returns.columns

for name, wgt in weights.items():
    print(f"\n{name.upper()} MODEL PORTFÖYÜ:")
    selected_mask = wgt > 1e-6
    selected = asset_names[selected_mask]
    selected_weights = wgt[selected_mask]
    
    for asset, weight in zip(selected, selected_weights):
        print(f"  {asset:10s}: {weight:6.2%}")
    print(f"  Toplam    : {wgt.sum():6.2%}")

