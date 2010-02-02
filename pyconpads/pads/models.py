from django.db import models
from django.conf import settings

# Create your models here.
class Pad(models.Model):
    id = models.CharField(max_length=128, primary_key=True, db_column='ID')
    json = models.TextField(db_column='JSON')
    
    class Meta:
        db_table = 'PAD_APOOL'
        managed = False
        
    def __unicode__(self):
        return self.id
        
    def etherpad_url(self):
        return settings.ETHERPAD_URL + self.id
        
class PadMeta(models.Model):
    pad = models.OneToOneField(Pad)
    name = models.CharField(max_length=500, blank=True)
    talk_time = models.DateTimeField(null=True, blank=True)
    hide = models.BooleanField(default=False)