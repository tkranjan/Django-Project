from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .data import products
from .models import Product
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
class HomePageView(ListView):
    page_title = "Product List"

    def get(self,request:HttpRequest):
        product_list = Product.objects.all()

        return render(
            request, 'index.html',{"title": self.page_title,"products":product_list}
        )


##Detail view

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.all()
    template_name = "product/product_detail.html"


# Create your views here.
"""def homepage(request:HttpRequest) -> HttpResponse:
    page_title = "Product List"
    product_list = Product.objects.all()
    return render(request, "index.html",{'title':page_title, 'products':product_list})"""

# def about(request:HttpRequest) -> HttpResponse:
#     page_title = "About Page"
#     return render(request, "about.html",{'title':page_title})

# def contact(request:HttpRequest) -> HttpResponse:
#     page_title = "Contact Page"
#     return render(request, "contact.html",{'title':page_title})

class AboutPageView(TemplateView):
    template_name = "about.html"
    page_title = "About Page"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context
    
class ContactPageView(TemplateView):
    template_name = "contact.html"
    page_title = "Contact Page"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context



class ProductCreateView(TemplateView):
    template_name = "product/product_create_form.html"

