from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse
from models import User


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                opts = {
                    'use_https': request.is_secure(),
                    'token_generator': default_token_generator,
                    'from_email': None,
                    'email_template_name': 'registration/password_reset_email.html',
                    'subject_template_name': 'registration/password_reset_subject.txt',
                    'request': request,
                }
                form.save(**opts)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


def password_reset_confirm(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse('password_reset_complete'),
        template_name='registration/password_reset_confirm.html',
        extra_context={'uidb64': uidb64, 'token': token}
    )(request, uidb64=uidb64, token=token)


def password_reset_complete(request):
    return auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html')(request)