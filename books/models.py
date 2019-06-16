from django.db import models

# Create your models here.

class Book (models.Model):
    title=models.CharField(max_length=70)
    author=models.CharField(max_length=150,help_text="Use Pen Name not your real Name")
    review=models.TextField(blank=True,null=True)
    date_reviewed=models.DateTimeField(blank=True,null=True)
    is_favourite=models.BooleanField(default=False,verbose_name="Favourite?")

    def __str__(self):
        return self.title
