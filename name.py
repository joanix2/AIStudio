# Fonction pour demander si le projet a un nom et gérer la génération de noms
from ask import poser_question
from textGen import appeler_openai, generate_name


def demander_nom_projet(description):
    a_un_nom = poser_question("Le projet a-t-il déjà un nom ? (oui/non)")
    
    if a_un_nom.lower() == "oui":
        nom_projet = poser_question("Quel est le nom du projet ?")
    else:
        # Générer des idées de noms à partir des réponses précédentes
        suggestions = generate_name(description)
        print("Voici quelques suggestions de noms pour le projet :")
        for suggestion in suggestions:
            print(f"- {suggestion}")
        
        # Demander un nom après les suggestions
        nom_projet = poser_question("Quel nom souhaitez-vous donner au projet ? (choisissez parmi les suggestions ou entrez un nouveau nom)")
    
    return nom_projet

def generate_description(answer_json):
    system = "You are a helpful assistant specialized in generating creative app names."
    user = f"Generate creative app names for an application described as: {answer_json}"
    return appeler_openai(system, user)

def generate_name(description_projet):
    system = "You are a helpful assistant specialized in generating creative app names."
    user = f"Generate creative app names for an application described as: {description_projet}"
    return appeler_openai(system, user)