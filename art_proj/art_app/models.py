from django.db import models

# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    password =  models.CharField(max_length = 50)
    is_customer = models.BooleanField(default = False)
    is_artist = models.BooleanField(default = False)
    city = models.CharField(max_length = 50)

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Artist(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True) 
    bio = models.TextField()
    img = models.ImageField(upload_to='images/')

class Customer(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

class Artwork(models.Model):
    title = models.CharField(max_length = 45)
    description = models.TextField()
    quantity = models.IntegerField()
    size = models.CharField(max_length = 15)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    artist = models.ForeignKey(Artist, related_name="artworks", on_delete= models.CASCADE)
    customer = models.ManyToManyField(Customer, related_name = "purchases")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def price_display(self):
    #     return "$%s" % self.price

class ArtworkImage(models.Model):
    name = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    artwork = models.ForeignKey(Artwork, related_name="images", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review_txt = models.TextField()
    artwork = models.ForeignKey(Artwork, related_name = "reviews", on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, related_name = "reviews", on_delete = models.CASCADE)

    #date & time stamps
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)