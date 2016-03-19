from django.shortcuts import render,HttpResponse

# Create your views here.
def index_page(request):
    return render(request,'index.html')

def base_page(request):
    return render(request,'base.html')
