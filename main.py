import json
import os

from ask import poser_question
from back.CRUD import generate_controllers_from_models
from back.DTOs import update_models_with_dtos
from back.models import generate_csharp_models
from back.schema import generate_schema
from docker import manage_docker_containers, run_docker_compose
from front.datagrids import generate_angular_components
from front.services import generate_angular_services
from init_project import init_project
from name import demander_nom_projet, generate_description

# Fonction pour enregistrer les réponses dans un fichier JSON
def enregistrer_reponses(fichier, reponses):
    with open(fichier, "w") as f:
        json.dump(reponses, f, indent=4)
    print(f"Les réponses ont été enregistrées dans le fichier {fichier}")

# Fonction principale qui pose les questions et enregistre les réponses
def main():
    # Liste des questions à poser
    questions = [
        "Pourquoi ce logiciel est-il nécessaire ? (quels problèmes ou besoins il résout ?)",
        "Qui sont les utilisateurs principaux du logiciel ?",
        "Où les utilisateurs utiliseront-ils le logiciel ? (au bureau, en télétravail, sur mobile, etc.)",
        "Que doit accomplir concrètement le logiciel? (objectifs globaux et spécifiques)",
        "Quelles sont les principales entités que le logiciel doit gérer ? (clients, commandes, produits, etc.)",
        "Quoi sont les informations spécifiques que chaque entité doit contenir ? (détails à capturer pour chaque entité)",
        "Comment les données sont-elles collectées, modifiées et supprimées dans le logiciel ?",
        "Quand se produisent les principaux événements métiers dans le logiciel ? (création de commande, validation d’un ticket)",
        "Quand les utilisateurs doivent-ils recevoir des notifications ou des alertes ? (changement de statut, deadlines)"
    ]

    # Dictionnaire pour stocker les réponses
    reponses = {}

    # Boucle pour poser les questions et stocker les réponses
    for question in questions:
        reponses[question] = poser_question(question)

    # Générer une description du projet
    description = generate_description(reponses)
    reponses["description"] = description

    # Demander le nom du projet
    nom_projet = demander_nom_projet(description)
    reponses["name"] = nom_projet

    # Enregistrer les réponses dans un fichier caché au format JSON
    fichier_cache = os.path.join(os.getcwd(), ".reponses_logiciel.json")
    enregistrer_reponses(fichier_cache, reponses)

    # Initialiser le projet avec les réponses obtenues
    base_url = "https://example.com/repo/"
    init_project(nom_projet, base_url)

    # Créer le fichier DBML
    schema_path = generate_schema(reponses)

    # Créer les modèles
    models_directory = generate_csharp_models(schema_path)

    # Créer les DTOs
    update_models_with_dtos(models_directory)

    # Générer les Controllers à partir des modèles
    controllers_directory = "./controllers"  # Dossier de destination pour les fichiers Controller
    generate_controllers_from_models(models_directory, controllers_directory)

    # Créer les services
    openapi_file = "./openapi.json"  # Chemin vers votre fichier OpenAPI JSON généré par l'API C# .NET
    output_directory = "./src/app/services"  # Dossier de destination pour les services Angular

    generate_angular_services(openapi_file, output_directory)

    # Créer les datagrid
    models_directory = "./models"  # Répertoire contenant les fichiers C# des modèles
    angular_directory = "./src/app/components"  # Répertoire où les composants Angular seront générés
    generate_angular_components(models_directory, angular_directory)  # Générer des composants Angular pour chaque modèle C# trouvé

    # Créer les formulaires

    # Créer la page de connexion

    # Lancer l'App
    run_docker_compose()
    manage_docker_containers()


# Appel de la fonction main
if __name__ == "__main__":
    main()
