from django.contrib import admin
from .models  import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('document', 'name', 'first_surname', 'last_surname')


admin.site.register(Person, PersonAdmin)
