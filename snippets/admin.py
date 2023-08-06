from django.contrib import admin
from snippets.models import Snippet, Profile, Product, Collection, ProductCollection, Album, Track

admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Snippet)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(ProductCollection)
