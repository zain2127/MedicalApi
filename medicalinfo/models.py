from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    specialtiy = models.CharField(max_length=200)
    rating=models.IntegerField()
    image=models.ImageField(null=True)

    def __str__(self):
        return self.name + ' ' + self.education
    
class Medicine(models.Model):
    drugname = models.CharField(max_length=200)
    dosage_form=models.CharField(max_length=200) 
    dosageStrength = models.FloatField()
    indications=models.CharField(max_length=200)
    contradictions=models.CharField(max_length=1200)
    side_effect=models.CharField(max_length=200)
    storage=models.CharField(max_length=200)
    image=models.ImageField(null=True)

    def __str__(self):
        return self.drugname
    