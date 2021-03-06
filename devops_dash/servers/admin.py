from django.contrib import admin

from .models import Project, ServerDetails, ServerProvider, PaymentType


class ServerAdmin(admin.ModelAdmin):
  # List page
  list_display = ('server_name', 'project', 'provider', 'last_ping_status', 'last_seen_activity', 'payment_type', 'ip_address', 'linked_domain',
                  'monthly_mount', 'environment_type', 'expires_on', 'still_valid', 'comments',
                  'admin_server_url', 'separate_bill', 'seperate_bill_file', 'image_tag')
  search_fields = ['project__name', 'server_name', 'provider__name', 'ip_address', 'linked_domain',
                  'monthly_mount', 'environment_type', 'expires_on', 'comments',
                  'admin_server_url', 'separate_bill']
  list_filter = ['project__name', 'payment_type__label', 'linked_domain', 'separate_bill', 
                 'monthly_mount', 'environment_type']
    
  # Below is mandatory for calculated fields
  readonly_fields = ['image_tag', 'still_valid']
  
  # CRUD page  
  fieldsets = [
      ('Project',               {'fields': ['project']}),
      ('General information', {'fields': ['provider', 'environment_type', 'server_name', 'ip_address', 'linked_domain', 'admin_server_url']}),
      ('Subscriptions', {'fields': ['payment_type', 'separate_bill', 'monthly_mount', 'expires_on', 'still_valid', 'image_tag', 'seperate_bill_file']}),
      ('Misc', {'fields': ['comments']}),
  ]


class ServerInline(admin.StackedInline):
    model = ServerDetails
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['name']}),
  ]
  inlines = [ServerInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ServerDetails, ServerAdmin)
admin.site.register(PaymentType)
admin.site.register(ServerProvider)


