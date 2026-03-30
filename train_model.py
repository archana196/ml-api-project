from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

# Step 1: Create simple data
X = np.array([[1], [2], [3], [4], [5]])  # input
y = np.array([2, 4, 6, 8, 10])           # output

# Step 2: Train model
model = LinearRegression()
model.fit(X, y)

# Step 3: Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")