from django.db import models

class Case(models.Model):
    custom_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=150, default='')
    data_category = models.CharField(max_length=50, default='web')
    short_description = models.CharField(max_length=150, default='')
    project = models.CharField(max_length=150)
    language_framework = models.CharField(max_length=200, default='HTML, CSS, JavaScipt')
    client = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)
    preview_url = models.URLField(default='https://spindola.engineer')
    description = models.TextField()
    card_img_url = models.URLField()
    modal_img_url = models.URLField()

    def __str__(self):
        return self.title