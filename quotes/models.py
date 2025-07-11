from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text[:50]}" - {self.author}'
