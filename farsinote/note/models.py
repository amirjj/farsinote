from django.db import models


class Note(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=600)
    created_date = models.DateTimeField('Create date')
    tag = models.CharField(max_length=200)
    body = models.TextField()
    is_deleted = models.BooleanField(default=False)

