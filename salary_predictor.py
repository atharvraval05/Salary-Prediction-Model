import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data2 = {'Exp': [1, 2, 3, 4, 5, 6, 7],
         'Salary': [20000, 45000, 67890, 82290, 89820, 93083, 99999]}
df2 = pd.DataFrame(data2)

x2 = df2[['Exp']]
y2 = df2['Salary']

# Train model
model2 = LinearRegression()
model2.fit(x2, y2)

# User input
year = int(input("Enter years of experience: "))

# Prediction
pred_salary = model2.predict([[year]])
print(f"Predicted Salary at {year} years of experience: {pred_salary[0]:.2f}")

# Regression line
y_pred = model2.predict(x2)

# Plot actual data
plt.scatter(x2, y2, color='blue', label="Actual Data")

# Plot regression line
plt.plot(x2, y_pred, color='red', linewidth=2, label="Regression Line")

# Plot user prediction point
plt.scatter([year], pred_salary, color='green', marker='x', s=100,
            label=f"Prediction at {year} years")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Years Of Experience vs Salary")
plt.legend()
plt.grid(axis="y", alpha=0.4)
plt.show()

# Print equation of line
print(f"Salary = {model2.coef_[0]:.2f} * Experience + {model2.intercept_:.2f}")
