from django.contrib import admin

from .models import Project, ServerDetails, ServerProvider

#admin.site.register(ServerDetails)
admin.site.register(ServerProvider)


class ServerAdmin(admin.ModelAdmin):
  # List page
  list_display = ('project', 'provider', 'ip_address', 'linked_domain',
                  'monthly_mount', 'environment_type', 'expires_on', 'comments',
                  'admin_server_url', 'separate_bill', 'seperate_bill_file')
  search_fields = ['ip_address', 'linked_domain', 'project__name']
  list_filter = ['project__name', 'linked_domain', 'separate_bill', 
                 'monthly_mount', 'separate_bill', 'environment_type']
  
  #fields = ['image_tag']
  #readonly_fields = ['image_tag']
  
  # CRUD page  
  #fieldsets = [
  #    (None,               {'fields': ['project']}),
  #    ('More information', {'fields': ['ip_address', 'linked_domain']}),
  #]


class ServerInline(admin.StackedInline):
    model = ServerDetails
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
#  fields = ['project', 'ip_address', 'linked_domain']
  fieldsets = [
      (None,               {'fields': ['name']}),
      #('More information', {'fields': ['ip_address', 'linked_domain']}),
  ]
  inlines = [ServerInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ServerDetails, ServerAdmin)