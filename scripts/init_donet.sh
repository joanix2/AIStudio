#!/bin/bash

# Vérifier si le nom du projet est passé en paramètre
if [ -z "$1" ]; then
  echo "Usage: $0 <nom_du_projet>"
  exit 1
fi

# Nom du projet
PROJECT_NAME=$1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Initialiser un projet API C# .NET avec le nom passé en paramètre
dotnet new webapi -n "$PROJECT_NAME"

# Aller dans le répertoire du projet
cd "$PROJECT_NAME" || exit

# Ajouter Swagger (Swagger est déjà intégré dans un projet Web API, mais on s'assure ici)
dotnet add package Swashbuckle.AspNetCore

# Modifier Program.cs pour activer Swagger
sed -i 's/.*app.UseSwaggerUI.*/app.UseSwagger();\napp.UseSwaggerUI();/' Program.cs

# Ajouter fichiers de configuration pour Visual Studio Code
mkdir -p .vscode

# Copier les templates et remplacer les placeholders
cp "$SCRIPT_DIR/templates/launch.json.template" .vscode/launch.json
cp "$SCRIPT_DIR/templates/tasks.json.template" .vscode/tasks.json

sed -i "s/@PROJECT_NAME@/$PROJECT_NAME/g" .vscode/launch.json
sed -i "s/@PROJECT_NAME@/$PROJECT_NAME/g" .vscode/tasks.json

# Restaurer les packages et construire le projet
dotnet restore
dotnet build

echo "Initialisation complète du projet '$PROJECT_NAME'."
