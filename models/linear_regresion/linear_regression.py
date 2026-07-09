import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("./height-weight.csv")

# Extract values
X_original = df["Weight"].values
y = df["Height"].values

# -------- Feature Scaling --------
X_mean = np.mean(X_original)
X_std = np.std(X_original)

X = (X_original - X_mean) / X_std

# -------- Initialize Parameters --------
m = 0
b = 0

learning_rate = 0.01
iterations = 10000
n = len(X)

# -------- Loss Function --------
def loss_function(m, b, X, y):
    return np.mean((y - (m * X + b)) ** 2)

# -------- Gradient Descent --------
for i in range(iterations):
    y_pred = m * X + b
    
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    
    m -= learning_rate * dm
    b -= learning_rate * db
    
    if i % 1000 == 0:
        print(f"Iteration {i}, Loss: {loss_function(m, b, X, y)}")

print("\nFinal parameters (scaled space):")
print("m =", m)
print("b =", b)

# -------- Convert Line Back to Original Scale --------
# Because we trained on scaled X, we must convert slope back

m_original = m / X_std
b_original = b - (m * X_mean / X_std)

print("\nFinal equation in original scale:")
print(f"Height = {m_original:.4f} * Weight + {b_original:.4f}")

# -------- Plot --------
plt.scatter(X_original, y)
plt.plot(X_original, m_original * X_original + b_original)
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Optimized Linear Regression from Scratch")
plt.show()