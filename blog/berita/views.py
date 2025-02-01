from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Company,Post,Service,Testimonial,Pricing, Gallery
from .serializers import CompanySerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    companies = Company.objects.all()
    context = {
        'companies':companies,
    }
    return render(request, 'listcompany.html', context)

def company(request, company_slug):
    company = Company.objects.filter(slug=company_slug).first()
    
    if company is None:
        return render(request, '404.html')
    
    testimonials = Testimonial.objects.filter(Company=company)
    services = Service.objects.filter(Company=company)
    pricing = Pricing.objects.filter(Company=company)
    gallery = Gallery.objects.filter(company=company)
    context = {
        'company':company,
        'testimonials':testimonials,
        'services':services,
        'pricing':pricing,
        'gallery':gallery
    }
    return render(request, 'index.html', context)

def post_detail(request, post_id):
    return HttpResponse(f" ini adalah berita dengan ID: {post_id}")

#ViewSet
# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    lookup_field = 'id'

#CBV
# class AuthorListCreateView(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
# class AuthorDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializers
#     lookup_field = 'id'

# class About(View):
#     def get(self, request):
#         context={
#             'name':'Sugeng Tambler',
#             'alamat':'Gunung Bromo, Gunung Kelud'
#         }
#         return render(request, 'about.html', context)
