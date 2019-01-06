from django.db import models

class Deployer(models.Model):
    queue_id = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.queue_id