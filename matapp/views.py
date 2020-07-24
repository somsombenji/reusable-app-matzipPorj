from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Matzip
from .form import MatForm


def index(request):
    return render(request, 'index.html')

#CRUD 함수들
def home(request):
    data = Matzip.objects
    datas = Matzip.objects.all()
    paginator = Paginator(datas, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'data':data, 'posts':posts})

def create(request):
    if request.method=='POST':
        blog = MatForm(request.POST, request.FILES)
        if blog.is_valid():
            new = blog.save(commit=False)
            new.pub_date = timezone.now()
            new.save()
            return redirect('home')
    else:
        form = MatForm()
        return render(request, 'create.html', {'form':form})

def update(request, blog_id):
    blog = get_object_or_404(Matzip, pk=blog_id)
    if request.method == 'POST':
        modify = MatForm(request.POST, request.FILES, instance=blog)
        if modify.is_valid():
            modify.save()
            return redirect('home')
    else:
        content=MatForm(instance=blog)
        return render(request, 'update.html', {'content':content})

def delete(request, blog_id):
    data = get_object_or_404(Matzip, pk=blog_id)
    data.delete()
    return redirect('home')

def detail(request, blog_id):
    data = get_object_or_404(Matzip, pk=blog_id)
    return render(request, 'detail.html', {'data':data})

#로그인 페이지 띄우기
def login(request):
    return render(request, 'login.html')

#API
def api(request):
    return render(request, 'api.html')

def api1(request):
    return render(request, 'api1.html')

def api2(request):
    return render(request, 'api2.html')

def api3(request):
    return render(request, 'api3.html')