from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FilesUploaded(models.Model):
      title = models.CharField(max_length=200)
      fileUploaded = models.FileField(upload_to='uploads/',help_text='the file')
      fileFormat = models.CharField(max_length = 255)
      def __unicode__(self):
        return self.title
        
        

