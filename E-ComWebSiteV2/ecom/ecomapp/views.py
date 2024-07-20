from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def main(request):
    notes = Note.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'ecomapp/index.html', {"notes": notes})
