from django.db import models

# Create your models here.
class Estimate(models.Model):
    user = models.CharField(max_length=30)
    localite = models.CharField(max_length=100)
    nombre_de_personnes  = models.IntegerField()
    nbre_etoile_hotel  = models.IntegerField()
    forme_de_tourisme = models.CharField(max_length=100)
    emails = models.EmailField()
    nombre_de_lieux_a_visiter  = models.IntegerField()
    types_de_transport = models.CharField(max_length=200)
    commentaires = models.TextField(max_length=500)
    
    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.user,
                                          self.localite,
                                          self.nombre_de_personnes,
                                          self.nbre_etoile_hotel,
                                          self.forme_de_tourisme,
                                          self.emails,
                                          self.nombre_de_lieux_a_visiter,
                                          self.types_de_transport,
                                          self.commentaires)