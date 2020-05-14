from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


SERVER_ENV_TYPES = (
            ('D','Development'),
            ('S','Staging'),
            ('P','Production'),
            ('T','Training'),
            ('M','Demo'),
            )

class Project(models.Model):
  name = models.CharField('Project Name', max_length=200) # Project name
  
  def __str__(self):
      return self.name
 
class ServerProvider(models.Model):
  # Example GCP, DO, Amazon...
  name = models.CharField('Provider Name', max_length=200)
  
  def __str__(self):
      return self.name

class ServerDetails(models.Model):
  server_name = models.CharField('Server Name', max_length=200, default='')
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  provider = models.ForeignKey(ServerProvider, on_delete=models.CASCADE, null=True)
  ip_address = models.GenericIPAddressField('IP Address', null=True, blank=True)
  linked_domain = models.CharField('Linked Domain', max_length=200, null=True,
                                   blank=True)
  environment_type = models.CharField('Environment', choices=SERVER_ENV_TYPES,
                                      max_length=1)
  monthly_mount = models.PositiveIntegerField('Monthly Amount', null=True, blank=True)
  expires_on = models.DateField('Expires on', null=True, blank=True)
  comments = models.TextField('Comments', null=True, blank=True)
  admin_server_url = models.URLField('Admin Server URL', null=True, blank=True)

  separate_bill = models.BooleanField('Separate bill?', default=False, blank=True)
  seperate_bill_file = models.ImageField('Bill file', upload_to='bills', null=True, blank=True)
  
  def image_tag(self):
    return mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_ROOT, self.seperate_bill_file))

  image_tag.short_description = 'Image'

  def __str__(self):
      return str(self.project.name) + '---' + str(self.ip_address)
    
    
    