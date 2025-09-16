from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(
            title="Titre test",
            content="Contenu test",
            pseudonym="Testeur",
            email="test@example.com",
            telephone="0600000000"
        )
        self.assertEqual(str(post), "Titre test")
        self.assertEqual(post.pseudonym, "Testeur")

class CommentModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Titre", content="Contenu")

    def test_create_comment(self):
        comment = Comment.objects.create(
            post=self.post,
            author_pseudonym="Commentateur",
            content="Un commentaire"
        )
        self.assertIn("Commentaire par Commentateur", str(comment))
        self.assertEqual(comment.post, self.post)

class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(title="API Post", content="API Content")

    def test_list_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_create_post(self):
        data = {
            "title": "Nouveau post",
            "content": "Contenu du post",
            "pseudonym": "Anon"
        }
        response = self.client.post(reverse('post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Nouveau post")

class CommentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post = Post.objects.create(title="API Post", content="API Content")

    def test_create_comment(self):
        data = {
            "post": self.post.id,
            "author_pseudonym": "Anon",
            "content": "Commentaire API"
        }
        response = self.client.post(reverse('comment-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["author_pseudonym"], "Anon")