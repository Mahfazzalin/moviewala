from django.contrib import admin
from listing_details.models import movie_details


# Register your models here.
class movie_detailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_link', 'language', 'subtitle', 'textbox', 'd_link', 'ss_1', 'ss_2', 'ss_3', 'ss_4')


admin.site.register(movie_details, movie_detailsAdmin)
