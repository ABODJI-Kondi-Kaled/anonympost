from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    """
    Permet d'afficher et de gérer les commentaires directement
    depuis la page d'administration d'un Post.
    """
    model = Comment
    extra = 0  # N'affiche pas de formulaire de commentaire vide par défaut
    readonly_fields = ('author_pseudonym', 'content', 'created_at')
    can_delete = True # Permet de supprimer des commentaires depuis le Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Post.
    """
    list_display = ('title', 'pseudonym', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'pseudonym')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [CommentInline] # Intègre la gestion des commentaires

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configuration de l'interface d'administration pour le modèle Comment.
    """
    list_display = ('post', 'author_pseudonym', 'created_at', 'short_content')
    list_filter = ('created_at',)
    search_fields = ('content', 'author_pseudonym', 'post__title')
    readonly_fields = ('created_at', 'post')

    def short_content(self, obj):
        """Retourne un aperçu du contenu du commentaire."""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Aperçu du commentaire'
