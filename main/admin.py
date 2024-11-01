from django.contrib import admin

from main.models import *
# Register your models here.

class HousePhotoInline(admin.TabularInline):
    model = HousePhoto
class VoiturePhotoInline(admin.TabularInline):
    model = CarPhoto
class ModePhotoInline(admin.TabularInline):
    model = ModePhoto
class BusinessPhotoInline(admin.TabularInline):
    model = BusinessPhoto


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = (HousePhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("category", "description", "prix", "disponibilité", "pour", "ville", "address", )},
        ),
        
    )
    ordering = ("category", "prix")
    list_display = (
        "category",
        "pour",
        "ville",
        "prix",
        "count_photos",
    )
    list_filter = (
        "category",
        "pour",
        "ville",
        "prix",
    )
    search_fields = ("=city", "^host__username")

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_disponibilité = "Photo Count"



@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    inlines = (VoiturePhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("nom", "description", "prix", "disponibilité", "pour", "prix_par_jour", "prix_par_semaine", "prix_par_mois" )},
        ),
        
    )
    ordering = ("nom", "prix")
    list_display = (
        "nom",
        "pour",
        "prix",
        "prix_par_jour",
        "count_photos",
    )
    list_filter = (
        "nom",
        "pour",
        "prix",
        "prix_par_jour",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_disponibilité = "Photo Count"



@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    inlines = (ModePhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("nom", "type", "description", "prix", "disponibilité",)},
        ),
        
    )
    ordering = ("type", "prix")
    list_display = (
        "type",
        "prix",
        "count_photos",
    )
    list_filter = (
        "type",
        "prix",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_disponibilité = "Photo Count"


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    inlines = (BusinessPhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("owner","name","category","description","address","phone_number","email","website","logo","banner","is_featured","premium")},
        ),
        
    )
    list_display = (
        "name",
        "count_photos",
    )
    list_filter = (
        "name",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_disponibilité = "Photo Count"


admin.site.register(Category)
admin.site.register(HouseCategory)
