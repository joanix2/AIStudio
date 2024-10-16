# Fonction pour générer les modèles C# à partir du fichier DBML
from textGen import appeler_openai


def generate_csharp_models(dbml_file):
    # Lire le contenu du fichier DBML
    try:
        with open(dbml_file, "r") as f:
            dbml_content = f.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier DBML : {e}")
        return None

    system_message = "You are an assistant that generates C# models from DBML schema files."

    # Construire le message utilisateur pour convertir le DBML en modèles C#
    user_message = f"Generate C# models from the following DBML schema:\n\n{dbml_content}"

    destination_dir = "./models"  # Dossier de destination pour les fichiers générés

    # Appeler l'API pour générer les modèles C#
    appeler_openai(system_message, user_message, create_files=True, destination_dir=destination_dir)

    return destination_dir