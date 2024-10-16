#!/bin/bash

# Vérifier si un nom de projet et une adresse de base ont été fournis
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <nom_du_projet> <adresse_de_base>"
  echo "Exemple : $0 mon_projet https://example.com/repo/"
  exit 1
fi

# Variables
PROJECT_NAME=$1
BASE_URL=$2
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ENV="${PROJECT_NAME}-environment"
FRONT_REPO="${PROJECT_NAME}-front"
API_REPO="${PROJECT_NAME}-API"
ASSETS_REPO="${PROJECT_NAME}-assets"

# Créer le repository d'environnement
echo "Création du repository d'environnement : $REPO_ENV"
mkdir $REPO_ENV
cd $REPO_ENV
git init

# Créer et ajouter des sous-modules pour le front-end, l'API et les assets
echo "Ajout des sous-modules pour le front-end, l'API et les assets..."
mkdir $FRONT_REPO $API_REPO $ASSETS_REPO
git submodule add ${BASE_URL}${FRONT_REPO}.git $FRONT_REPO
git submodule add ${BASE_URL}${API_REPO}.git $API_REPO
git submodule add ${BASE_URL}${ASSETS_REPO}.git $ASSETS_REPO

# Lancer les scripts d'initialisation des projets front-end et back-end
echo "Initialisation du projet front-end Angular..."
"$SCRIPT_DIR/init_angular.sh" "${FRONT_REPO}"

echo "Initialisation du projet back-end API (.NET)..."
"$SCRIPT_DIR/init_dotnet.sh" "${API_REPO}"

# Créer les templates Docker et docker-compose
echo "Configuration de Docker..."

# Copier le template docker-compose et remplacer les placeholders
cp "$SCRIPT_DIR/templates/docker-compose.yml.template" "$REPO_ENV/docker-compose.yml"
sed -i "s/@ANGULAR_PROJECT_NAME@/${FRONT_REPO}/g" "$REPO_ENV/docker-compose.yml"
sed -i "s/@DOTNET_PROJECT_NAME@/${API_REPO}/g" "$REPO_ENV/docker-compose.yml"

# Copier les Dockerfiles dans les répertoires appropriés
cp "$SCRIPT_DIR/templates/Dockerfile.angular.template" "${FRONT_REPO}/Dockerfile"
cp "$SCRIPT_DIR/templates/Dockerfile.dotnet.template" "${API_REPO}/Dockerfile"

# Remplacer les placeholders dans le Dockerfile .NET
sed -i "s/@PROJECT_NAME@/${API_REPO}/g" "${API_REPO}/Dockerfile"

# Commiter les changements dans le repository d'environnement
echo "Commit des modifications dans le repository d'environnement..."
git add .
git commit -m "Initialisation du projet avec sous-modules front-end, back-end et assets"

echo "Initialisation du projet ${PROJECT_NAME} terminée avec succès."
