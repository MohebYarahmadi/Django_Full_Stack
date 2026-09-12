from django.db import models
# from django.db.models import UniqueConstraint

from apps.abstracts.models import AbstractModel, AbstractManager


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey('apps_posts.Post', on_delete=models.PROTECT)
    author = models.ForeignKey('apps_users.User', on_delete=models.PROTECT)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    class Meta:
        db_table = "apps.comments"
        constraints = [
            models.UniqueConstraint(
                fields=["post", "author"], name="unique_post_per_author"
            )
        ]

    def __str__(self):
        return self.author.name
