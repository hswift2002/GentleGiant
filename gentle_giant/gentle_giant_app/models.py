from django.db import models

# Create your models here.
class Scoreboard(models.Model):
    user_id = models.AutoField(primary_key= True)
    user_name = models.CharField(max_length= 3)
    user_score = models.IntegerField()

    def __str__(self):
        return self.user_name