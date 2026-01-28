# utils/metrics.py

def accuracy_score(y_true, y_pred):

    if len(y_true) != len(y_pred):
        return 0.0
    
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)