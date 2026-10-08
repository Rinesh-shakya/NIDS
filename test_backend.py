import pandas as pd

from integration.predictor import detect_and_mitigate
from integration.history import save_history
from integration.history import load_history

X_test = pd.read_csv("data/processed/X_test.csv")

sample = X_test.iloc[0]

result = detect_and_mitigate(sample)

save_history(result)

print(load_history())