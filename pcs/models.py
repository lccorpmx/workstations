from django.db import models

class workstationuser(models.Model):
    cpu = models.TextField(blank=True)
    gpu = models.TextField(blank=True)
    ram = models.TextField(blank=True)
    mobo = models.TextField(blank=True)
    psu = models.TextField(blank=True)
    data = models.TextField(blank=True)
    gabo = models.TextField(blank=True)
    monitor = models.TextField(blank=True)
    teclado = models.TextField(blank=True)
    mouse = models.TextField(blank=True)



    