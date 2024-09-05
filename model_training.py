import mlflow
import mlflow.sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Initialiser un experiment MLflow nommé "projet"
mlflow.set_experiment("projet")

# Dictionnaire pour stocker les performances des modèles
model_performances = {}

def train_model(X_train, y_train, X_test, y_test, model, model_name):
    """
    Cette fonction entraîne un modèle donné, suit les métriques dans MLflow, et retourne les performances.
    """
    with mlflow.start_run(run_name=model_name):
        # Entraîner le modèle
        model.fit(X_train, y_train)
        # Prédire les valeurs de test
        predictions = model.predict(X_test)
        # Calculer l'accuracy
        accuracy = accuracy_score(y_test, predictions)
        # Calculer l'AUC-ROC
        auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

        # Afficher les résultats dans la console
        print(f"Modèle: {model_name}")
        print(f"Accuracy: {accuracy}")
        print(f"AUC-ROC: {auc}")
        print("-" * 40)

        # Logguer les paramètres et métriques dans MLflow
        mlflow.log_param("model_type", model_name)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("auc_roc", auc)

        # Logguer le modèle dans MLflow
        mlflow.sklearn.log_model(model, model_name)

        # Retourner les performances sous forme de dictionnaire
        return {"model": model, "accuracy": accuracy, "auc_roc": auc}

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
model_performances["Decision Tree"] = train_model(X_train, y_train, X_test, y_test, decision_tree, "Decision Tree")

# Entraîner et suivre une régression logistique
logistic_regression = LogisticRegression(random_state=42)
model_performances["Logistic Regression"] = train_model(X_train, y_train, X_test, y_test, logistic_regression, "Logistic Regression")

# Entraîner et suivre un Random Forest
random_forest = RandomForestClassifier(random_state=42, n_estimators=100)
model_performances["Random Forest"] = train_model(X_train, y_train, X_test, y_test, random_forest, "Random Forest")

# Comparaison des modèles : sélectionner le modèle avec le meilleur AUC-ROC
best_model_name = max(model_performances, key=lambda x: model_performances[x]['auc_roc'])
best_model = model_performances[best_model_name]['model']
best_auc_roc = model_performances[best_model_name]['auc_roc']

print(f"Le meilleur modèle est : {best_model_name} avec un AUC-ROC de {best_auc_roc}")

# Sauvegarder le meilleur modèle sous forme de fichier .pkl
with open(f'{best_model_name}_best_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)

print(f"Le modèle {best_model_name} a été sauvegardé sous {best_model_name}_best_model.pkl")