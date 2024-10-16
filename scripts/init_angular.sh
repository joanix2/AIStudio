#!/bin/bash

# Vérifier si un nom de projet a été fourni en argument
if [ -z "$1" ]; then
  echo "Erreur : Vous devez fournir un nom pour le projet."
  echo "Usage : ./init_angular.sh <nom-du-projet>"
  exit 1
fi

# Nom du projet fourni en argument
PROJECT_NAME=$1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Version Angular souhaitée
ANGULAR_VERSION="18.0.0"

# Initialisation du projet Angular
echo "Initialisation du projet Angular $ANGULAR_VERSION..."
npx -p @angular/cli@$ANGULAR_VERSION ng new "$PROJECT_NAME" --routing --style=css --strict --skip-git
cd "$PROJECT_NAME" || exit

# Ajout de Tailwind CSS
echo "Ajout de Tailwind CSS..."
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init

# Configuration de Tailwind
echo "Configuration de Tailwind..."
cp "$SCRIPT_DIR/templates/tailwind.config.js.template" tailwind.config.js

# Mise à jour du fichier styles.css pour inclure Tailwind
{
  echo "@tailwind base;"
  echo "@tailwind components;"
  echo "@tailwind utilities;"
} > src/styles.css

# Installation d'Angular Material
echo "Ajout d'Angular Material..."
ng add @angular/material --defaults

# Finalisation
echo "Initialisation complète du projet '$PROJECT_NAME' avec Tailwind et Angular Material."
