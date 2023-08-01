from django.db import models

# Create your models here.
STYLE_CHOICES = [('bild', 'Bold'), ('underline', 'Underline'), ('friendly', 'Friendly')]
LANGUAGE_CHOICES = (('python', 'Python'), ('js', 'JavaScript'), ('java', 'Java'))


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
