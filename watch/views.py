from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('update_profile')
    profiles = Profile.objects.filter(id = current_user.id).all()
    hoods = NeighbourHood.objects.all().order_by('-posted_at')    
    return render(request, 'index.html',{"profiles": profiles, "hoods":hoods})



@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request, 'update-profile.html', {'form': form})
 
 

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    return render(request,'profile.html',{"current_user":current_user, "user":user, "profiles":profiles})
 


@login_required(login_url='/accounts/login/')
def createhood(request):
    current_user = request.user
    form = HoodForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect ('index')
        else:
            form = ProfileForm()
    return render(request,'create-hood.html',{'form':form})
 


@login_required(login_url='/accounts/login/')
def neighbourhood(request,id):
    user = request.user
    posts = Post.objects.all().order_by('-posted_at').filter(neighbourhood_id=id)
    hood = NeighbourHood.objects.get(id=id)
    police = Authority.objects.all().filter(neighbourhood_id=id) 
    health = Health.objects.all().filter(neighbourhood_id=id) 
    businesses = Business.objects.all().filter(neighbourhood_id=id)
    profiles = Profile.objects.filter(user = user).all()
    return render(request,'neighbourhood.html',{'hood':hood,'police':police,'health': health,'posts':posts,'businesses': businesses,'profiles':profiles})
 


@login_required(login_url='/accounts/login/')
def post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    current_user = request.user
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':  
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighbourhood = hood
            post.save()
            return redirect ('neighbourhood', hood_id)
        else:
            form = PostForm()
    return render(request,'post.html',{'hood':hood, 'form':form})
 
 
 
@login_required(login_url='/accounts/login/') 
def createbusiness(request, id):
    hood = NeighbourHood.objects.get(id=id)
    current_user = request.user
    form = BusinessForm(request.POST, request.FILES)
    if request.method == 'POST':   
        if form.is_valid():
            busi = form.save(commit=False)
            busi.user = request.user
            busi.neighbourhood = hood
            busi.save()
            return redirect ('neighbourhood', id=hood.id)
        else:
            form = BusinessForm()
    return render(request,'create-business.html',{'hood':hood, 'form':form})



@login_required(login_url='/accounts/login/')
def search_results(request):
  if 'business' in request.GET and request.GET["business"]:
    search_term = request.GET.get('business')
    searched_users = Business.search_business(search_term)
    message = f"{search_term}"
    return render(request,'search.html',{"message":message,"results":searched_users})
  else:
    message="You haven't searched for any term."  
    return render(request,'search.html',{"message":message,"results":searched_users})



def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('index')


def move_neighbourhood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')
