from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=120)
    level = models.PositiveSmallIntegerField(default=3, help_text="1-5 scale")
    icon = models.CharField(max_length=60, blank=True, help_text="Optional emoji or icon name")

    class Meta:
        ordering = ["-level", "name"]

    def __str__(self) -> str:
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=160)
    company = models.CharField(max_length=160)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self) -> str:
        return f"{self.role} @ {self.company}"
