from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.level})"

class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    button_text = models.CharField(max_length=50, default='Contact Me')
    button_link = models.URLField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)

    def __str__(self):
        return "Hero Section"


class About(models.Model):
    heading = models.CharField(max_length=200, default="About Me")
    description = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return "About Me Section"
