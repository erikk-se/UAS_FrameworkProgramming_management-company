from django.db import models

# Create your models here.
class Author(models.Model):
    nama = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nama
    
class Post(models.Model):
    judul = models.CharField(max_length=250)
    isi = models.TextField()
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
        
class AboutSection(models.Model):
    title = models.CharField(max_length=100, default='untuk kamu')
    content = models.TextField(default='untuk kamu')
    video_url = models.URLField(default='https://www.youtube.com/watch?v=VGq0wZBbOG0')
    image = models.ImageField(upload_to='assets/img/', default='assets/img/about.jpg')

    def __str__(self):
        return self.title

class Company(models.Model):
    nama = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='assets/img/company/', default='assets/img/company/logo.png')
    banner = models.ImageField(upload_to='assets/img/company/', default='assets/img/company/logo.png')
    deskripsi = models.TextField()
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    alamat = models.TextField()
    pelanggan = models.IntegerField()
    projek = models.IntegerField()
    pekerja = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nama

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/img/gallery/', default='assets/img/gallery/gallery-1.jpg')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nama
    
class Testimonial(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    pesan = models.TextField()
    star = models.SmallIntegerField()
    image = models.ImageField(upload_to='assets/img/testimonials/', default='assets/img/testimonials/testimonials-1.jpg')
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nama

class PricingFeatures(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    nama = models.TextField()
    
    def __str__(self):
        return self.nama
    
class Pricing(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()
    periode = models.CharField(max_length=100)
    description = models.TextField()
    features = models.ManyToManyField(PricingFeatures, blank=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nama
