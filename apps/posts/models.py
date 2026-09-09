from django.db import models

from apps.abstracts.models import AbstractModel, AbstractManager


# ================================
#   Post Manager
# ================================
class PostManager(AbstractManager):
    pass


# ================================
#   Post Model
# ================================
class Post(AbstractModel):
    author = models.ForeignKey(to='apps_users.User', on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = PostManager()

    class Meta:
        db_table = "'apps.posts'"

    def __str__(self):
        return f'{self.author.name}'
