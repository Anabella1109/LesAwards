from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewCommentForm, Profileform, Projectform, Gradeform
from .models import Profile, Project, Grade
from django.contrib.auth.models import User

def home(request):
    projects=Project.objects.all()
    return render(request,'projects/home.html', {'projects':projects})

@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
    #  images=Image.objects.filter(user=user)
    #  following1=following(user)
    #  followers1=followers(profile)
    
     return render(request, 'projects/profile.html',{"user":user,"profile": profile})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.user=current_user
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = Projectform()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def grade_project(request,id):
     current_user=request.user
     project=Project.objects.get(id=id)
     if request.method == 'POST':
        form = Gradeform(request.POST, request.FILES)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = current_user
            grade.project=project
            grade.total=form.cleaned_data['design']+form.cleaned_data['content']+form.cleaned_data['usability']
            grade.save()
        return redirect('home')

     else:
        form = Gradeform()
     return render(request, 'new_grade.html', {"form": form, 'proj':project})



@login_required(login_url='/accounts/login/')
def project(request,id):

    try:
        project = Project.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    grades =Grade.objects.filter(project=project)
    return render(request,"projects/project.html", {"project":project,'grades':grades})


