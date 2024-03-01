from django.contrib import admin

from main.models import *

admin.site.register(AboutUsModel)
admin.site.register(ProductsModel)
admin.site.register(TechnologiesModel)
admin.site.register(ServiceItemsModel)


class ServiceItemsInline(admin.StackedInline):
    model = ServiceItemsModel
    extra = 1


@admin.register(ServiceModel)
class ServiceModel(admin.ModelAdmin):
    list_display = [field.name for field in ServiceModel._meta.fields]
    # inlines = [ServiceItemsInline]
    

admin.site.register(DocumentsModel)
admin.site.register(ContactsModel)
admin.site.register(OurPartnersModel)
admin.site.register(OurStatisticsModel)
# admin.site.register()
