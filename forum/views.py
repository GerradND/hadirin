from django.contrib import messages
from django.shortcuts import redirect, render
from forum.forms import ThreadForm, ThreadReplyForm
from django.contrib.auth.decorators import login_required
from forum.models import Thread

def home(request):
    threads = Thread.objects.all()
    return render(request, 'forum/index.html', { "threads": threads })

@login_required
def thread_detail(request, pk):
    thread = Thread.objects.get(id = pk)
    return render(request, 'forum/thread_detail.html', { "thread": thread })

@login_required
def add_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.save()
            messages.success(request, 'Thread berhasil dibuat')
            return redirect('forum:home')
        else:
            messages.error(request, form.errors)
    return render(request, 'forum/add_thread.html')

@login_required
def edit_thread(request, pk):
    thread = Thread.objects.get(id = pk)
    if request.user != thread.user:
        messages.error(request,'403: Access Denied')
        return redirect('forum:home')
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('forum:detail_thread', pk=pk)
        else:
            messages.error(request, form.errors)
    return render(request, 'forum/edit_thread.html', { 'thread' : thread })

@login_required
def reply_thread(request, pk):
    if request.method == "POST":
        form = ThreadReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.main_thread = Thread.objects.get(id = pk)
            reply.save()
            return redirect('forum:detail_thread', pk=pk)
        else:
            messages.error(request, form.errors)
    thread = Thread.objects.get(id = pk)
    return render(request, 'forum/reply_thread.html', { 'thread' : thread })

@login_required
def delete_thread(request, pk):
    thread = Thread.objects.get(id = pk)
    if request.user != thread.user:
        messages.error(request,'403: Access Denied')
        return redirect('forum:home')
    if request.method == 'POST':
        thread.delete()
        messages.success(request, 'Thread berhasil dihapus')
        return redirect('forum:home')
    return render(request, 'forum/delete_thread.html', { "thread" : thread })