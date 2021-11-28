from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'forum/index.html')

def thread_detail(request):
    return render(request, 'forum/thread_detail.html')

def add_thread(request):
    return render(request, 'forum/add_thread.html')