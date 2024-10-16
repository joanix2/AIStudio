import os
import subprocess

# Fonction pour vérifier si ng-openapi-gen est installé
def check_ng_openapi_gen_installed():
    try:
        # Vérifie si ng-openapi-gen est accessible via la ligne de commande
        result = subprocess.run(["npx", "ng-openapi-gen", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("ng-openapi-gen est installé.")
            return True
        else:
            print("ng-openapi-gen n'est pas installé. Exécutez 'npm install ng-openapi-gen --save-dev' pour l'installer.")
            return False
    except FileNotFoundError:
        print("ng-openapi-gen n'est pas installé. Exécutez 'npm install ng-openapi-gen --save-dev' pour l'installer.")
        return False

# Fonction pour générer les services Angular à partir du fichier OpenAPI JSON
def generate_angular_services(openapi_file, output_dir="./src/app/services"):
    # Vérifier si ng-openapi-gen est installé
    if not check_ng_openapi_gen_installed():
        return
    
    # Vérifier si le fichier OpenAPI JSON existe
    if not os.path.exists(openapi_file):
        print(f"Le fichier OpenAPI '{openapi_file}' est introuvable.")
        return
    
    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Le dossier de destination '{output_dir}' a été créé.")
    
    # Générer les services Angular à partir du fichier OpenAPI JSON
    try:
        command = ["npx", "ng-openapi-gen", "--input", openapi_file, "--output", output_dir]
        print(f"Exécution de la commande : {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Les services Angular ont été générés avec succès dans le dossier '{output_dir}'.")
        else:
            print(f"Erreur lors de la génération des services Angular : {result.stderr}")
    
    except Exception as e:
        print(f"Une erreur est survenue lors de la génération des services Angular : {e}")

# Exemple d'utilisation
def main():
    openapi_file = "./openapi.json"  # Chemin vers votre fichier OpenAPI JSON généré par l'API C# .NET
    output_directory = "./src/app/services"  # Dossier de destination pour les services Angular

    generate_angular_services(openapi_file, output_directory)

if __name__ == "__main__":
    main()
