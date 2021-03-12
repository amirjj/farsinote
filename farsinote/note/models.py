from django.db import models
import datetime
from django.urls import reverse


class Note(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=600)
    created_date = models.DateTimeField('Create date')
    tag = models.CharField(max_length=200)
    body = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.created_date = datetime.datetime.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


