import os
import json
import openai
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la clé API à partir des variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# Fonction pour appeler l'API OpenAI avec ou sans function calling
def appeler_openai(system, user, create_files=False, destination_dir=None):
    try:
        # Construire le message de base
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]

        # Définir le répertoire de destination, par défaut le répertoire courant
        if destination_dir is None:
            destination_dir = os.getcwd()

        # Si create_files est activé, passer par function calling pour générer plusieurs fichiers
        if create_files:
            function_name = "generate_files"
            function_args = {}  # GPT génère les noms et contenus des fichiers

            # Appeler l'API OpenAI avec function calling pour générer plusieurs fichiers
            completion = openai.ChatCompletion.create(
                model="gpt-4-0613",
                messages=messages,
                functions=[{
                    "name": function_name,
                    "description": "Generate multiple files with names and content based on the user's request.",
                    "parameters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "file_name": {"type": "string"},
                                "content": {"type": "string"}
                            },
                            "required": ["file_name", "content"]
                        }
                    }
                }],
                function_call={"name": function_name, "arguments": json.dumps(function_args)}
            )

            # Récupérer les arguments de la fonction appelée (nom du fichier et contenu)
            response_message = completion.choices[0].message['function_call']['arguments']
            response_data = json.loads(response_message)

            # Enregistrer chaque fichier généré
            for file in response_data:
                yield save_generated_file(file['file_name'], file['content'], destination_dir)
        else:
            # Appeler l'API pour une completion classique
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            # Retourner la réponse simple
            return completion.choices[0].message['content']

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

# Fonction pour sauvegarder les fichiers générés dans le dossier de destination
def save_generated_file(file_name, content, destination_dir):
    # Assurez-vous que le répertoire de destination existe
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Créer le chemin complet du fichier
    file_path = os.path.join(destination_dir, file_name)

    # Sauvegarder le fichier
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Fichier '{file_name}' généré et sauvegardé dans '{destination_dir}'.")

    return destination_dir
