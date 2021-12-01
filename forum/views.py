from django.contrib import messages
from django.shortcuts import redirect, render

# Dummy Data
thread = {
    'user' : 'Budi Budiman',
    'title' : "Lorem ipsum dolor sit amet conquistador",
    'content' : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    'replies' : [
        {
            'user' : 'Susan Susanti', 
            'content' : 'Saya Setuju dengan pendapat anda' 
        },
        {
            'user' : 'Rudi Rudiman', 
            'content' : 'Saya tidak etuju' 
        }
    ]
}

# threads = [thread, thread]

# Create your views here.
def home(request):
    return render(request, 'forum/index.html')

def thread_detail(request):
    return render(request, 'forum/thread_detail.html')

def add_thread(request):
    if request.method == 'POST':
        messages.success(request, 'Thread berhasil dibuat')
        return redirect('forum:home')
    return render(request, 'forum/add_thread.html')

def edit_thread(request):
    return render(request, 'forum/edit_thread.html', {'thread' : thread})

def reply_thread(request):
    return render(request, 'forum/reply_thread.html')

def delete_thread(request):
    if request.method == 'POST':
        messages.success(request, 'Thread berhasil dihapus')
        return redirect('forum:home')
    return render(request, 'forum/delete_thread.html')