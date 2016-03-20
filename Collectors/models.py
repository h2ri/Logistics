from django.db import models

# Create your models here.
class PostalCode(models.Model):
    postalCode = models.IntegerField(primary_key=True)
    Locality = models.CharField(max_length=255,blank=True,null=True)
    Active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.postalCode)

class Collectors(models.Model):
    name = models.CharField(max_length=200)
    addressLatitude = models.FloatField(blank=True,null=True)
    addressLogitude = models.FloatField(blank=True,null=True)


class Clients(models.Model):
    #riders = models.ForeignKey(Collec, related_name='riders',null=True)
    postalCode = models.ForeignKey(PostalCode, related_name='postal_Code')
    name = models.CharField(max_length=200)
    addressLatitude = models.FloatField(blank=True,null=True)
    addressLogitude = models.FloatField(blank=True,null=True)



class CollectorPinCodeRelation(models.Model):
    postalCode = models.ForeignKey(PostalCode, related_name='Collection_postal_Code')
    collector = models.ForeignKey(Collectors,related_name='acollectors')
