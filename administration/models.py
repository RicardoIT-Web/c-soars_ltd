from django.db import models


class File(models.Model):
    """ Model for managing files so User can access """
    title = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    pdf = models.FileField(upload_to='media/files/pdfs/')

    def __str__(self):
        return self.title

    def remove(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
