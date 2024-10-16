import os
from textGen import appeler_openai

# Fonction pour mettre à jour le fichier avec les DTOs générés
def mettre_a_jour_avec_dto(file_path):
    try:
        # Lire le contenu du fichier modèle actuel
        with open(file_path, "r") as f:
            model_content = f.read()

        # Construire la demande pour OpenAI pour générer les DTOs
        system_message = "You are an assistant that generates C# DTOs for input and output based on existing models."
        user_message = f"Generate C# DTOs for input and output based on the following model:\n\n{model_content}"

        # Appeler OpenAI pour générer les DTOs
        dto_content = appeler_openai(system_message, user_message)

        # Si le contenu des DTOs est généré, l'ajouter au fichier
        if dto_content:
            with open(file_path, "a") as f:  # Ouvrir le fichier en mode append
                f.write("\n\n// DTOs for Input and Output\n")
                f.write(dto_content)
            print(f"DTOs ajoutés à '{file_path}' avec succès.")
        else:
            print(f"Erreur lors de la génération des DTOs pour '{file_path}'.")

    except Exception as e:
        print(f"Une erreur est survenue lors de la mise à jour de '{file_path}': {e}")

# Fonction principale pour parcourir chaque fichier dans le dossier 'models' et mettre à jour avec les DTOs
def update_models_with_dtos(directory):
    # Vérifier si le dossier existe
    if not os.path.exists(directory):
        print(f"Le dossier '{directory}' n'existe pas.")
        return

    # Parcourir tous les fichiers .cs dans le dossier spécifié
    for file_name in os.listdir(directory):
        if file_name.endswith(".cs"):  # Sélectionner uniquement les fichiers C#
            file_path = os.path.join(directory, file_name)
            mettre_a_jour_avec_dto(file_path)

# Exemple d'utilisation
def main():
    models_directory = "./models"  # Dossier contenant les fichiers .cs
    update_models_with_dtos(models_directory)

if __name__ == "__main__":
    main()
