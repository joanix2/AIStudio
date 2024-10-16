import os

# Fonction d'initialisation du projet Angular et API avec Docker
def init_project(nom_projet, base_url):
    # Construire la commande shell pour initialiser le projet
    init_command = f"./init_project.sh {nom_projet} {base_url}"
    
    # Exécuter la commande shell pour lancer l'initialisation
    os.system(init_command)