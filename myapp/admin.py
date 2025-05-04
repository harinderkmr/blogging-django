from django.contrib import admin
from .models import Post,Comment,Contact, Category



# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
# myapp/admin.py

admin.site.register(Category)



admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'
