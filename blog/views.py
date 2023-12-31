from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import PostModel
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,Http404,HttpResponseRedirect
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def post_model_list_view(request):
    qs = PostModel.objects.all()
    query = request.GET.get('q')
    if query is not None:
        qs = PostModel.objects.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(slug__icontains=query)
        )
    context = {'object_list':qs}
    
    template = 'blog/post_list.html'

    return render(request,template,context)


def post_model_detail_view(request,id):
    qs = get_object_or_404(PostModel,id=id)
    print(qs)
    context = {'object_detail':qs}
    
    template = 'blog/post_detail.html'

    return render(request,template,context)


def post_model_create_view(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,"created a new blog post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

    context = {'form':form}
    
    template = 'blog/post_create.html'

    return render(request,template,context)


def post_model_update_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,"Updated post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

    context = {'form':form}
    
    template = 'blog/post_update.html'

    return render(request,template,context)


def post_model_delete_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    if request.method=='POST':
        obj.delete()
        messages.success(request,"Deleted post!")

        return HttpResponseRedirect("/blog/")

    

    context = {'object':obj}
    
    template = 'blog/post_delete.html'

    return render(request,template,context)








@login_required(login_url='/login/')
def login_required_list_view(request):
    qs = PostModel.objects.all()
    context = {'qs':qs}
    if request.user.is_authenticated():
        template = 'blog/post_list.html'
    else:
        template = 'blog/post_list_public.html'  
        return HttpResponseRedirect('/login')  
    print(request.user)
    return render(request,template,context)