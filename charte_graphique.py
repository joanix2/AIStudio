from ask import poser_question


def definir_charte_graphique():
    # Couleurs
    couleurs_principales = poser_question(
        "Quelle est la couleur principale de la marque (couleur dominante) ?", 
        "#3498db"  # Par défaut : bleu clair
    )
    couleurs_secondaires = poser_question(
        "Quelle est la couleur secondaire (pour les éléments de support) ?", 
        "#2ecc71"  # Par défaut : vert clair
    )
    couleurs_arriere_plan = poser_question(
        "Quelle est la couleur de l'arrière-plan ?", 
        "#ffffff"  # Par défaut : blanc
    )
    
    # Icônes
    style_icones = poser_question(
        "Quel style d'icônes préférez-vous (ligne, rempli, plat, etc.) ?", 
        "ligne"  # Par défaut : ligne
    )
    
    # Boutons
    forme_boutons = poser_question(
        "Quelle forme de boutons souhaitez-vous (arrondis, rectangulaires) ?", 
        "arrondis"  # Par défaut : arrondis
    )
    couleurs_boutons = poser_question(
        "Quelle couleur pour les boutons (couleurs d'accent) ?", 
        "#e74c3c"  # Par défaut : rouge vif
    )
    couleur_erreur_annulation = poser_question(
        "Quelle couleur pour les boutons d'erreur ou d'annulation ?", 
        "#e74c3c"  # Par défaut : rouge
    )
    
    styles_etats_boutons = poser_question(
        "Quelles sont les couleurs pour les différents états des boutons (normal, survolé, cliqué, désactivé) ?",
        "normal: #3498db, survolé: #2980b9, cliqué: #1abc9c, désactivé: #bdc3c7"
        # Par défaut : différentes nuances de bleu et gris
    )
    
    # Résumé de la charte graphique
    charte_graphique = {
        "Couleurs principales": couleurs_principales,
        "Couleurs secondaires": couleurs_secondaires,
        "Couleurs d'arrière-plan": couleurs_arriere_plan,
        "Style des icônes": style_icones,
        "Forme des boutons": forme_boutons,
        "Couleurs des boutons": couleurs_boutons,
        "Couleur erreur/annulation": couleur_erreur_annulation,
        "Styles d'état des boutons": styles_etats_boutons
    }
    
    # Afficher la charte graphique définie
    print("\nCharte graphique définie :")
    for cle, valeur in charte_graphique.items():
        print(f"- {cle}: {valeur}")
    
    return charte_graphique

# Exécution de la fonction
charte_graphique = definir_charte_graphique()
