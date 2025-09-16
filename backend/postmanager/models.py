from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



class Post(models.Model):
    """
    Modèle pour une histoire anonyme.
    """
    title = models.CharField(max_length=255, help_text="Le titre accrocheur de votre histoire.")
    content = models.TextField(help_text="Le contenu de l'histoire. Soyez juteux !")
    pseudonym = models.CharField(max_length=75, blank=True, null=True, help_text="Un pseudonyme si vous souhaitez en utiliser un.")
    email = models.EmailField(blank=True, null=True, help_text="Votre email (optionnel, pour les notifications).")
    telephone = models.CharField(max_length=20, blank=True, null=True, help_text="Votre numéro de téléphone (optionnel).")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at'] # Affiche les histoires les plus récentes en premier

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Modèle pour les commentaires sur une histoire.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', help_text="L'histoire à laquelle ce commentaire est rattaché.")
    author_pseudonym = models.CharField(max_length=75, blank=True, null=True, help_text="Pseudonyme de l'auteur du commentaire.")
    content = models.TextField(max_length=1000, help_text="Le contenu du commentaire.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at'] # Affiche les commentaires les plus anciens en premier

    def __str__(self):
        return f'Commentaire par {self.author_pseudonym or "Anonyme"} sur {self.post.title}'