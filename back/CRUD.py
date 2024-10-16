# Fonction pour générer un fichier Controller à partir d'un modèle C#
import os
from textGen import appeler_openai


def generate_controller_for_model(model_file, destination_dir):
    try:
        # Lire le contenu du modèle actuel
        with open(model_file, "r") as f:
            model_content = f.read()

        # Extraire le nom du modèle à partir du fichier (nom du fichier sans extension)
        model_name = os.path.basename(model_file).replace(".cs", "")

        # Construire la demande pour OpenAI pour générer un Controller basé sur ce modèle
        system_message = "You are an assistant that generates C# API controllers with CRUD routes."
        user_message = f"Generate a C# API controller with CRUD routes for the following model:\n\n{model_content}"

        # Appeler OpenAI pour générer le contenu du fichier Controller
        controller_content = appeler_openai(system_message, user_message)

        # Si le contenu du Controller est généré, sauvegarder dans un nouveau fichier
        if controller_content:
            controller_file_name = f"{model_name}Controller.cs"
            controller_file_path = os.path.join(destination_dir, controller_file_name)

            with open(controller_file_path, "w") as f:
                f.write(controller_content)

            print(f"Controller '{controller_file_name}' généré avec succès dans '{destination_dir}'.")
        else:
            print(f"Erreur lors de la génération du Controller pour '{model_file}'.")

    except Exception as e:
        print(f"Une erreur est survenue lors de la génération du Controller pour '{model_file}': {e}")

# Fonction principale pour parcourir chaque fichier modèle dans le dossier 'models' et générer des fichiers Controller
def generate_controllers_from_models(models_dir, controllers_dir):
    # Vérifier si le dossier des modèles existe
    if not os.path.exists(models_dir):
        print(f"Le dossier '{models_dir}' n'existe pas.")
        return

    # Créer le dossier des controllers s'il n'existe pas
    if not os.path.exists(controllers_dir):
        os.makedirs(controllers_dir)

    # Parcourir tous les fichiers .cs dans le dossier spécifié
    for file_name in os.listdir(models_dir):
        if file_name.endswith(".cs"):  # Sélectionner uniquement les fichiers C#
            model_file_path = os.path.join(models_dir, file_name)
            generate_controller_for_model(model_file_path, controllers_dir)