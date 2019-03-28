from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect

def home(request):
    return render(request,'projects/home.html')

@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
    #  images=Image.objects.filter(user=user)
    #  following1=following(user)
    #  followers1=followers(profile)
    
     return render(request, 'grams/profile.html',{"user":user,"profile": profile})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.user=current_user
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})



# Create your views here.
