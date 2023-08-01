from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import PostModel
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,Http404,HttpResponseRedirect
# Create your views here.


def post_model_list_view(request):
    qs = PostModel.objects.all()
    context = {'object_list':qs}
    
    template = 'blog/post_list.html'

    return render(request,template,context)


def post_model_detail_view(request,id):
    qs = get_object_or_404(PostModel,id=id)
    print(qs)
    context = {'object_detail':qs}
    
    template = 'blog/post_detail.html'

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