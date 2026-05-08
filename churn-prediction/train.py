import joblib
from sklearn.model_selection import train_test_split
from src.preprocessing import load_data, preprocess_data
from src.model import train_model
from src.evaluation import evaluate_model

df = load_data("data/churn.csv")
df = preprocess_data(df)

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = train_model(X_train, y_train)

acc, auc = evaluate_model(model, X_test, y_test)

print("Accuracy:", acc)
print("ROC-AUC:", auc)

joblib.dump(model, "model.pkl")
joblib.dump(X.columns, "features.pkl")
