from django.contrib import admin
from .models import Author, Post, AboutSection, Company, Service, Testimonial, Pricing, Gallery, PricingFeatures

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("nama", "bio")
    list_filter = ("nama",)
    search_fields = ("nama","bio")

class PostAdmin(admin.ModelAdmin):
    list_display = ("judul", "isi", "author")
    list_filter = ("judul", "author")
    search_fields = ("judul", "isi", "author__nama")
    list_per_page = 2

class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "video_url", "image")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("nama", "deskripsi", "email", "whatsapp", "instagram", "facebook", "twitter", "alamat", "pelanggan", "projek", "pekerja")
    list_filter = ("nama", "deskripsi", "email", "whatsapp", "instagram", "facebook", "twitter", "alamat", "pelanggan", "projek", "pekerja")
    search_fields = ("nama", "deskripsi", "email", "whatsapp", "instagram", "facebook", "twitter", "alamat", "pelanggan", "projek", "pekerja")

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("nama", "deskripsi", "Company")
    list_filter = ("nama", "Company")
    search_fields = ("nama", "deskripsi", "Company")

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("nama", "jabatan", "pesan", "star", "image", "Company")
    list_filter = ("nama", "jabatan", "star", "Company")
    search_fields = ("nama", "jabatan", "pesan", "star", "image", "Company")

class PricingAdmin(admin.ModelAdmin):
    list_display = ("nama", "harga", "periode", "description", "featured", "Company")
    list_filter = ("nama", "harga", "periode", "featured", "Company")
    search_fields = ("nama", "harga", "periode", "description", "featured", "Company")

class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "company")
    list_filter = ("title", "company")
    search_fields = ("title", "image", "company")

class PricingFeaturesAdmin(admin.ModelAdmin):
    list_display = ("Company", "nama")
    list_filter = ("Company", "nama")
    search_fields = ("Company", "nama")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Pricing)
admin.site.register(Gallery)
admin.site.register(PricingFeatures)