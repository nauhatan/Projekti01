from django.db import models

# Create your models here.
class Kysymys(models.Model):
    kysymys_txt = models.CharField(max_length=100)
    julkaisu_pvm = models.DateTimeField("julkaisu pvm")

    def __str__(self):
        return self.kysymys_txt


class Vaihtoehto(models.Model):
    vaihtoehto_txt = models.CharField(max_length=200)
    valinta = models.IntegerField(default=0)
    kysymys = models.ForeignKey(Kysymys, on_delete=models.CASCADE)

    def __str__(self):
        return self.vaihtoehto_txt
