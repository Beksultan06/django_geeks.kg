from django.shortcuts import render
from django.views import generic
from apps.posts.models import Post, TeamMember, Courses, Front, Back

class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "posts"

class AboutView(generic.ListView):
    queryset = TeamMember.objects.all()
    template_name = 'about.html'
    context_object_name = 'posts'

class CousersView(generic.ListView):
    queryset = Courses.objects.all()
    template_name = 'cousers.html'
    context_object_name = "posts"

class FrontView(generic.ListView):
    queryset = Front.objects.all()
    template_name = 'front.html'
    context_object_name = "posts"

class BakcView(generic.ListView):
    queryset = Back.objects.all()
    template_name = 'backend.html'
    context_object_name = "posts"

