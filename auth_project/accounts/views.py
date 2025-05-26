from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import BlogPost
from django import forms
from .forms import CustomRegisterForm
from django.contrib.contenttypes.models import ContentType

# Vista de perfil protegida por login
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'username': request.user.username,
        'email': request.user.email
    })

# Registro de usuario
def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')

            # Asignar permisos según el rol
            if role == 'editor':
                content_type = ContentType.objects.get_for_model(BlogPost)
                permiso = Permission.objects.get(codename='can_publish', content_type=content_type)
                user.user_permissions.add(permiso)

            login(request, user)
            return redirect('profile')
    else:
        form = CustomRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

import datetime
from django.utils.timezone import now
from django.contrib.sessions.models import Session

def get_online_users():
    active_sessions = Session.objects.filter(expire_date__gte=now())
    user_ids = []

    for session in active_sessions:
        data = session.get_decoded()
        uid = data.get('_auth_user_id')
        last_seen = data.get('last_seen')
        if uid and last_seen:
            last_seen_dt = datetime.datetime.fromisoformat(last_seen)
            if now() - last_seen_dt < datetime.timedelta(minutes=10):
                user_ids.append(uid)

    return User.objects.filter(id__in=user_ids)

from django.http import JsonResponse

def online_users_view(request):
    users = get_online_users()
    usernames = [user.username for user in users]
    return JsonResponse({
        'cantidad': len(usernames),
        'usuarios': usernames
    })

def landing_page(request):
    return render(request, 'accounts/landing.html')

# Formulario para crear posts
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']

# Listado de posts
@login_required
def blog_list(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'accounts/blog_list.html', {'posts': posts})

# Detalle de un post
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'accounts/blog_detail.html', {'post': post})

# Crear post (requiere permiso)
@permission_required('accounts.can_publish', raise_exception=True)
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'accounts/blog_create.html', {'form': form})


from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Permission

from django.contrib import messages

@user_passes_test(lambda u: u.is_superuser)
def asignar_permiso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            permiso = Permission.objects.get(codename='can_publish')
            user.user_permissions.add(permiso)
            messages.success(request, f'Permiso asignado a {user.username}.')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
        except Permission.DoesNotExist:
            messages.error(request, 'El permiso no existe.')
        return redirect('asignar_permiso')

    usuarios = User.objects.all()
    return render(request, 'accounts/asignar_permiso.html', {'usuarios': usuarios})
