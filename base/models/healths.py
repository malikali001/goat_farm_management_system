from base.models.custom_users import CustomUser
from django.db import models
from base.models.goats import Goat


class Health(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    description = models.TextField()
    treatment = models.CharField(max_length=150)
    goat = models.ForeignKey(Goat, on_delete=models.CASCADE)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
