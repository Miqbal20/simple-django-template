from django.contrib import admin
from mainsite.models import Data, State


# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name', 'age']
    list_filter = ('id_province',)
    list_per_page = 10


admin.site.register(Data, DataAdmin)
admin.site.register(State)

