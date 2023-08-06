from django.db import models


STYLE_CHOICES = [('bild', 'Bold'), ('underline', 'Underline'), ('friendly', 'Friendly')]
LANGUAGE_CHOICES = (('python', 'Python'), ('js', 'JavaScript'), ('java', 'Java'))


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='snippet_owner', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ': ' + self.title


# O2O ---
class Profile(models.Model):
    user = models.OneToOneField('auth.User',related_name='user_profile', on_delete=models.CASCADE)
    aadhar_no = models.IntegerField()


# M2O ---
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='album_owner', on_delete=models.CASCADE)

# M2O
class Track(models.Model):
    album = models.ForeignKey(Album, related_name='track_album', on_delete=models.CASCADE)
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='track_owner', on_delete=models.CASCADE)



# M2M ---
class Product(models.Model):
    name = models.CharField(max_length=20)

class Collection(models.Model):
    name = models.CharField(max_length=20)
    prod_coll = models.ManyToManyField(Product, through='ProductCollection', related_name='prod_collection')
    
class ProductCollection(models.Model):
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    collectionid = models.ForeignKey(Collection, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)