from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

from datetime import datetime

# Create your models here.


class Address(models.Model):
    street = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    city = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    country = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"


class Country(models.Model):
    name = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class User(models.Model):
    username = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        related_name="users"
    )
    country = models.ManyToManyField(
        Country,
        related_name="users"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name_plural = "Users"


class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, related_name="todos"
    )
    title = models.CharField(
        max_length=64,
        validators=[MaxLengthValidator(64)]
    )
    description = models.TextField(blank=False)
    level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    necessary_time = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        if (self.completed):
            return "Completed"
        else:
            return "Doing"

    def save(self, *args, **kwargs):
        if (self.title == None or self.title == ""):
            raise ValueError("Title is required")
        if (self.description == None or self.description == ""):
            raise ValueError("Description is required")

        super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Todos"
