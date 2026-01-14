FROM python:3.10-slim

# Dépendances système audio
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Dossier de travail
WORKDIR /app

# Copier les fichiers
COPY pipeline/ pipeline/
COPY data/ data/
COPY requirements.txt .

# Installer dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut
ENTRYPOINT ["python", "pipeline/main.py"]

