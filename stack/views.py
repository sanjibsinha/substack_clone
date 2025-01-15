from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from stack.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

@login_required
def profile_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        request.user.username = username
        request.user.email = email
        request.user.save()
        update_session_auth_hash(request, request.user)  # Keep the user logged in after changes
        return HttpResponse("Profile updated successfully!")

    return render(request, 'profile.html')

@login_required
def user_dashboard(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(author=request.user)

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    return render(request, 'dashboard.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        Post.objects.create(
            author=request.user,
            title=title,
            content=content
        )
        return redirect('index')
    return render(request, 'create_post.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return HttpResponse("Passwords do not match!")
        
        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse("Username already taken!")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('logout')

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Store in the database (simplified for now)
        print(f"New Subscriber: {email}")
        return HttpResponse("Thank you for subscribing!")
    return render(request, 'subscribe.html')
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return HttpResponse("You are not authorized to edit this post.")

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', post_id=post.id)

    return render(request, 'edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return HttpResponse("You are not authorized to delete this post.")

    post.delete()
    return redirect('index')