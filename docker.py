import docker
import os

def run_docker_compose():
    client = docker.from_env()  # Créer un client Docker basé sur l'environnement

    # Vérifier si docker-compose.yml existe
    compose_file = "docker-compose.yml"
    if not os.path.exists(compose_file):
        print(f"Le fichier {compose_file} est introuvable.")
        return

    try:
        # Démarrer les services à partir du fichier docker-compose.yml
        output = client.containers.run(
            "docker/compose:1.29.2",  # Utilise l'image officielle docker-compose
            f"up -d",  # Commande docker-compose
            volumes={
                os.path.abspath("."): {
                    "bind": "/workspace", "mode": "rw"
                }
            },
            working_dir="/workspace",
            remove=True,
            tty=True
        )
        print(output.decode("utf-8"))
        print("Conteneurs lancés avec succès.")
    except Exception as e:
        print(f"Erreur lors du lancement de docker-compose : {e}")

def manage_docker_containers():
    # Créer un client Docker
    client = docker.from_env()

    # Lancer un nouveau conteneur
    try:
        print("Démarrage du conteneur...")
        container = client.containers.run(
            "nginx",  # Remplace par l'image de ton choix
            detach=True,  # Exécute en arrière-plan
            ports={'80/tcp': 8080},  # Redirige le port 80 du conteneur vers le port 8080 de la machine hôte
            name="my_nginx_container"
        )
        print(f"Conteneur {container.name} démarré.")
    except docker.errors.ContainerError as e:
        print(f"Erreur lors du démarrage du conteneur : {e}")

    # Afficher tous les conteneurs en cours d'exécution
    containers = client.containers.list()
    print("Conteneurs en cours d'exécution :")
    for c in containers:
        print(f"{c.name} - {c.status}")

    # Arrêter et supprimer le conteneur
    container = client.containers.get("my_nginx_container")
    container.stop()
    container.remove()
    print(f"Conteneur {container.name} arrêté et supprimé.")
