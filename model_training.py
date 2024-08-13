import mlflow
import mlflow.sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def train_model(X_train, y_train, X_test, y_test, model, model_name):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

        print(f"Accuracy: {accuracy}")
        print(f"AUC-ROC: {auc}")

        mlflow.log_param("model_type", model_name)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("auc_roc", auc)

        mlflow.sklearn.log_model(model, model_name)

# Chargement des données depuis un fichier CSV
data = pd.read_csv('data/Loan_Data.csv')

# Séparation des features (X) et de la variable cible (y)
X = data.drop(columns=['customer_id', 'default'])
y = data['default']

# Normalisation des features pour les mettre à la même échelle
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Division en ensembles d'entraînement et de test (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entraîner et suivre un arbre de décision
decision_tree = DecisionTreeClassifier(random_state=42)
train_model(X_train, y_train, X_test, y_test, decision_tree, "Decision Tree")

# Entraîner et suivre une régression logistique
logistic_regression = LogisticRegression(random_state=42)
train_model(X_train, y_train, X_test, y_test, logistic_regression, "Logistic Regression")