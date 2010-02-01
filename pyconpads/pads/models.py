from django.db import models

# Create your models here.
class Pad(models.Model):
    id = models.CharField(max_length=128, primary_key=True, db_column='ID')
    json = models.TextField(db_column='JSON')
    
    class Meta:
        db_table = 'PAD_APOOL'
        managed = False
        
    def __unicode__(self):
        return self.id