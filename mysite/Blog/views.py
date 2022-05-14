from django.shortcuts import render, get_object_or_404, redirect
from .forms import PageForm
from .models import Page

def index(request):
    object_list = Page.objects.all()
    return render(request, 'Blog/home.html', {'object_list': object_list})

def detail(request, page_id):
    object_detail = get_object_or_404(Page,id=page_id)
    return render(request, 'Blog/page_detail.html', {'object_detail': object_detail})

def create(request):
    if request.method=='POST':
        form = PageForm(request.POST)
        new_page = form.save()
        return redirect('page-detail', page_id=new_page.id)
    else:
        form=PageForm()
        return render(request,'Blog/page_create.html', {'form':form})


def update (request, page_id):
    page = get_object_or_404(Page,id=page_id)
    if request.method=='POST':
        form = PageForm(request.POST, instance=page)
        form.save()
        return redirect('page-detail', page_id=page.id)
    else:
        form=PageForm(instance=page)
        return render(request,'Blog/page_create.html', {'form':form})


def delete(request, page_id):
    page = get_object_or_404(Page,id=page_id)
    page.delete()
    return redirect('page-list')
