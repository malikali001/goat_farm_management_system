import uuid

from base.models.custom_users import CustomUser
from django.db import models


class Goat(models.Model):
    name = models.UUIDField(unique=True, default=uuid.uuid4)
    breed = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
