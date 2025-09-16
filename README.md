# AnonymPost Backend

API Django REST pour la publication et la gestion de posts anonymes et de leurs commentaires.

## Fonctionnalités

- Création, lecture, modification et suppression de posts anonymes
- Ajout et gestion de commentaires sur chaque post
- API RESTful avec navigation web (Django REST Framework)
- Tests unitaires pour les modèles et l’API
- Prêt pour le déploiement Docker/Kubernetes

## Installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/ABODJI-Kondi-Kaled/anonympost
   cd anonympost/backend
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

## API

- **Posts** : `/api/posts/`
- **Commentaires** : `/api/comments/`

L’API supporte les opérations : GET, POST, PATCH, DELETE.

## Tests

Pour lancer les tests :

```bash
python manage.py test postmanager
```

## Déploiement Docker/Kubernetes

- Dockerfile et exemples de fichiers Kubernetes fournis.
- Compatible avec Minikube ou kind pour le déploiement local.

## Contribuer

Les contributions sont les bienvenues !  
N’hésitez pas à ouvrir une issue ou une pull request.

---

**Auteur** : ABODJI Kondi Kalèd  
**Licence** : MIT
