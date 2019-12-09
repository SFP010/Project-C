from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.views.generic import DetailView
from art.models import Artwork
from .forms import UserRegistrationForm, UserUpdateForm, ProfilePhotoUpdateForm, ProfileInfoForm ,isArtist
from .functions import send_confirmation_email
from .tokens import account_activation_token

# Create your views here.


class ArtistCard(DetailView):
    model = User
    template_name = 'artistCard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArtistCard, self).get_context_data(*args, **kwargs)
        context['User'] = User.objects.all()
        context['Artwork'] = Artwork.objects.all()
        return context


def register(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in!")

    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'account created for {username}')

                email = form.cleaned_data.get('email')
                send_confirmation_email(request, form, user, email)

                # return redirect('login_page')
                return render(request,'email/email_sent.html')
            # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = UserRegistrationForm()
        return render(request,'users/register.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request,'email/confirmation_complete.html')
    else:
        return render(request,'email/invalid_link.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_photo_update_form = ProfilePhotoUpdateForm(request.POST,request.FILES,
                                                        instance=request.user.userprofile)
        profile_info_update_form = ProfileInfoForm(request.POST,instance=request.user.userprofile)
        if user_update_form.is_valid and profile_photo_update_form.is_valid and profile_info_update_form.is_valid:
            user_update_form.save()
            profile_info_update_form.save()
            profile_photo_update_form.save()
            messages.success(request, f'Your profile information is updated')
            return redirect('profile_page')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_info_update_form = ProfileInfoForm(instance=request.user.userprofile)
        profile_photo_update_form = ProfilePhotoUpdateForm(instance=request.user.userprofile)
    context ={
        'user_update_form': user_update_form,
        'profile_photo_update_form': profile_photo_update_form,
        'profile_info_update_form': profile_info_update_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def isartist(request):
    if request.method == 'POST':
        form = isArtist(request.POST,request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.applicant = request.user.userprofile
            instance.save()
            messages.success(request, f'Your request  is received')
            return redirect('home_page')
    else:
        form = isArtist()
    return render(request, 'isartist.html', {'form': form})
