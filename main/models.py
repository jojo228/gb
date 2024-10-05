from django.db import models
from enum import Enum
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    PREMIUM_CHOICES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    )
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    premium = models.CharField(max_length=10, choices=PREMIUM_CHOICES, default='basic')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class HouseType(Enum):
    PIECE = "Pièce"
    DEUX_CHAMBRE_SALON = "Deux chambres salon"
    TROIS_CHAMBRE_SALON = "Trois chambres salon"
    VILLA = "Villa"
    MAISON = "Maison"
    APPARTEMENT = "Appartement"
    BUREAU = "Bureau"
    BOUTIQUE = "Boutique"
    APPARTEMENT_MEUBLES = "Appartement Meublé"
    TERRAINS_RURAUX = "Terrain Rural"
    TERRAINS_URBAINS = "Terrain Urbains"


class ClotheType(Enum):
    TSHIRT = "T-SHIRTS ET POLO"
    PANTALONS = "PANTALONS"
    BIJOUX = "BIJOUX"
    CHAUSSURES_SACS = "CHAUSSURES ET SACS"
    MECHES = "MÈCHES"


class HousePhoto(models.Model):
    caption = models.CharField(max_length=80)
    file = models.FileField(upload_to="house_photos")
    house = models.ForeignKey("House", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    
class CarPhoto(models.Model):
    caption = models.CharField(max_length=80)
    file = models.FileField(upload_to="voiture_photos")
    voiture = models.ForeignKey("Voiture", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    
class ModePhoto(models.Model):
    caption = models.CharField(max_length=80)
    file = models.FileField(upload_to="vest_photos")
    mode = models.ForeignKey("Mode", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    


class House(models.Model):

    HOUSE_AVAILABILITY = [
        ("Disponible", "Disponible"),
        ("Non Disponible", "Non Disponible"),
    ]

    HOUSE_FOR = [
        ("Location", "Location"),
        ("Vente", "Vente"),
    ]

    type = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in HouseType])
    description = models.TextField()
    disponibilité = models.CharField(max_length=20, choices=HOUSE_AVAILABILITY,)
    pour = models.CharField(max_length=20, choices=HOUSE_FOR,)
    ville = models.CharField(max_length=80)
    prix = models.CharField(max_length=80, default=0)
    caution = models.CharField(max_length=80, default=0)
    address = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        self.ville = str.capitalize(self.ville)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("house_detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
    


class Voiture(models.Model):

    CAR_AVAILABILITY = [
        ("Disponible", "Disponible"),
        ("Non Disponible", "Non Disponible"),
    ]

    CAR_FOR = [
        ("Location", "Location"),
        ("Vente", "Vente"),
    ]
    nom = models.CharField(max_length=200)
    description = models.TextField()
    disponibilité = models.CharField(max_length=20, choices=CAR_AVAILABILITY,)
    pour = models.CharField(max_length=20, choices=CAR_FOR,)
    prix = models.CharField(max_length=80, default=0)
    prix_par_jour = models.IntegerField(default=0)
    prix_par_semaine = models.IntegerField(default=0)
    prix_par_mois = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("voiture_detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
    


class Mode(models.Model):

    HOUSE_AVAILABILITY = [
        ("Disponible", "Disponible"),
        ("Non Disponible", "Non Disponible"),
    ]

    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in ClotheType])
    description = models.TextField()
    disponibilité = models.CharField(max_length=20, choices=HOUSE_AVAILABILITY,)
    prix = models.CharField(max_length=80, default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom


    def get_absolute_url(self):
        return reverse("vest_detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
    

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    house = models.ForeignKey("House", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.house}'"