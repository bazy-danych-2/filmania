from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')



class Final(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/final.html')