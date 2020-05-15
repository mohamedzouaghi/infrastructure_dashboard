import datetime


from django.db import models
from django.utils.html import mark_safe
from django.conf import settings


from django.utils import timezone


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

class PaymentType(models.Model):
  # Who should pay the server
  label = models.CharField('Type', max_length=200)
  description = models.TextField('description', null=True, blank=True)
  
  def __str__(self):
      return self.label

# TODO(mz@)  Add status model for simple monitoring
#class ServerStatus(models.Model):
#  server = models.ForeignKey(ServerDetails, on_delete=models.CASCADE)
#
#  def last_ping_status(self):
#    # TODO(mz@) add code to check ping status here
#    return 'Unkown'
#  
#  def last_seen_activity(self):
#    # TODO(mz@) add code to check ping status here
#    return 'Unkown' 


class ServerDetails(models.Model):
  server_name = models.CharField('Server Name', max_length=200, default='')
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  provider = models.ForeignKey(ServerProvider, on_delete=models.CASCADE, null=True)
  payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, null=True)
  
  ip_address = models.GenericIPAddressField('IP Address', null=True, blank=True)
  linked_domain = models.CharField('Linked Domain', max_length=200, null=True,
                                   blank=True)
  environment_type = models.CharField('Environment', choices=SERVER_ENV_TYPES,
                                      max_length=1)
  monthly_mount = models.PositiveIntegerField('Monthly Cost', null=True, blank=True)
  expires_on = models.DateField('Expires on', null=True, blank=True)
  comments = models.TextField('Comments', null=True, blank=True)
  admin_server_url = models.URLField('Admin Server URL', null=True, blank=True)

  separate_bill = models.BooleanField('Separate Bill?', default=False, blank=True)
  seperate_bill_file = models.ImageField('Bill file', upload_to='bills', null=True, blank=True)
  
  def still_valid(self):
    if not self.expires_on:
      return False
    # TODO (mz@): set this to True when contract is of a type "Paid by customer"
    return self.expires_on >= datetime.date.today() + datetime.timedelta(days=30)
  
  still_valid.admin_order_field = 'expires_on'
  still_valid.boolean = True
  still_valid.short_description = 'Still valid (not expired)?'
  
  # Below is an attempt to display the image within the admin page
  def image_tag(self):
    return mark_safe('<img src="%s%s" width="150" height="150" />' % ( settings.MEDIA_URL, self.seperate_bill_file))

  image_tag.short_description = 'Bill image'

  def __str__(self):
    return str(self.project.name) + '---' + str(self.ip_address)
  
  def last_ping_status(self):
    # TODO(mz@) add code to check ping status here
    return 'Unkown'
  
  def last_seen_activity(self):
    # TODO(mz@) add code to check ping status here
    return 'Unkown'   

    
    
    