from django.contrib import admin
from calculator.models import StringSet, String


class StringSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user',)
    #search_fields = ('name', 'user',)

class StringAdmin(admin.ModelAdmin):
    list_display = ('string_set', 'string_number', 'scale_length', 'note', 'octave', 'gauge', 'string_type',)
    #search_fields = ('string_set', 'string_number', 'scale_length', 'note', 'octave', 'gauge', 'string_type',)

admin.site.register(StringSet, StringSetAdmin)
admin.site.register(String, StringAdmin)
