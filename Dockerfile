FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier tous les fichiers du répertoire courant dans le répertoire de travail
COPY . /app/

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Commande d'exécution de l'application
CMD ["python", "app.py"]
