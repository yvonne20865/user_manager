from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import CustomUser
from .utils import send_sms
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Require email verification
            user.is_verified = False
            user.is_phone_verified = True  # Skip SMS verification
            user.save()
            # Send email verification
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"{request.scheme}://{request.get_host()}/accounts/activate/{uid}/{token}/"
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'activation_link': activation_link,
            })
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            return render(request, 'accounts/activation_success.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_verified = True
        user.is_active = True
        user.save()
        # Redirect to dashboard after activation
        return redirect('dashboard')
    else:
        return render(request, 'accounts/activation_invalid.html')

@csrf_exempt
def verify_sms(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        user_id = request.session.get('sms_user_id')
        sms_code = request.session.get('sms_code')
        if code == sms_code and user_id:
            user = CustomUser.objects.get(pk=user_id)
            user.is_phone_verified = True
            user.save()
            # Optionally log the user in here
            return redirect('login')
        else:
            return render(request, 'accounts/verify_sms.html', {'error': 'Invalid code'})
    return render(request, 'accounts/verify_sms.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
