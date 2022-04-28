from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Category(models.Model):
    NAME_MAX_LEN = 25

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    is_done = models.BooleanField(
        default=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
