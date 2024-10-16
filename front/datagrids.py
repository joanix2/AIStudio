import os

# Fonction pour générer les composants Angular avec DataGrid pour chaque modèle C#
def generate_angular_components(models_directory, angular_directory):
    if not os.path.exists(models_directory):
        print(f"Le répertoire des modèles C# '{models_directory}' n'existe pas.")
        return
    
    if not os.path.exists(angular_directory):
        print(f"Le répertoire Angular '{angular_directory}' n'existe pas.")
        return
    
    # Parcourir chaque fichier modèle .cs dans le répertoire des modèles
    for file_name in os.listdir(models_directory):
        if file_name.endswith(".cs"):
            model_name = file_name.replace(".cs", "")  # Récupérer le nom du modèle sans l'extension .cs
            
            # Générer le nom du composant Angular en kebab-case (nom-modèle-page)
            angular_component_name = f"{model_name.lower()}-page"
            
            # Créer le répertoire pour le composant dans le répertoire Angular
            component_dir = os.path.join(angular_directory, angular_component_name)
            if not os.path.exists(component_dir):
                os.makedirs(component_dir)
            
            # Générer les fichiers TypeScript, HTML, et CSS pour le composant Angular
            generate_ts_file(component_dir, model_name, angular_component_name)
            generate_html_file(component_dir, model_name)
            generate_css_file(component_dir)

            print(f"Composant '{angular_component_name}' généré avec succès.")

# Générer le fichier TypeScript du composant
def generate_ts_file(component_dir, model_name, angular_component_name):
    ts_content = f"""
import {{ Component, OnInit }} from '@angular/core';

@Component({{
  selector: 'app-{angular_component_name}',
  templateUrl: './{angular_component_name}.component.html',
  styleUrls: ['./{angular_component_name}.component.css']
}})
export class {model_name}PageComponent implements OnInit {{
  apiUrl: string = 'https://your-api-url.com/api/{model_name.lower()}';  // URL de l'API pour {model_name.lower()}

  constructor() {{ }}

  ngOnInit(): void {{
  }}
}}
"""
    ts_file_path = os.path.join(component_dir, f"{angular_component_name}.component.ts")
    with open(ts_file_path, "w") as ts_file:
        ts_file.write(ts_content)

# Générer le fichier HTML du composant
def generate_html_file(component_dir, model_name):
    html_content = f"""
<h2>{model_name}</h2>
<app-generic-data-grid [apiUrl]="apiUrl"></app-generic-data-grid>
"""
    html_file_path = os.path.join(component_dir, f"{model_name.lower()}-page.component.html")
    with open(html_file_path, "w") as html_file:
        html_file.write(html_content)

# Générer un fichier CSS vide (optionnel, peut être personnalisé plus tard)
def generate_css_file(component_dir):
    css_content = """
/* Styles spécifiques pour le composant DataGrid */
"""
    css_file_path = os.path.join(component_dir, f"{os.path.basename(component_dir)}.component.css")
    with open(css_file_path, "w") as css_file:
        css_file.write(css_content)

# Exemple d'utilisation
def main():
    models_directory = "./models"  # Répertoire contenant les fichiers C# des modèles
    angular_directory = "./src/app/components"  # Répertoire où les composants Angular seront générés

    # Générer des composants Angular pour chaque modèle C# trouvé
    generate_angular_components(models_directory, angular_directory)

if __name__ == "__main__":
    main()
