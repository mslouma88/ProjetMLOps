# 🚀 Projet MLOps : Prédiction des Défauts de Paiement pour les Prêts Personnels

## 📚 Aperçu du Projet

Nous avons rejoint une nouvelle équipe dans le secteur de la **banque de détail**, qui fait face à des **taux de défaut élevés** sur les prêts personnels. Ces prêts sont essentiels pour les revenus de la banque, mais comportent un risque élevé de non-remboursement par les emprunteurs. L'objectif de ce projet est de développer un modèle prédictif capable d'estimer la probabilité de défaut de paiement pour chaque client, en fonction de ses caractéristiques. Cela permettra à la banque de mieux gérer le risque et d'assurer sa stabilité financière.


## 🎯 Objectif
L'objectif principal est de construire un modèle prédictif qui estime la probabilité de défaut pour chaque client. Les prédictions précises aideront à allouer suffisamment de capital pour couvrir les pertes potentielles.

L'équipe de risque (notre équipe) souhaite analyser le portefeuille de prêts existants afin de prévoir les **défauts potentiels futurs** et d'estimer la perte attendue. Notre tâche consiste à adopter une **démarche MLOps end-to-end** pour proposer à la banque un **algorithme de prédiction des risques de défaut**.

## 🛠️ Étapes du Projet

1. **Appropriation du sujet** : Compréhension du contexte et des données disponibles.
2. **Pré-traitement des données** : Nettoyage, transformation et préparation des données pour l'entraînement des modèles.
3. **Model Engineering** : Tester au moins deux algorithmes de classification (par exemple : arbre de décision, régression logistique, Random Forest).
4. **Déploiement du meilleur modèle** : Créer une application (Flask) et déployer sur le cloud.

## 🛠️ Technologies Utilisées

- **Python** 🐍
- **Scikit-Learn** 🧠
- **Flask** 🌐
- **MLflow** 📊
- **Docker** 🐳
- **Git & GitHub** 🔄
- **AWS** ☁️

## 🚀 Exécution du Projet

### 1. Initialisation du projet
- Clonez le dépôt :
    ```bash
    git clone https://github.com/mslouma88/ProjetMLOps.git
    ```
- Initialisez MLflow pour le suivi des expérimentations.

### 2. Pré-traitement des données
- Effectuons le nettoyage et la transformation des données via les notebooks fournis.

### 3. Entraînement des modèles
- Entraînons et évaluons plusieurs modèles de classification, en enregistrant chaque modèle comme un **experiment** dans MLflow.
- Comparons les **métriques** dans MLflow pour sélectionner le meilleur modèle.

### 4. Déploiement
- Construisons l'image Docker pour l'application :
    ```bash
    docker build -t prediction-defauts-app .
    ```
- Déployons l'application sur le cloud via AWS.
- Partagons l'URL de notre application pour la démonstration.

## 👥 Auteur(e)s

Ce projet a été réalisé par :

- **Salam MEJRI** 🧑‍💻 - [@github](https://github.com/mslouma88) 
- **Nesrine BENAMOR** 🧑‍💻 - [@github](https://github.com/Nes890)


## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

Merci pour votre intérêt pour notre projet ! Si vous avez des questions, n'hésitez pas à nous contacter. 😊
