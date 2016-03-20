from django.contrib import admin
from models import PostalCode,Collectors,Clients,CollectorPinCodeRelation

class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('postalCode','Locality','Active')

class CollectorsAdmin(admin.ModelAdmin):
    list_display = ('name','addressLatitude','addressLogitude',)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name','addressLatitude','addressLogitude','postalCode')

admin.site.register(PostalCode,PostalCodeAdmin)
admin.site.register(Collectors,CollectorsAdmin)
admin.site.register(Clients,ClientsAdmin)
admin.site.register(CollectorPinCodeRelation)