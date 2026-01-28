# main.py

from models.regression import LinearRegModel
from models.classification import KNNModel
from utils.metrics import accuracy_score

# 1. ا(Regression)
print("--- Regression Test ---")
reg = LinearRegModel()
reg.fit([1, 2, 3], [10, 20, 30])
print(reg.predict([5, 6]))  # المفروض يطبع [20.0, 20.0] بناء على المحاكاة

print("\n--- Classification Test ---")
#20 claasificaton
knn = KNNModel()
knn.train([1, 2, 3], ["A", "B", "A"])
pred = knn.predict([10, 11])
print(pred) # المفروض يطبع ['class1', 'class1']

# 3.(Metrics)
score = accuracy_score(["class1", "class1"], pred)
print(f"Accuracy: {score}")